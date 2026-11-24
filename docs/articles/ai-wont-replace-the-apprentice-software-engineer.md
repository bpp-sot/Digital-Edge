---
title: "AI Won't Replace the Apprentice Software Engineer. But It Will Redefine Them."
description: "If AI can write and deploy the code, what does it mean to be an apprentice software engineer? Scott Kenyon on why the fundamentals could matter more, not less."
author: "Scott Kenyon"
author_slug: "scott-kenyon"
author_role: "Programme Lead, Software &amp; DevOps"
date: "2026-11-16"
updated: "2026-11-16"
date_display: "16 November 2026"
read_time: "5 min read"
tags:
  - AI
  - Careers
  - Learning
type: article
render_macros: true
hero_pill: "After the prompt"
hero_quote: "AI can give someone an answer incredibly quickly. The real skill is knowing whether it's the right answer."
summary:
  - "AI tools can now generate code, explain errors, create tests and suggest fixes in seconds. Scott Kenyon doesn't think that means we need fewer apprentices, but it does change what we should expect of them."
  - "Writing code has only ever been one part of software engineering. Someone still has to understand what the AI produced, test it, secure it and decide whether it belongs in the wider system."
  - "To evaluate a generated answer you need the fundamentals, which is why AI could make programming, testing and DevOps knowledge more important, not less."
takeaways:
  - label: "Use it, don't depend on it"
    text: "Apprentices should learn to use AI well. The risk is an engineer who can generate answers but can't tell whether they're any good."
  - label: "Understand before you challenge"
    text: "You can't properly evaluate generated code, tests or pipelines without understanding programming, testing and CI/CD."
  - label: "A better question"
    text: "Instead of asking whether AI will replace apprentice roles, ask what an apprentice should be capable of when AI is already in the toolkit."
brilliant_quote:
  text: "We don't want to create software engineers who are brilliant at generating answers but unable to tell whether those answers are any good."
discussion:
  - "What should an apprentice software engineer in your team be able to do now that AI is part of the toolkit?"
  - "How do you check that someone understands AI-generated code before it gets merged?"
  - "Where is the balance between letting learners use AI and making sure they still do the thinking?"
related:
  - tag: "Quality"
    title: "Why the Best Companies Are Investing in Quality Engineers, Not Just All-Out AI"
    description: "Scott Kenyon on what AI misses when it tests software, and why quality still needs quality engineers."
    href: "../why-the-best-companies-invest-in-quality-engineers/"
  - tag: "Security"
    title: "The AI Agent Security Problem Nobody Can Afford to Ignore"
    description: "Ant Lees on why apprentices need secure engineering from the start."
    href: "../ai-agent-security-problem/"
  - tag: "Learning"
    title: "What Happens to Learning When AI Gives Us the Answers?"
    description: "Gemma McKay on showing your working, and the effort we might not want AI to take away."
    href: "../what-happens-to-learning-when-ai-gives-us-the-answers/"
---

# AI Won't Replace the Apprentice Software Engineer. But It Will Redefine Them.

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

There's a question I've been thinking about a lot recently:

<p class="de-article-interjection">If AI can write and deploy the code, what does it mean to be an Apprentice software engineer?</p>

Working as a Programme Lead across Software and DevOps, I spend a lot of time thinking about what we're actually preparing apprentices for and, importantly, what the software industry they are entering is going to look like. AI is now becoming part of that industry. We have tools that can generate code, explain errors, create tests, troubleshoot problems and suggest improvements in seconds.

So, does that mean we need fewer Apprentices? **Personally, I don't think it does.** But I do think we need to reconsider what we mean when we talk about Apprentices in software.

## Being a software engineer isn't just about writing code

When we talk about AI and software development, the conversation very quickly turns to how well AI can write code. For me, that misses a big part of what software engineering actually is. Writing code is important, but software engineering has never just been about producing lines of code.

<figure class="de-ticket-board">
  <p class="de-ticket-board__lead">An Apprentice engineer could be…</p>
  <ul class="de-ticket-board__tickets">
    <li class="is-feature"><span>Feature</span>Developing functionality one day</li>
    <li class="is-defect"><span>Defect</span>Investigating a defect the next</li>
    <li class="is-review"><span>Review</span>Reviewing a pull request</li>
    <li class="is-tests"><span>Tests</span>Writing tests</li>
    <li class="is-build"><span>Build</span>Looking at a failed build</li>
    <li class="is-investigate"><span>Investigate</span>Trying to understand why something isn't behaving as expected</li>
  </ul>
  <div class="de-ticket-board__team">
    <p>They might be working with</p>
    <ul>
      <li>Developers</li>
      <li>Testers</li>
      <li>DevOps engineers</li>
      <li>Product teams</li>
      <li>Other stakeholders</li>
    </ul>
  </div>
  <figcaption>The code is only one part of the job.</figcaption>
</figure>

If I ask an AI tool to create something and it produces 50 lines of code in seconds, someone still needs to understand what they're looking at.

