from datetime import date
from types import SimpleNamespace

import article_macros


class FakeEnv:
    """Stands in for mkdocs-macros-plugin's env: @env.macro just registers the function."""

    def __init__(self, conf=None):
        self.macros = {}
        self.conf = conf or {}

    def macro(self, func):
        self.macros[func.__name__] = func
        return func


def load_macros(conf=None):
    env = FakeEnv(conf)
    article_macros.define_env(env)
    return env.macros


def make_page(meta):
    return SimpleNamespace(meta=meta)


def test_article_hero_renders_full_meta_with_role():
    macros = load_macros()
    page = make_page(
        {
            "tags": ["AI", "Careers"],
            "title": "Test Title",
            "description": "Fallback description",
            "author": "Jane Doe",
            "author_slug": "jane-doe",
            "author_role": "Head of Something",
            "date_display": "1 January 2026",
            "read_time": "5 min read",
            "hero_pill": "Big question",
            "hero_quote": "A quote.",
        }
    )

    html = macros["article_hero"](page)

    assert '<a href="../?tag=AI">AI</a>' in html
    assert '<a href="../?tag=Careers">Careers</a>' in html
    assert "<h1>Test Title</h1>" in html
    assert "<p>Fallback description</p>" in html
    assert '<a href="../../people/jane-doe/">Jane Doe</a>' in html
    assert "<span>Head of Something</span>" in html
    assert "<span>1 January 2026</span>" in html
    assert "<span>5 min read</span>" in html
    assert '<span class="de-pill">Big question</span>' in html
    assert "<p>A quote.</p>" in html


def test_article_hero_omits_role_span_when_no_author_role():
    macros = load_macros()
    page = make_page(
        {
            "title": "T",
            "description": "D",
            "author": "A",
            "author_slug": "a",
            "date_display": "1 January 2026",
            "read_time": "5 min read",
        }
    )

    html = macros["article_hero"](page)

    # No author_role means the meta div goes straight from the name link to the date span.
    assert '<a href="../../people/a/">A</a>\n      <span>1 January 2026</span>' in html


def test_article_hero_lede_falls_back_to_description():
    macros = load_macros()
    page = make_page({"title": "T", "description": "Fallback lede"})

    html = macros["article_hero"](page)

    assert "<p>Fallback lede</p>" in html


def test_article_hero_lede_overrides_description_when_set():
    macros = load_macros()
    page = make_page({"title": "T", "description": "SEO text", "lede": "On-page lede"})

    html = macros["article_hero"](page)

    assert "<p>On-page lede</p>" in html
    assert "<p>SEO text</p>" not in html


def test_article_summary_renders_bullets():
    macros = load_macros()
    page = make_page({"summary": ["First point.", "Second point."]})

    html = macros["article_summary"](page)

    assert "<h2>Article Summary</h2>" in html
    assert "<li>First point.</li>" in html
    assert "<li>Second point.</li>" in html


def test_article_takeaways_renders_cards():
    macros = load_macros()
    page = make_page({"takeaways": [{"label": "L1", "text": "T1"}, {"label": "L2", "text": "T2"}]})

    html = macros["article_takeaways"](page)

    assert "<strong>L1</strong>" in html
    assert "<p>T1</p>" in html
    assert "<strong>L2</strong>" in html
    assert "<p>T2</p>" in html


def test_discussion_box_renders_questions():
    macros = load_macros()
    page = make_page({"discussion": ["Q1?", "Q2?"]})

    html = macros["discussion_box"](page)

    assert "Use This In A Discussion" in html
    assert "<li>Q1?</li>" in html
    assert "<li>Q2?</li>" in html


def test_related_reading_renders_cards():
    macros = load_macros()
    page = make_page(
        {"related": [{"tag": "AI", "title": "Title1", "description": "Desc1", "href": "../foo/"}]}
    )

    html = macros["related_reading"](page)

    assert '<a class="de-card" href="../foo/">' in html
    assert '<span class="de-card__label">AI</span>' in html
    assert "<h3>Title1</h3>" in html
    assert "<p>Desc1</p>" in html


def test_spotlight_hero_renders_name_role_kicker_and_pulled_quote():
    macros = load_macros()
    page = make_page({"name": "Test Person", "role": "Test Role", "hero_quote": "A pulled quote."})

    html = macros["spotlight_hero"](page)

    assert '<p class="de-kicker">Off The Job: Staff Spotlight</p>' in html
    assert "<h1>Test Person</h1>" in html
    assert "<p>Test Role</p>" in html
    assert '<span class="de-pill">In their own words</span>' in html
    assert "<p>A pulled quote.</p>" in html


