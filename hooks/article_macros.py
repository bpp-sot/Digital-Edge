"""Jinja macros (via mkdocs-macros-plugin) for repeated page chrome.

Each page's YAML frontmatter carries the structured data (hero/summary/
takeaways/discussion/related-reading for articles, name/role/Q&A for staff
spotlights, hero/facts/quotes/sessions for community news stories); these
macros render it to HTML that would otherwise be hand-copied into every
markdown file of that type. Only pages with `render_macros: true` in their
frontmatter are rendered (see render_by_default: false in mkdocs.yml), so
nothing else on the site is affected.

The story_* macros are building blocks rather than a fixed page layout: each
community news page picks the ones that suit its content and places them
between its own markdown prose. Most take a `key` argument naming the
frontmatter list to render, so a page can use the same block twice.
"""

import re
from datetime import date
from pathlib import Path

import yaml

FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(?P<body>.*?)\n---\s*\n", re.DOTALL)

# Colour accent for each Community News card, keyed by the story's
# `news_label`. Unknown labels fall back to teal.
NEWS_ACCENTS = {
    "Event": "teal",
    "BCS Awards": "gold",
    "Apprentice Spotlight": "purple",
    "Programme News": "blue",
    "Podcast": "coral",
    "Announcement": "blue",
}

# Within a month, award stories list winners first, then highly commended,
# then finalists; everything else sorts after them.
AWARD_TIER_ORDER = {"Winner": 3, "Highly Commended": 2, "Finalist": 1}


def _tag_links(tags: list[str]) -> str:
    return "\n".join(f'      <a href="../?tag={tag}">{tag}</a>' for tag in tags)


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def _paragraphs(text) -> str:
    return "".join(f"<p>{paragraph.strip()}</p>" for paragraph in str(text).strip().split("\n\n"))


def _link(label: str, href: str | None) -> str:
    if not href:
        return label
    external = ' target="_blank" rel="noopener noreferrer"' if href.startswith("http") else ""
    return f'<a href="{href}"{external}>{label}</a>'


def _initials(name: str) -> str:
    words = name.split()
    if not words:
        return ""
    return (words[0][0] + (words[-1][0] if len(words) > 1 else "")).upper()


def _person_chip(person) -> str:
    if isinstance(person, str):
        person = {"name": person}
    role = f' <small>{person["role"]}</small>' if person.get("role") else ""
    label = f'{person["name"]}{role}'
    return _link(label, person["href"]) if person.get("href") else f"<span>{label}</span>"


def news_stories(docs_dir, section: str = "community-news") -> list[dict]:
    """Community News stories, newest first, read from each page's frontmatter.

    A page counts as a story when its frontmatter has both `date` and
    `news_label`, so the index and the staff spotlights are skipped. Read
    straight off disk (like search_filter.latest_article) so the index page
    doesn't depend on the order mkdocs processes pages in.
    """
    stories = []
    for path in sorted((Path(docs_dir) / section).glob("*.md")):
        match = FRONTMATTER_PATTERN.match(path.read_text(encoding="utf-8"))
        meta = yaml.safe_load(match.group("body")) if match else None
        if not isinstance(meta, dict) or not meta.get("date") or not meta.get("news_label"):
            continue

        published = meta["date"]
        if isinstance(published, str):
            published = date.fromisoformat(published)
        stories.append({**meta, "slug": path.stem, "date": published})

    def sort_key(story):
        tier = (story.get("hero_award") or {}).get("tier")
        return story["date"], AWARD_TIER_ORDER.get(tier, 0)

    return sorted(stories, key=sort_key, reverse=True)


def news_card(story: dict) -> str:
    accent = NEWS_ACCENTS.get(story["news_label"], "teal")
    tier = (story.get("hero_award") or {}).get("tier")
    tier_html = f'\n    <span class="de-news-card__tier de-news-card__tier--{_slug(tier)}">{tier}</span>' if tier else ""

    return f"""  <a class="de-card de-news-card de-news-card--{accent}" href="{story["slug"]}/">
    <span class="de-news-card__meta"><span class="de-card__label">{story["news_label"]}</span><time datetime="{story["date"].isoformat()}">{story["date"].strftime("%B %Y")}</time></span>
    <h3>{story.get("card_title") or story["title"]}</h3>
    <p>{story.get("description", "")}</p>{tier_html}
  </a>"""


