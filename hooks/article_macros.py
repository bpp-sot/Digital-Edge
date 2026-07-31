"""Jinja macros (via mkdocs-macros-plugin) for repeated page chrome.

Each page's YAML frontmatter carries the structured data (hero/summary/
takeaways/discussion/related-reading for articles, name/role/Q&A for staff
spotlights); these macros render it to HTML that would otherwise be
hand-copied into every markdown file of that type. Only pages with
`render_macros: true` in their frontmatter are rendered (see
render_by_default: false in mkdocs.yml), so nothing else on the site is
affected.
"""


def _tag_links(tags: list[str]) -> str:
    return "\n".join(f'      <a href="../?tag={tag}">{tag}</a>' for tag in tags)


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
  <h2>Related Reading</h2>
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