<figure class="de-ai-review">
  <div class="de-ai-review__diff" aria-hidden="true">
    <p class="de-ai-review__head"><span>AI-generated</span><strong>+50 lines</strong><small>in seconds</small></p>
    <ol class="de-ai-review__lines">
      <li><i style="--w: 46%"></i></li>
      <li><i style="--w: 72%"></i></li>
      <li><i style="--w: 64%"></i></li>
      <li><i style="--w: 38%"></i></li>
      <li><i style="--w: 80%"></i></li>
      <li><i style="--w: 58%"></i></li>
      <li><i style="--w: 70%"></i></li>
      <li><i style="--w: 30%"></i></li>
    </ol>
    <p class="de-ai-review__more">42 more lines</p>
  </div>
  <div class="de-ai-review__comments">
    <p class="de-ai-review__label">Review comments</p>
    <p>Does it actually solve the problem?</p>
    <p>Is it secure?</p>
    <p>How would I test it?</p>
    <p>Will somebody else be able to maintain it?</p>
    <p>Will it work within the wider system?</p>
    <p class="is-biggest"><span>And probably the biggest question of all:</span>Do I actually understand what this code is doing?</p>
  </div>
</figure>

For me, that's where the conversation around Apprentice software engineers and AI becomes much more interesting.

## Using AI isn't the problem. Depending on it could be.

I'm not against Apprentice engineers using AI. Quite the opposite. If these tools are going to be part of the environments our apprentices work in, then I believe we should be teaching people how to use them effectively.

<p class="de-article-interjection">But there's a big difference between using AI and depending on AI.</p>

Take a basic DevOps example. An Apprentice engineer asks an AI tool, *"Create a CI/CD pipeline for me."* Within seconds, they could have a configuration in front of them that looks like it will do exactly what they've asked for. Great.

<figure class="de-pipeline" data-pipeline>
  <div class="de-pipeline__top">
    <p class="de-pipeline__file"><strong>pipeline.yml</strong><span>Generated in seconds</span></p>
    <button type="button" class="de-pipeline__run" data-pipeline-run hidden>Run the pipeline</button>
  </div>
  <p class="de-pipeline__question">But what happens when that pipeline fails?</p>
  <ol class="de-pipeline__stages">
    <li data-pipeline-stage>
      <span class="de-pipeline__status" aria-hidden="true"></span>
      <strong>Test</strong>
      <small>What happens when a test doesn't run correctly?</small>
    </li>
    <li data-pipeline-stage>
      <span class="de-pipeline__status" aria-hidden="true"></span>
      <strong>Dependencies</strong>
      <small>What happens when a dependency causes a problem?</small>
    </li>
    <li data-pipeline-stage>
      <span class="de-pipeline__status" aria-hidden="true"></span>
      <strong>Deploy</strong>
      <small>What happens when the generated solution simply isn't suitable for the environment in which it's being deployed?</small>
    </li>
  </ol>
  <div class="de-pipeline__loop">
    <span aria-hidden="true">↻</span>
    <p>Of course, the engineer could go back to AI and ask it to solve the next problem. <strong>But then what happens when that answer is wrong?</strong></p>
  </div>
  <p class="de-pipeline__live" data-pipeline-status aria-live="polite"></p>
</figure>

{{ story_pull_quote(page, "brilliant_quote") }}

That's where I think the fundamentals really start to matter.

## Could AI actually make the fundamentals more important?

It might sound strange, but I think AI could actually make some of the fundamental software engineering skills **more important, not less**.

If AI can generate more of the solution, then one of the most valuable skills an engineer can have is the ability to properly evaluate that solution.

<figure class="de-understand-first">
  <div class="de-understand-first__grid">
    <div>
      <p class="de-understand-first__top">To challenge generated code,</p>
      <p class="de-understand-first__base">you need to understand <strong>programming.</strong></p>
    </div>
    <div>
      <p class="de-understand-first__top">To challenge an AI-generated test,</p>
      <p class="de-understand-first__base">you need to understand <strong>testing.</strong></p>
    </div>
    <div>
      <p class="de-understand-first__top">To investigate a CI/CD problem,</p>
      <p class="de-understand-first__base">you need to understand <strong>the pipeline.</strong></p>
    </div>
    <div>
      <p class="de-understand-first__top">To assess a suggested fix,</p>
      <p class="de-understand-first__base">you need to understand <strong>the original problem.</strong></p>
    </div>
  </div>
  <figcaption>You can't properly evaluate something you don't understand.</figcaption>
</figure>

AI can give someone an answer incredibly quickly. **The real skill is knowing whether it's the right answer.**

That's a very different skill from simply being able to prompt an AI tool, and I think it's something that will become increasingly important for junior engineers entering the industry.

## What does this mean for apprenticeships?

This is probably the part that interests me most as a Programme Lead.

Are we preparing apprentices for the software industry as it was, or are we preparing them for the software industry they're actually entering?