def _story_hero_aside(meta: dict) -> str:
    award = meta.get("hero_award")
    if award:
        return f"""  <aside class="de-story-medal de-story-medal--{_slug(award["tier"])}">
    <div class="de-story-medal__disc">
      <span>{award.get("year", "")}</span>
      <strong>{award["tier"]}</strong>
    </div>
    <p class="de-story-medal__event">{award.get("event", "BCS IT &amp; Digital Apprenticeship Awards")}</p>
    <p class="de-story-medal__category">{award.get("category", "")}</p>
  </aside>"""

    if meta.get("image"):
        return f"""  <aside class="de-story-hero__media de-story-hero__media--{meta.get("image_fit", "cover")}">
    <img src="{meta["image"]}" alt="{meta.get("image_alt", "")}">
  </aside>"""

    stat = meta.get("hero_stat")
    if stat:
        return f"""  <aside class="de-story-hero__stat">
    <strong>{stat["value"]}</strong>
    <p>{stat["label"]}</p>
  </aside>"""

    if meta.get("hero_quote"):
        return f"""  <aside>
    <span class="de-pill">{meta.get("hero_pill", "In their words")}</span>
    <p>{meta["hero_quote"]}</p>
  </aside>"""

    return ""


def define_env(env) -> None:
    @env.macro
    def article_hero(page) -> str:
        meta = page.meta
        role = meta.get("author_role", "")
        role_html = f"\n      <span>{role}</span>" if role else ""

        return f"""<section class="de-article-hero">
  <div>
    <div class="de-article-tags de-article-tags--hero" aria-label="Article tags">
{_tag_links(meta.get("tags", []))}
    </div>
    <h1>{meta.get("title", "")}</h1>
    <p>{meta.get("lede") or meta.get("description", "")}</p>
    <div class="de-article-meta">
      <a href="../../people/{meta.get("author_slug", "")}/">{meta.get("author", "")}</a>{role_html}
      <span>{meta.get("date_display", "")}</span>
      <span>{meta.get("read_time", "")}</span>
    </div>
  </div>
  <aside>
    <span class="de-pill">{meta.get("hero_pill", "")}</span>
    <p>{meta.get("hero_quote", "")}</p>
  </aside>
</section>"""

    @env.macro
    def article_summary(page) -> str:
        items = page.meta.get("summary", [])
        list_items = "\n".join(f"    <li>{item}</li>" for item in items)

        return f"""<section class="de-article-summary">
  <h2>Article Summary</h2>
  <ul>
{list_items}
  </ul>
</section>"""

    @env.macro
    def article_takeaways(page) -> str:
        items = page.meta.get("takeaways", [])
        cards = "\n".join(
            f"""  <article>
    <strong>{item["label"]}</strong>
    <p>{item["text"]}</p>
  </article>"""
            for item in items
        )

        return f"""<section class="de-article-takeaways">
{cards}
</section>"""

    @env.macro
    def discussion_box(page) -> str:
        items = page.meta.get("discussion", [])
        list_items = "\n".join(f"    <li>{item}</li>" for item in items)

        return f"""<section class="de-discussion-box">
  <h2>Use This In A Discussion</h2>
  <ul>
{list_items}
  </ul>
</section>"""

    @env.macro
    def related_reading(page) -> str:
        items = page.meta.get("related", [])
        cards = "\n".join(
            f"""    <a class="de-card" href="{item["href"]}">
      <span class="de-card__label">{item["tag"]}</span>
      <h3>{item["title"]}</h3>
      <p>{item["description"]}</p>
    </a>"""
            for item in items
        )

        return f"""<section class="de-related-reading">
  <h2>{page.meta.get("related_heading", "Related Reading")}</h2>
  <div class="de-card-grid">
{cards}
  </div>
</section>"""

    @env.macro
    def spotlight_hero(page) -> str:
        meta = page.meta
        return f"""<section class="de-news-hero">
  <div>
    <p class="de-kicker">{meta.get("kicker", "Off The Job: Staff Spotlight")}</p>
    <h1>{meta.get("name", "")}</h1>
    <p>{meta.get("role", "")}</p>
  </div>
  <aside>
    <span class="de-pill">In their own words</span>
    <p>{meta.get("hero_quote", "")}</p>
  </aside>
</section>"""

    @env.macro
    def spotlight_quickfire(page) -> str:
        items = page.meta.get("quickfire", [])
        tiles = "\n".join(
            f"""    <div class="de-spotlight-quickfire__item">
      <span>{item["question"]}</span>
      <p>{item["answer"]}</p>
    </div>"""
            for item in items
        )

        return f"""<section class="de-spotlight-quickfire" aria-label="Quick fire round">
  <h2>Quick Fire Round</h2>
  <div class="de-spotlight-quickfire__grid">
{tiles}
  </div>
</section>"""

    @env.macro
    def spotlight_interview(page) -> str:
        items = page.meta.get("interview", [])
        entries = "\n".join(
            f"""  <div class="de-spotlight-interview__item">
    <h3>{item["question"]}</h3>
    {"".join(f"<p>{paragraph.strip()}</p>" for paragraph in item["answer"].strip().split("\n\n"))}
  </div>"""
            for item in items
        )

        return f"""<section class="de-spotlight-interview">
  <h2>The Interview</h2>
{entries}
</section>"""

    @env.macro
    def news_listing(year) -> str:
        stories = [story for story in news_stories(env.conf["docs_dir"]) if story["date"].year == int(year)]
        if not stories:
            return '<p class="de-news-empty">No stories yet.</p>'
        cards = "\n".join(news_card(story) for story in stories)

        return f"""<div class="de-card-grid de-news-listing">
{cards}
</div>"""

    @env.macro
    def story_hero(page) -> str:
        meta = page.meta
        aside = _story_hero_aside(meta)
        single = "" if aside else " de-news-hero--single"
        author = meta.get("author")
        byline = None
        if author:
            author_href = f'../../people/{meta["author_slug"]}/' if meta.get("author_slug") else None
            byline = f"By {_link(author, author_href)}"
        details = "".join(
            f"<span>{item}</span>" for item in (meta.get("news_label"), meta.get("date_display"), byline) if item
        )

        return f"""<section class="de-news-hero de-story-hero{single}">
  <div>
    <p class="de-kicker">{meta.get("kicker", "")}</p>
    <h1>{meta.get("heading") or meta.get("title", "")}</h1>
    <p>{meta.get("lede") or meta.get("description", "")}</p>
    <div class="de-story-meta">{details}</div>
  </div>
{aside}
</section>"""

    @env.macro
    def story_facts(page, key: str = "facts") -> str:
        tiles = "\n".join(
            f"""  <div>
    <strong>{item["value"]}</strong>
    <span>{item["label"]}</span>
  </div>"""
            for item in page.meta.get(key, [])
        )

        return f"""<section class="de-story-facts" aria-label="Key facts">
{tiles}
</section>"""

    @env.macro
    def story_pull_quote(page, key: str = "pull_quote") -> str:
        quote = page.meta.get(key) or {}
        cite = f"\n  <figcaption>{quote['cite']}</figcaption>" if quote.get("cite") else ""

        return f"""<figure class="de-story-quote">
  <blockquote>{_paragraphs(quote.get("text", ""))}</blockquote>{cite}
</figure>"""

    @env.macro
    def story_quotes(page, key: str = "quotes") -> str:
        figures = "\n".join(
            f"""  <figure>
    <blockquote>{_paragraphs(item["text"])}</blockquote>
    <figcaption><strong>{item.get("cite", "")}</strong>{f"<span>{item['role']}</span>" if item.get("role") else ""}</figcaption>
  </figure>"""
            for item in page.meta.get(key, [])
        )

        return f"""<section class="de-story-quotes">
{figures}
</section>"""

    @env.macro
    def story_cards(page, key: str, numbered: bool = False) -> str:
        modifier = " de-story-cards--numbered" if numbered else ""
        cards = []
        for item in page.meta.get(key, []):
            label = f'\n    <span class="de-card__label">{item["label"]}</span>' if item.get("label") else ""
            text = f'\n    {_paragraphs(item["text"])}' if item.get("text") else ""
            cards.append(f"""  <article>{label}
    <h3>{item["title"]}</h3>{text}
  </article>""")
        cards_html = "\n".join(cards)

        return f"""<div class="de-story-cards{modifier}">
{cards_html}
</div>"""

    @env.macro
    def story_people(page, key: str = "people") -> str:
        people = "\n".join(
            f"""  <li>
    <span class="de-story-people__avatar" aria-hidden="true">{_initials(person["name"])}</span>
    <span><strong>{_link(person["name"], person.get("href"))}</strong>{f"<small>{person['role']}</small>" if person.get("role") else ""}</span>
  </li>"""
            for person in page.meta.get(key, [])
        )

        return f"""<ul class="de-story-people">
{people}
</ul>"""

    @env.macro
    def story_sessions(page, key: str = "sessions", layout: str = "timeline") -> str:
        items = []
        for session in page.meta.get(key, []):
            slot = f'\n    <span class="de-story-sessions__slot">{session["slot"]}</span>' if session.get("slot") else ""
            text = f'\n      {_paragraphs(session["text"])}' if session.get("text") else ""
            people = session.get("people", [])
            chips = (
                '\n      <div class="de-story-chips">' + "".join(_person_chip(person) for person in people) + "</div>"
                if people
                else ""
            )
            items.append(f"""  <li>{slot}
    <div>
      <span class="de-card__label">{session["format"]}</span>
      <h3>{session["title"]}</h3>{text}{chips}
    </div>
  </li>""")
        items_html = "\n".join(items)

        return f"""<ol class="de-story-sessions de-story-sessions--{layout}">
{items_html}
</ol>"""

    @env.macro
    def story_callouts(page, key: str = "callouts") -> str:
        cards = "\n".join(
            f"""  <article>
    <span>{item["label"]}</span>
    {_paragraphs(item["text"])}
  </article>"""
            for item in page.meta.get(key, [])
        )

        return f"""<section class="de-story-callouts">
{cards}
</section>"""

    @env.macro
    def story_steps(page, key: str = "steps") -> str:
        steps = "\n".join(
            f"""  <li>
    <strong>{step["title"]}</strong>
    <span>{step["text"]}</span>
  </li>"""
            for step in page.meta.get(key, [])
        )

        return f"""<ol class="de-story-steps">
{steps}
</ol>"""

    @env.macro
    def story_badges(page, key: str = "badges") -> str:
        badge_cards = []
        for badge in page.meta.get(key, []):
            skills = "\n".join(f"      <li>{skill}</li>" for skill in badge.get("skills", []))
            badge_cards.append(f"""  <article>
    <img src="{badge["image"]}" alt="{badge["name"]} digital badge" loading="lazy">
    <h3>{badge["name"]}</h3>
    <p>{badge["text"]}</p>
    <ul aria-label="Skills recognised by the {badge["name"]} badge">
{skills}
    </ul>
  </article>""")
        cards = "\n".join(badge_cards)

        return f"""<div class="de-story-badges">
{cards}
</div>"""

    @env.macro
    def award_board(page) -> str:
        meta = page.meta
        tiers = []
        for tier in meta.get("board", []):
            entries = "\n".join(
                f"""      <li>
        <strong>{_link(entry["name"], entry.get("href"))}</strong>
        <span>{entry["category"]}</span>
        <em>{entry["provider"]}</em>
      </li>"""
                for entry in tier.get("entries", [])
            )
            tiers.append(f"""  <div class="de-award-board__tier de-award-board__tier--{_slug(tier["tier"])}">
    <h3>{tier.get("heading", tier["tier"])}</h3>
    <ul>
{entries}
    </ul>
  </div>""")

        groups = []
        for group in meta.get("finalists", []):
            names = "\n".join(
                f"      <li>{_link(person['name'], person.get('href'))}</li>" for person in group.get("people", [])
            )
            groups.append(f"""  <article>
    <h3>{group["provider"]}</h3>
    <ul>
{names}
    </ul>
  </article>""")

        tiers_html = "\n".join(tiers)
        groups_html = "\n".join(groups)

        return f"""<section class="de-award-board" aria-label="Winners and highly commended">
{tiers_html}
</section>
<section class="de-award-finalists" aria-label="Other finalists">
{groups_html}
</section>"""

    @env.macro
    def story_cta(page, key: str = "cta") -> str:
        cta = page.meta.get(key) or {}
        button_list = []
        for index, link in enumerate(cta.get("links", [])):
            style = link.get("style", "primary" if index == 0 else "secondary")
            external = ' target="_blank" rel="noopener noreferrer"' if link["href"].startswith("http") else ""
            button_list.append(f'    <a class="de-button de-button--{style}" href="{link["href"]}"{external}>{link["label"]}</a>')
        buttons = "\n".join(button_list)
        kicker = f'\n    <p class="de-kicker">{cta["kicker"]}</p>' if cta.get("kicker") else ""

        return f"""<section class="de-story-cta">
  <div>{kicker}
    <h2>{cta.get("title", "")}</h2>
    {_paragraphs(cta.get("text", ""))}
  </div>
  <div class="de-actions">
{buttons}
  </div>
</section>"""

    @env.macro
    def story_checklist(page, key: str = "checklist") -> str:
        checklist = page.meta.get(key) or {}
        items = "\n".join(f"  <label><input type=\"checkbox\"> {item}</label>" for item in checklist.get("items", []))
        note = f"\n  <p>{checklist['text']}</p>" if checklist.get("text") else ""

        return f"""<div class="de-check-card">
  <h2>{checklist.get("title", "")}</h2>
{items}{note}
</div>"""

    @env.macro
    def story_chips(page, key: str) -> str:
        chips = "\n".join(f"  <span>{chip}</span>" for chip in page.meta.get(key, []))

        return f"""<div class="de-chip-list">
{chips}
</div>"""
