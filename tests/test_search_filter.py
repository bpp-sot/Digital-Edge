from datetime import datetime, timezone
from types import SimpleNamespace

import search_filter


def make_config(docs_dir):
    return SimpleNamespace(
        docs_dir=str(docs_dir),
        site_url="https://example.com/",
        site_name="Digital Edge",
    )


def write_article(articles_dir, slug, *, title, description, author, date, type_="article"):
    articles_dir.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        f'title: "{title}"\n'
        f'description: "{description}"\n'
        f'author: "{author}"\n'
        f'date: "{date}"\n'
        f"type: {type_}\n"
        "---\n\n"
        f"# {title}\n"
    )
    (articles_dir / f"{slug}.md").write_text(content, encoding="utf-8")


class TestParseFrontmatter:
    def test_parses_quoted_and_unquoted_values(self):
        text = '---\ntitle: "Hello World"\ndate: 2026-01-01\n---\n\nBody\n'
        fields = search_filter.parse_frontmatter(text)
        assert fields["title"] == "Hello World"
        assert fields["date"] == "2026-01-01"

    def test_returns_empty_dict_when_no_frontmatter(self):
        assert search_filter.parse_frontmatter("# Just a heading\n") == {}

    def test_first_occurrence_of_a_key_wins(self):
        text = '---\ntitle: "First"\ntitle: "Second"\n---\n'
        fields = search_filter.parse_frontmatter(text)
        assert fields["title"] == "First"


class TestLatestArticle:
    def test_picks_the_most_recently_dated_article(self, tmp_path):
        articles_dir = tmp_path / "articles"
        write_article(articles_dir, "old", title="Old", description="d", author="A", date="2026-01-01")
        write_article(articles_dir, "new", title="New", description="d", author="A", date="2026-06-01")

        article = search_filter.latest_article(make_config(tmp_path))

        assert article["slug"] == "new"

    def test_skips_index_and_non_article_types(self, tmp_path):
        articles_dir = tmp_path / "articles"
        write_article(articles_dir, "index", title="Index", description="d", author="A", date="2026-06-01")
        write_article(
            articles_dir, "not-article", title="Not", description="d", author="A", date="2026-06-02", type_="guide"
        )
        write_article(articles_dir, "real", title="Real", description="d", author="A", date="2026-01-01")

        article = search_filter.latest_article(make_config(tmp_path))

        assert article["slug"] == "real"

    def test_returns_none_when_no_articles_dir(self, tmp_path):
        assert search_filter.latest_article(make_config(tmp_path)) is None


class TestAuthorLatestDates:
    def test_tracks_each_authors_most_recent_date(self, tmp_path):
        articles_dir = tmp_path / "articles"
        write_article(articles_dir, "a1", title="A1", description="d", author="Alice", date="2026-01-01")
        write_article(articles_dir, "a2", title="A2", description="d", author="Alice", date="2026-03-01")
        write_article(articles_dir, "b1", title="B1", description="d", author="Bob", date="2026-02-01")

        dates = search_filter.author_latest_dates(make_config(tmp_path))

        assert dates["Alice"] == datetime(2026, 3, 1, tzinfo=timezone.utc)
        assert dates["Bob"] == datetime(2026, 2, 1, tzinfo=timezone.utc)


class TestReorderPersonCards:
    def test_sorts_cards_by_authors_latest_article_newest_first(self, tmp_path):
        articles_dir = tmp_path / "articles"
        write_article(articles_dir, "a1", title="A1", description="d", author="Alice", date="2026-01-01")
        write_article(articles_dir, "b1", title="B1", description="d", author="Bob", date="2026-06-01")
        # Carol has no article at all, so she should sort last.

        markdown = (
            '<article class="de-person-card">de-person-card__name" href="alice/">Alice</a></article>'
            '<article class="de-person-card">de-person-card__name" href="bob/">Bob</a></article>'
            '<article class="de-person-card">de-person-card__name" href="carol/">Carol</a></article>'
        )

        result = search_filter.reorder_person_cards(markdown, make_config(tmp_path))

        assert result.index("Bob") < result.index("Alice") < result.index("Carol")

    def test_returns_markdown_unchanged_when_no_cards_present(self, tmp_path):
        markdown = "<p>No cards here.</p>"
        assert search_filter.reorder_person_cards(markdown, make_config(tmp_path)) == markdown