def test_spotlight_quickfire_renders_question_answer_tiles():
    macros = load_macros()
    page = make_page({"quickfire": [{"question": "Ultimate meal", "answer": "Pizza."}]})

    html = macros["spotlight_quickfire"](page)

    assert "<h2>Quick Fire Round</h2>" in html
    assert "<span>Ultimate meal</span>" in html
    assert "<p>Pizza.</p>" in html


def test_spotlight_interview_renders_single_paragraph_answer():
    macros = load_macros()
    page = make_page({"interview": [{"question": "Q1?", "answer": "One paragraph."}]})

    html = macros["spotlight_interview"](page)

    assert "<h2>The Interview</h2>" in html
    assert "<h3>Q1?</h3>" in html
    assert "<p>One paragraph.</p>" in html


def test_spotlight_interview_splits_multi_paragraph_answer_into_separate_p_tags():
    macros = load_macros()
    page = make_page({"interview": [{"question": "Q1?", "answer": "First paragraph.\n\nSecond paragraph."}]})

    html = macros["spotlight_interview"](page)

    assert "<p>First paragraph.</p><p>Second paragraph.</p>" in html


def test_related_reading_uses_related_heading_when_set():
    macros = load_macros()
    page = make_page({"related_heading": "More Community News", "related": []})

    html = macros["related_reading"](page)

    assert "<h2>More Community News</h2>" in html


def write_story(directory, name, frontmatter):
    (directory / f"{name}.md").write_text(f"---\n{frontmatter}\n---\n\n# {name}\n", encoding="utf-8")


def test_news_stories_skips_pages_without_date_or_label_and_sorts_newest_first(tmp_path):
    news = tmp_path / "community-news"
    news.mkdir()
    write_story(news, "index", 'title: "Community News"')
    write_story(news, "staff-spotlight", 'title: "Spotlight"\nname: "Someone"')
    write_story(news, "older", 'title: "Older"\nnews_label: "Event"\ndate: 2025-02-01')
    write_story(news, "newer", 'title: "Newer"\nnews_label: "Event"\ndate: 2026-02-01')

    stories = article_macros.news_stories(tmp_path)

    assert [story["slug"] for story in stories] == ["newer", "older"]


def test_news_stories_lists_winners_before_finalists_in_the_same_month(tmp_path):
    news = tmp_path / "community-news"
    news.mkdir()
    write_story(news, "a-finalist", 'title: "F"\nnews_label: "BCS Awards"\ndate: 2025-09-01\nhero_award:\n  tier: "Finalist"')
    write_story(news, "z-winner", 'title: "W"\nnews_label: "BCS Awards"\ndate: 2025-09-01\nhero_award:\n  tier: "Winner"')

    stories = article_macros.news_stories(tmp_path)

    assert [story["slug"] for story in stories] == ["z-winner", "a-finalist"]


def test_news_card_renders_label_month_accent_and_award_tier():
    story = {
        "slug": "zoe",
        "title": "Long SEO title",
        "card_title": "Zoe Hurst",
        "description": "Desc",
        "news_label": "BCS Awards",
        "date": date(2025, 8, 1),
        "hero_award": {"tier": "Highly Commended"},
    }

    html = article_macros.news_card(story)

    assert '<a class="de-card de-news-card de-news-card--gold" href="zoe/">' in html
    assert '<span class="de-card__label">BCS Awards</span>' in html
    assert '<time datetime="2025-08-01">August 2025</time>' in html
    assert "<h3>Zoe Hurst</h3>" in html
    assert '<span class="de-news-card__tier de-news-card__tier--highly-commended">Highly Commended</span>' in html


def test_news_listing_filters_by_year_and_handles_an_empty_year(tmp_path):
    news = tmp_path / "community-news"
    news.mkdir()
    write_story(news, "this-year", 'title: "This year"\nnews_label: "Event"\ndate: 2026-03-01')
    write_story(news, "last-year", 'title: "Last year"\nnews_label: "Event"\ndate: 2025-03-01')
    macros = load_macros({"docs_dir": str(tmp_path)})

    html = macros["news_listing"](2026)

    assert 'href="this-year/"' in html
    assert 'href="last-year/"' not in html
    assert "No stories yet." in macros["news_listing"](2024)


def test_story_hero_renders_award_medal():
    macros = load_macros()
    page = make_page(
        {
            "title": "SEO title",
            "heading": "Zoe Hurst",
            "lede": "Lede.",
            "news_label": "BCS Awards",
            "date_display": "August 2025",
            "hero_award": {"tier": "Highly Commended", "category": "Software Apprentice of the Year", "year": 2025},
        }
    )

    html = macros["story_hero"](page)

    assert "<h1>Zoe Hurst</h1>" in html
    assert '<aside class="de-story-medal de-story-medal--highly-commended">' in html
    assert "<strong>Highly Commended</strong>" in html
    assert "Software Apprentice of the Year" in html
    assert "<span>BCS Awards</span><span>August 2025</span>" in html
    assert "de-news-hero--single" not in html


