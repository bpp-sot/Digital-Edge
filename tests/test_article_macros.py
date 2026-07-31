from types import SimpleNamespace

import article_macros


class FakeEnv:
    """Stands in for mkdocs-macros-plugin's env: @env.macro just registers the function."""

    def __init__(self):
        self.macros = {}

    def macro(self, func):
        self.macros[func.__name__] = func
        return func


def load_macros():
    env = FakeEnv()
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