<figure class="de-balance">
  <div class="de-balance__beam">
    <p><span>Not this</span>I don't think we should teach software engineering as though AI doesn't exist. That wouldn't reflect the reality of modern software teams.</p>
    <p><span>Or this</span>But at the same time, I don't think we should allow AI to do all of the thinking for the learner.</p>
  </div>
  <div class="de-balance__pivot" aria-hidden="true"></div>
  <figcaption>We've got to find a balance.</figcaption>
</figure>

<figure class="de-toolkit">
  <div class="de-toolkit__foundations">
    <p class="de-toolkit__lead">Our apprentices still need strong foundations in</p>
    <ul>
      <li>Programming</li>
      <li>Testing</li>
      <li>Debugging</li>
      <li>Version control</li>
      <li>Security</li>
      <li>CI/CD</li>
      <li>DevOps</li>
      <li>Problem solving</li>
      <li>Communication</li>
    </ul>
    <p class="de-toolkit__note">Those skills don't suddenly disappear because an AI tool can produce an answer.</p>
  </div>
  <div class="de-toolkit__new">
    <span>But there's another skill that increasingly sits alongside them:</span>
    <strong>Working effectively with AI</strong>
  </div>
</figure>

And for me, that doesn't simply mean being good at writing prompts. Prompting is useful, but I'm much more interested in what happens **after the prompt**.

<figure class="de-after-prompt">
  <p class="de-after-prompt__start"><span>Prompt</span><i aria-hidden="true"></i><strong>After the prompt</strong></p>
  <p class="de-after-prompt__lead">Can the apprentice…</p>
  <ol>
    <li>understand the response they've received?</li>
    <li>challenge it?</li>
    <li>spot something that might be wrong?</li>
    <li>improve it?</li>
    <li>test it?</li>
    <li class="is-key"><span>Most importantly,</span>explain why they've chosen to use that solution?</li>
  </ol>
  <figcaption>That's where I think the real learning takes place.</figcaption>
</figure>

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">An AI tool hands you 50 lines of code that look right. What do you do next?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That's the slide from using AI into depending on it. Somebody still has to know whether it solves the problem, whether it's secure and whether anyone else can maintain it.">Use it, it looks right</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That's what Scott means by what happens after the prompt: understand it, challenge it, test it, and be able to explain why you chose it.">Make sure I understand it first</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

## Apprentices in the software space aren't disappearing

I think the roles are changing.

<figure class="de-less-more">
  <p class="de-less-more__lead">The junior software engineer of the future might</p>
  <div class="de-less-more__cols">
    <div class="de-less-more__less">
      <span>Less</span>
      <p>write less code completely from scratch.</p>
    </div>
    <div class="de-less-more__more">
      <span>More</span>
      <p>spend more time</p>
      <ul>
        <li>understanding systems</li>
        <li>evaluating generated code</li>
        <li>testing solutions</li>
        <li>debugging problems</li>
        <li>deciding what should actually be implemented</li>
      </ul>
    </div>
  </div>
</figure>

And I don't necessarily see that as a bad thing.

If anything, it gives us an opportunity to put more emphasis on the **engineering** part of software engineering.

That's also why I prefer talking about **junior software engineers rather than simply junior developers**. Software engineering is bigger than writing application code. It brings together development, testing, quality, DevOps, security, operations and the wider software lifecycle. AI is going to affect all of those areas.

## Maybe we're asking the wrong question

There's understandably a lot of discussion at the moment about whether AI will replace Apprentice software roles. I'm not convinced that's the most useful question we can be asking.

<figure class="de-question-swap">
  <p class="de-question-swap__old"><s>"Will AI replace Apprentice software roles?"</s></p>
  <p class="de-question-swap__but">I'd rather ask:</p>
  <p class="de-question-swap__new">"What should an Apprentice software engineer be capable of in a world where AI is already part of their toolkit?"</p>
</figure>

That's the question I think employers, educators and apprenticeship providers need to be thinking about.

<figure class="de-versus-with">
  <p class="de-versus-with__no"><span>I don't see the future as</span><strong>software engineer <s>versus</s> AI.</strong></p>
  <p class="de-versus-with__yes"><span>I see it as</span><strong>software engineers learning how to work effectively <em>with</em> AI,</strong><span>while still having the knowledge, skills and confidence to challenge it when it's wrong.</span></p>
</figure>

<p class="de-article-interjection">And for me, that's a really important distinction.</p>

<section class="de-article-close-panel">
  <div>
    <p class="de-kicker">Redefined, not replaced</p>
    <h2>The Apprentice software engineer isn't disappearing.</h2>
    <p>But what we expect them to know, understand and be able to do is changing.</p>
  </div>
  <aside>
    <h3>As the tools change</h3>
    <p>As the tools change, ultimately the way we prepare the next generation of software engineers needs to change with them. It's enabling the understanding of the end-to-end software cycles that create long term sustainable value.</p>
  </aside>
</section>

{{ discussion_box(page) }}

{{ related_reading(page) }}