def test_story_hero_renders_image_stat_or_single_column():
    macros = load_macros()

    image_html = macros["story_hero"](make_page({"title": "T", "image": "pic.jpg", "image_alt": "Alt", "image_fit": "portrait"}))
    stat_html = macros["story_hero"](make_page({"title": "T", "hero_stat": {"value": "17", "label": "finalists"}}))
    plain_html = macros["story_hero"](make_page({"title": "T"}))

    assert '<aside class="de-story-hero__media de-story-hero__media--portrait">' in image_html
    assert '<img src="pic.jpg" alt="Alt">' in image_html
    assert "<strong>17</strong>" in stat_html
    assert "<p>finalists</p>" in stat_html
    assert "de-news-hero--single" in plain_html


def test_story_hero_links_author_byline_to_their_profile():
    macros = load_macros()
    page = make_page({"title": "T", "author": "David Green", "author_slug": "david-green"})

    html = macros["story_hero"](page)

    assert '<span>By <a href="../../people/david-green/">David Green</a></span>' in html


def test_story_sessions_renders_slot_format_and_people_chips():
    macros = load_macros()
    page = make_page(
        {
            "sessions": [
                {
                    "slot": "Morning",
                    "format": "Panel",
                    "title": "Can AI Be Truly Creative?",
                    "people": [
                        {"name": "Gemma McKay", "role": "Award Lead", "href": "../../people/gemma-mckay/"},
                        {"name": "Dominic Lyons", "href": "https://www.linkedin.com/in/example/"},
                        "Tony Pitchford",
                    ],
                }
            ]
        }
    )

    html = macros["story_sessions"](page, layout="grid")

    assert '<ol class="de-story-sessions de-story-sessions--grid">' in html
    assert '<span class="de-story-sessions__slot">Morning</span>' in html
    assert '<span class="de-card__label">Panel</span>' in html
    assert '<a href="../../people/gemma-mckay/">Gemma McKay <small>Award Lead</small></a>' in html
    assert '<a href="https://www.linkedin.com/in/example/" target="_blank" rel="noopener noreferrer">Dominic Lyons</a>' in html
    assert "<span>Tony Pitchford</span>" in html


def test_award_board_renders_tiers_and_finalists_with_story_links():
    macros = load_macros()
    page = make_page(
        {
            "board": [
                {
                    "tier": "Winner",
                    "heading": "Winners",
                    "entries": [{"name": "Chantelle Hunt", "category": "Cat", "provider": "Estio", "href": "../chantelle/"}],
                }
            ],
            "finalists": [{"provider": "Firebrand", "people": [{"name": "Tom Collier"}]}],
        }
    )

    html = macros["award_board"](page)

    assert '<div class="de-award-board__tier de-award-board__tier--winner">' in html
    assert "<h3>Winners</h3>" in html
    assert '<strong><a href="../chantelle/">Chantelle Hunt</a></strong>' in html
    assert "<em>Estio</em>" in html
    assert "<h3>Firebrand</h3>" in html
    assert "<li>Tom Collier</li>" in html


def test_story_cta_styles_first_link_primary_and_opens_external_links_in_new_tab():
    macros = load_macros()
    page = make_page(
        {
            "listen": {
                "title": "Listen",
                "text": "Out now.",
                "links": [
                    {"label": "Spotify", "href": "https://open.spotify.com/episode/x", "style": "spotify"},
                    {"label": "Events", "href": "../../events/"},
                    {"label": "Podcasts", "href": "../../podcast/"},
                ],
            }
        }
    )

    html = macros["story_cta"](page, "listen")

    assert '<a class="de-button de-button--spotify" href="https://open.spotify.com/episode/x" target="_blank" rel="noopener noreferrer">Spotify</a>' in html
    assert '<a class="de-button de-button--secondary" href="../../events/">Events</a>' in html
    assert "<h2>Listen</h2>" in html
    assert "<p>Out now.</p>" in html


def test_story_checklist_renders_checkbox_items():
    macros = load_macros()
    page = make_page({"checklist": {"title": "Start now", "items": ["One?", "Two?"], "text": "Note."}})

    html = macros["story_checklist"](page)

    assert "<h2>Start now</h2>" in html
    assert '<label><input type="checkbox"> One?</label>' in html
    assert "<p>Note.</p>" in html
