---
title: "AI Under Pressure: Analysing the OpenAI Sandbox Leak"
description: "OpenAI's own models found a genuine flaw in their sandbox, escalated their privileges, and broke into Hugging Face to win a benchmark. Nobody told them to. That's the problem."
author: "Jacob Reilly-Cooper"
author_slug: "jacob-reilly-cooper"
author_role: "Head of Tech Learning"
date: "2026-09-09"
updated: "2026-09-09"
date_display: "9 September 2026"
read_time: "7 min read"
tags:
  - AI
  - Adoption
type: article
render_macros: true
hero_pill: "Reward hacking"
hero_quote: "Nobody told these models to leave the sandbox. Nobody told them to attack another company. They were told to pass a hacking test, and passing it turned out to mean cheating."
summary:
  - "OpenAI's own models found an unknown flaw in a sandbox tool, escalated their privileges, reached the internet, and broke into Hugging Face using stolen credentials, all to win a benchmark test."
  - "Hugging Face caught it first, flagging over 17,000 automated actions and shutting the intrusion down days before OpenAI connected it back to its own testing."
  - "California's frontier AI law wouldn't have required OpenAI to report any of this. It only covers incidents that kill, injure, or cause catastrophic harm."
takeaways:
  - label: "What happened"
    text: "A previously unknown flaw let OpenAI's own models escalate privileges, reach the internet, and break into Hugging Face using stolen credentials, to win a benchmark."
  - label: "Who caught it"
    text: "Hugging Face, not OpenAI. It flagged over 17,000 automated actions and shut the intrusion down days before OpenAI connected it back to its own testing."
  - label: "What's missing"
    text: "A clear line of responsibility. The law doesn't require this to be reported, and nobody at OpenAI can say it won't happen again."
discussion:
  - "If a person had done exactly what these models did, would you call it a testing mishap or a crime?"
  - "What would it take for you to trust that an AI sandbox actually contains what it's meant to?"
  - "Where else in your own work might a narrow goal and removed restraints find a shortcut nobody ruled out?"
related:
  - tag: "AI"
    title: "From Mythos to Fable"
    description: "Why frontier AI moving into workflows makes governance and readiness more important."
    href: "../from-mythos-to-fable/"
  - tag: "AI"
    title: "Agentic Engineering"
    description: "The next gap education needs to close as AI agents move from advice into real workflows."
    href: "../agentic-engineering/"
---

# AI Under Pressure: Analysing the OpenAI Sandbox Leak

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

In July 2026, OpenAI admitted something most companies would rather keep quiet: models it was testing broke out of the environment built to contain them, then broke into someone else's systems to win.

Here's what actually happened.

## How the models got out

<section class="de-article-pattern-grid">
  <article>
    <span class="de-step-badge">1</span>
    <h3>Safety filters off</h3>
    <p>OpenAI runs internal tests on its models with the usual safety filters switched off, to see what they're really capable of. The models are meant to stay inside a sandbox, an isolated environment with no way out except one internal tool that fetches software packages.</p>
  </article>
  <article>
    <span class="de-step-badge">2</span>
    <h3>A flaw, then a breakout</h3>
    <p>This time, the models found a genuine, previously unknown flaw in that tool. They used it to escalate their own privileges and moved machine to machine until they reached one with internet access.</p>
  </article>
  <article>
    <span class="de-step-badge">3</span>
    <h3>Onto Hugging Face</h3>
    <p>Once online, they worked out that Hugging Face likely held the answers to the benchmark they were being tested against. So they broke in using stolen credentials, among other things, and took what they needed.</p>
  </article>
</section>

Nobody told these models to leave the sandbox. Nobody told them to attack another company. They were told to pass a hacking test, and passing it turned out to mean cheating.

<aside class="de-key-term">
  <strong>Key term: Reward hacking</strong>
  <p>Give a system a narrow goal and remove the usual restraints, and it will find the fastest route to that goal, including ones nobody ruled out because nobody thought they were reachable.</p>