class TestFeaturedArticleFallback:
    def test_featured_article_card_falls_back_when_no_articles(self, tmp_path):
        card = search_filter.featured_article_card(make_config(tmp_path))
        assert "<!-- de-feature-article:start -->" in card
        assert "Read the Latest Articles" in card

    def test_featured_article_hero_falls_back_when_no_articles(self, tmp_path):
        hero = search_filter.featured_article_hero(make_config(tmp_path))
        assert "<!-- de-feature-article-hero:start -->" in hero
        assert "Read the Latest Articles" in hero

    def test_featured_article_card_uses_latest_article(self, tmp_path):
        articles_dir = tmp_path / "articles"
        write_article(articles_dir, "new", title="Newest Article", description="A great read.", author="A", date="2026-06-01")

        card = search_filter.featured_article_card(make_config(tmp_path))

        assert "Newest Article" in card
        assert "articles/new/" in card


def event_card(title, *, status="Upcoming", start=None, classes="de-event-card"):
    start_attr = f'\n  data-event-start="{start}"' if start else ""
    return (
        f'<button\n  class="{classes}"\n  type="button"\n'
        f'  data-event-title="{title}"\n  data-event-status="{status}"{start_attr}\n'
        f'  data-event-description="About {title}."\n>\n  <strong>{title}</strong>\n</button>\n'
    )


class TestNextFeaturedEvent:
    def test_picks_the_soonest_upcoming_event_including_modifier_classes(self, tmp_path):
        (tmp_path / "events.md").write_text(
            event_card("Later", start="2099-03-01T12:00:00+00:00")
            + event_card("Sooner", start="2099-01-12T13:00:00+00:00", classes="de-event-card de-event-card--session"),
            encoding="utf-8",
        )

        event = search_filter.next_featured_event(make_config(tmp_path))

        assert event["title"] == "Sooner"
        assert event["summary"] == "About Sooner."

    def test_skips_past_undated_and_already_started_events(self, tmp_path):
        (tmp_path / "events.md").write_text(
            event_card("Marked past", status="Past", start="2099-01-01T12:00:00+00:00", classes="de-event-card de-event-card--past")
            + event_card("No date yet", classes="de-event-card de-event-card--live")
            + event_card("Already happened", start="2000-01-01T12:00:00+00:00")
            + event_card("Next one", start="2099-06-01T12:00:00+01:00"),
            encoding="utf-8",
        )

        event = search_filter.next_featured_event(make_config(tmp_path))

        assert event["title"] == "Next one"


class TestOnPostBuildExternalLinks:
    def test_adds_new_tab_attributes_to_known_external_links(self, tmp_path):
        site_dir = tmp_path / "site"
        site_dir.mkdir()
        (site_dir / "index.html").write_text(
            f'<a href="{search_filter.SPOTIFY_URL}">Podcast</a>'
            f'<a href="{search_filter.VIRTUAL_CAMPUS_URL}">Virtual Campus</a>'
            '<a href="/people/">People</a>',
            encoding="utf-8",
        )

        search_filter.on_post_build(SimpleNamespace(site_dir=str(site_dir)))

        html = (site_dir / "index.html").read_text(encoding="utf-8")
        assert f'<a href="{search_filter.SPOTIFY_URL}" target="_blank" rel="noopener noreferrer">' in html
        assert f'<a href="{search_filter.VIRTUAL_CAMPUS_URL}" target="_blank" rel="noopener noreferrer">' in html
        assert '<a href="/people/">People</a>' in html

    def test_does_not_duplicate_attributes_if_already_present(self, tmp_path):
        site_dir = tmp_path / "site"
        site_dir.mkdir()
        already_tagged = (
            f'<a href="{search_filter.SPOTIFY_URL}" target="_blank" rel="noopener noreferrer">Podcast</a>'
        )
        (site_dir / "index.html").write_text(already_tagged, encoding="utf-8")

        search_filter.on_post_build(SimpleNamespace(site_dir=str(site_dir)))

        html = (site_dir / "index.html").read_text(encoding="utf-8")
        assert html.count("target=") == 1
