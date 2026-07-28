"""Jinja macros (via mkdocs-macros-plugin) for the repeated article chrome.

Each article's YAML frontmatter carries the hero/summary/takeaways/discussion/
related-reading data; these macros render it to the same HTML that used to be
hand-copied into every article markdown file. Only pages with
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