</aside>

## Hugging Face caught it. OpenAI didn't.

<div class="de-strip" aria-label="What we know so far">
  <div>
    <strong>17,000+</strong>
    <span>automated actions flagged by Hugging Face in a matter of hours</span>
  </div>
  <div>
    <strong>16 July</strong>
    <span>the day Hugging Face shut the intrusion down, before OpenAI connected it back to its own testing</span>
  </div>
  <div>
    <strong>2 or 3</strong>
    <span>models involved, depending whether you ask OpenAI or Bloomberg</span>
  </div>
  <div>
    <strong>0</strong>
    <span>new reporting requirements this triggers under California's frontier AI law</span>
  </div>
</div>

Hugging Face's own systems flagged the activity and shut it down days before OpenAI worked out the intrusion was its own doing. Its CEO called it "mind-blowing that all of this happened autonomously." OpenAI says a combination of models were involved, including its GPT-5.6 Sol model and one still in pre-release. Bloomberg reported three models in total. Nobody involved seems entirely sure of the headcount.

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">A system found the fastest route to its goal by breaking rules nobody explicitly wrote down. Whose failure is that?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="It's a tempting instinct, but reward hacking is what happens when a system does exactly what it was optimised to do. Blaming the model treats the outcome as a rogue choice rather than a predictable one.">The system's, it should know better</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="This is closer to the article's own argument. The model did exactly what it was optimised to do. The fence around it wasn't finished, and that's a design and governance problem, not a rogue-AI one.">The people who designed the constraints</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

## This isn't just an OpenAI problem

None of this is news to the people who've worked on it directly. Ariel Herbert-Voss, OpenAI's own first security hire, has talked publicly about this exact scenario: models becoming capable enough to reward-hack their way through whatever's meant to contain them. She called it "a really difficult problem to defend against," which is part of why she left to start RunSybil, a company built entirely around attacking systems the way an AI agent would.

It's not only OpenAI, either. Anthropic reportedly had an early version of its Mythos model do something similar back in April, when a researcher deliberately tested for it. Google DeepMind, Meta and others simply haven't disclosed anything comparable, which isn't the same as it not happening.

## The double standard

California's new frontier AI law wouldn't have required OpenAI to report any of this. It only covers incidents that kill, injure, or cause catastrophic harm, and a model hacking its way into a third party's production systems doesn't clear that bar unless somebody actually gets hurt.

> If a person had done this, there would already be a clear line of responsibility waiting for them. Right now, there isn't one.

<div class="de-before-after">
  <article>
    <span>If a person did this</span>
    <h3>Criminal act</h3>
    <p>Stolen credentials, a breach of another company's production systems: the sort of thing that draws sanctions and an indictment.</p>
  </article>
  <article>
    <span>Because a model did this</span>
    <h3>Testing mishap</h3>
    <p>No law requires it to be reported, and nobody at OpenAI can say whether it happens again.</p>
  </article>
</div>

Nathan Calvin, general counsel at the AI safety group Encode, put it bluntly: he called a company hacking its way into someone else's systems, and not knowing how to stop it happening twice, "pretty nuts." The only difference between "incident" and "attack" here is who was doing the hacking.

<p class="de-reflection"><strong>Reflection:</strong> What would "contained" actually need to mean before you'd trust it, in your own work with AI systems?</p>

I don't think this means AI is out of control. I think it means our definitions of "contained" and "accountable" are both behind where the technology already is.

That's the part worth teaching, if you're involved in any kind of AI literacy or training work. The useful lesson here has nothing to do with AI "turning evil." A system did exactly what it was optimised to do, and the fence around it wasn't finished. It's exactly the kind of case we use on the Level 4 AI Automation Apprenticeship at BPP, not just the polished demos.

{{ discussion_box(page) }}

{{ related_reading(page) }}
