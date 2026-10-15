---
title: "Don't Make AI Your Single Point of Failure"
description: "Shetland's sub-sea cables show how much our digital world depends on a few physical links. Our growing reliance on AI risks building the same weakness into how we think."
author: "Matt Lucas"
author_slug: "matt-lucas"
author_role: "Associate Professor of Technology, BPP University"
date: "2026-10-15"
updated: "2026-10-15"
date_display: "15 October 2026"
read_time: "6 min read"
tags:
  - AI
  - Workflows
type: article
render_macros: true
hero_pill: "Resilience"
hero_quote: "Let AI become a powerful part of your intellectual network, but do not make it the single cable on which everything depends."
summary:
  - "The online world still depends on very physical things. When a sub-sea cable to Shetland fails, a whole community feels it."
  - "Using AI to support your thinking makes you faster. Asking it to do your thinking for you wears down the judgement you need to spot its mistakes."
  - "Resilience means alternative routes: form your own view first, treat AI as a sparring partner, and keep practising important skills without it."
takeaways:
  - label: "Fluency is not accuracy"
    text: "A polished answer in seconds can feel like relief, but a plausible answer is not necessarily a good one."
  - label: "Better AI, less alert humans"
    text: "In one field experiment, recruiters given higher-quality AI were sometimes less accurate, because they had less incentive to scrutinise it."
  - label: "Build alternative routes"
    text: "Know what you would do when the chatbot will not load, or when it confidently tells you something that is wrong."
shetland_facts:
  - value: "A few"
    label: "sub-sea cables carry Shetland's digital connections to the wider world"
  - value: "2022"
    label: "Major incident declared as telephone and internet services go down"
  - value: "2025"
    label: "Cable damage disrupts internet services across Orkney and Shetland"
study_facts:
  - value: "181"
    label: "professional recruiters"
  - value: "Thousands"
    label: "of job applications assessed"
  - value: "Varied"
    label: "levels of algorithmic assistance"
strengths:
  - label: "What AI is exceptionally good at"
    text: "Speed, scale and synthesis. It can generate alternatives, summarise large quantities of material and expose us to perspectives we might not have considered."
  - label: "What humans contribute"
    text: "Context, values, accountability, and an understanding of what actually matters in a particular situation."
habits:
  - title: "Form a view first"
    text: "Know what a convincing answer would need to contain before you ask."
  - title: "Spar, don't consult an oracle"
    text: "Ask it to challenge your assumptions and say what would undermine its conclusion."
  - title: "Make your contribution visible"
    text: "Ask yourself the uncomfortable question: what did I add?"
  - title: "Keep practising without it"
    text: "Prove you can still frame a problem, build an argument or debug code unaided."
contribution_check:
  title: "What did I add? Think of the last thing you used AI for."
  items:
    - "Specialist knowledge the AI did not have"
    - "A hidden assumption I noticed"
    - "An inappropriate recommendation I rejected"
    - "A generic response I reshaped for a real audience"
resilience_quote:
  text: "This is not nostalgia for a pre-digital age; it is cognitive resilience."
outage_facts:
  - value: "Nov 2025"
    label: "A Cloudflare failure makes large parts of the web inaccessible"
  - value: "AWS & Azure"
    label: "Problems disrupt services millions of people and organisations depend on"
  - value: "180+"
    label: "significant internet disruptions recorded in Cloudflare's review of 2025"
outage_causes:
  - "Cable damage"
  - "Power failures"
  - "Bad weather"
  - "Network faults"
  - "Armed conflict"
  - "A faulty configuration file"
discussion:
  - "Think of the last AI answer you accepted. What did you add to it?"
  - "Which skills in your role would you struggle to use if AI were unavailable for a week?"
  - "Where has AI become a single point of failure in your team, and what would the alternative route be?"
related:
  - tag: "AI"
    title: "The Economics of the AI Apocalypse"
    description: "Mo Warsame on how a long run of rational decisions could remove the human checkpoints that keep AI in check."
    href: "../economics-of-the-ai-apocalypse/"
  - tag: "AI"
    title: "Are You an AI Optimist?"
    description: "Matt Lucas on the choices that decide whether AI turns out well."
    href: "../are-you-an-ai-optimist/"
---

# Don't Make AI Your Single Point of Failure

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

It is fast becoming a distant memory, but in the summer my family and I went on holiday to Shetland.

It is a remarkable place. Beautiful landscapes, a welcoming community and weather that gave a refreshing counterpoint to the heatwave we were experiencing in the South of England. It also feels reassuringly remote. That remoteness is part of Shetland's appeal, but it comes with a degree of technological precariousness.

The islands rely on a small number of sub-sea cables for their digital connections to the wider world. When one of those cables was damaged in 2025, internet services across Orkney and Shetland were disrupted. An even more serious incident in 2022 affected telephone and internet services, prompted the police to declare a major incident and left engineers scrambling to reroute traffic through the remaining links.

{{ story_facts(page, "shetland_facts") }}

It is easy to think of the internet as something almost abstract: information floating weightlessly around us, available everywhere and at any time. Shetland offers a useful corrective. The online world still depends on very physical things: cables, data centres, electricity supplies and people who know how to repair them.

It made me wonder how well most of us would cope if our technology suddenly became unavailable. More specifically, it made me think about our rapidly growing reliance on AI.

Engineers try to avoid building systems with a single point of failure: one component whose loss brings everything else to a halt. Yet that is exactly what we risk creating when AI becomes not simply a useful tool, but the place where we outsource our ideas, decisions and judgement.

<figure class="de-spof" data-spof data-cut="false">
  <div class="de-spof__panels">
    <div class="de-spof__panel de-spof__panel--single">
      <span class="de-card__label">Single point of failure</span>
      <h3>Everything through one cable</h3>
      <svg viewBox="0 0 320 200" role="img" aria-label="You connect to AI through one link, and your ideas, decisions and judgement all depend on AI.">
        <line class="de-spof__link de-spof__link--ai" x1="46" y1="100" x2="166" y2="100"/>
        <line class="de-spof__link de-spof__down" x1="166" y1="100" x2="268" y2="36"/>
        <line class="de-spof__link de-spof__down" x1="166" y1="100" x2="268" y2="100"/>
        <line class="de-spof__link de-spof__down" x1="166" y1="100" x2="268" y2="164"/>
        <g class="de-spof__break" transform="translate(109 100)" aria-hidden="true"><circle r="10"/><path d="M-4 -4 L4 4 M4 -4 L-4 4"/></g>
        <g class="de-spof__node de-spof__node--you" transform="translate(46 100)"><rect x="-42" y="-17" width="84" height="34" rx="17"/><text dy="0.35em">You</text></g>
        <g class="de-spof__node de-spof__node--ai" transform="translate(166 100)"><rect x="-36" y="-17" width="72" height="34" rx="17"/><text dy="0.35em">AI</text></g>
        <g class="de-spof__node de-spof__down" transform="translate(268 36)"><rect x="-48" y="-17" width="96" height="34" rx="17"/><text dy="0.35em">Ideas</text></g>
        <g class="de-spof__node de-spof__down" transform="translate(268 100)"><rect x="-48" y="-17" width="96" height="34" rx="17"/><text dy="0.35em">Decisions</text></g>
        <g class="de-spof__node de-spof__down" transform="translate(268 164)"><rect x="-48" y="-17" width="96" height="34" rx="17"/><text dy="0.35em">Judgement</text></g>
      </svg>
      <p class="de-spof__status"><span class="de-spof__state--ok">Fast and convenient, while the cable holds.</span><span class="de-spof__state--cut">Outage. Ideas, decisions and judgement all ran through one link.</span></p>
    </div>
    <div class="de-spof__panel de-spof__panel--network">
      <span class="de-card__label">Resilient network</span>
      <h3>AI as one route among several</h3>
      <svg viewBox="0 0 320 200" role="img" aria-label="You connect to AI, sources, colleagues and your own skills, which are also linked to each other.">
        <line class="de-spof__link de-spof__link--ai" x1="160" y1="100" x2="64" y2="34"/>
        <line class="de-spof__link de-spof__link--ai" x1="64" y1="34" x2="256" y2="34"/>
        <line class="de-spof__link de-spof__link--ai" x1="64" y1="34" x2="64" y2="166"/>
        <line class="de-spof__link" x1="160" y1="100" x2="256" y2="34"/>
        <line class="de-spof__link" x1="160" y1="100" x2="64" y2="166"/>
        <line class="de-spof__link" x1="160" y1="100" x2="256" y2="166"/>
        <line class="de-spof__link" x1="256" y1="34" x2="256" y2="166"/>
        <line class="de-spof__link" x1="64" y1="166" x2="256" y2="166"/>
        <g class="de-spof__break" transform="translate(112 67)" aria-hidden="true"><circle r="10"/><path d="M-4 -4 L4 4 M4 -4 L-4 4"/></g>
        <g class="de-spof__node de-spof__node--you" transform="translate(160 100)"><rect x="-42" y="-17" width="84" height="34" rx="17"/><text dy="0.35em">You</text></g>
        <g class="de-spof__node de-spof__node--ai" transform="translate(64 34)"><rect x="-36" y="-17" width="72" height="34" rx="17"/><text dy="0.35em">AI</text></g>
        <g class="de-spof__node" transform="translate(256 34)"><rect x="-48" y="-17" width="96" height="34" rx="17"/><text dy="0.35em">Sources</text></g>
        <g class="de-spof__node" transform="translate(64 166)"><rect x="-52" y="-17" width="104" height="34" rx="17"/><text dy="0.35em">Colleagues</text></g>
        <g class="de-spof__node" transform="translate(256 166)"><rect x="-52" y="-17" width="104" height="34" rx="17"/><text dy="0.35em">Your skills</text></g>
      </svg>
      <p class="de-spof__status"><span class="de-spof__state--ok">Every point still has another way through.</span><span class="de-spof__state--cut">Still running. Sources, colleagues and your own skills carry the load.</span></p>
    </div>
  </div>
  <div class="de-spof__controls">
    <figcaption>Try it: cut the AI cable and see which way of working keeps going.</figcaption>
    <button type="button" class="de-spof__toggle" data-spof-toggle aria-pressed="false" hidden>Cut the AI cable</button>
  </div>
  <p class="de-spof__live" data-spof-status aria-live="polite"></p>
</figure>

## A brilliant tool (and a tempting substitute)

I should say immediately that I am an AI enthusiast. I teach AI, research it and use it regularly. Generative AI can be a wonderful productivity tool. I use it to help structure ideas, test explanations, identify gaps in an argument and escape the tyranny of the blank page. Used well, it can make us faster, more creative and sometimes more ambitious.

There is, however, an important difference between using AI to support your thinking and asking it to do your thinking for you.

<div class="de-before-after">
  <article>
    <span>Using AI to</span>
    <h3>Support your thinking</h3>
    <p>You stay in charge of the ideas and the judgement. AI makes you faster.</p>
  </article>
  <article>
    <span>Asking AI to</span>
    <h3>Do your thinking for you</h3>
    <p>The answer arrives in seconds, and your judgement gets less practice.</p>
  </article>
</div>

That boundary is surprisingly easy to cross. AI systems produce fluent, confident answers in seconds. After wrestling with a problem for an hour, receiving a polished response can feel like relief. The temptation is to accept it, tidy up a few sentences and move on.

But fluency is not the same as accuracy, and a plausible answer is not necessarily a good one. More importantly, every time we accept an answer without really engaging with it, we give up an opportunity to practise the judgement that allows us to recognise a good answer in the first place.

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">Be honest: after an hour wrestling with a problem, an AI tool hands you a polished answer. What do you usually do?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="You are not alone: that is exactly the temptation. But every answer accepted without real engagement is a missed chance to practise the judgement that lets you recognise a good answer.">Accept it, tidy it up and move on</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That is the habit worth protecting. Fluency is not the same as accuracy, and your own view is what lets you tell the difference.">Test it against my own view first</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

### Falling asleep at the wheel

Fabrizio Dell'Acqua captured this risk nicely in a study called *Falling Asleep at the Wheel*. In a field experiment, 181 professional recruiters assessed thousands of job applications with different levels of algorithmic assistance.

{{ story_facts(page, "study_facts") }}

Counter-intuitively, recruiters given higher-quality AI were sometimes less accurate than those given lower-quality assistance.

Why? The people working with the less reliable system stayed alert. They spent longer examining the evidence and were less likely to follow its recommendation automatically. Those given apparently excellent AI had less incentive to scrutinise its advice. When the system did make a mistake, they were less prepared to catch it.

The lesson is not that worse AI is inherently better. It is that the performance of an AI system in isolation is not the same as the performance of a human and an AI working together. A highly capable tool can still produce a poor combined result if it encourages its user to disengage.

## The human must remain part of the system

This is one of the most important ideas I want students on my AI programmes to understand. Effective AI use is not simply a matter of learning how to write clever prompts. It means combining the strengths of the technology with the forms of judgement that remain distinctly human.

{{ story_callouts(page, "strengths") }}

The aim, then, is neither to reject AI nor to defer to it. It is to create a productive tension between its output and our judgement.

{{ story_cards(page, "habits", numbered=True) }}

That begins before we type a prompt. If possible, form an initial view of the problem yourself. What are you trying to achieve? What do you already know? What would a convincing answer need to contain? Even a rough position gives you something against which to evaluate the AI's response. Without one, the first coherent answer you see can easily become your answer.

Next, treat the system as a sparring partner rather than an oracle. Ask it to challenge your assumptions, provide counterarguments or explain what evidence would undermine its conclusion. If you are writing code, ask why the proposed solution works and where it might fail. If you are researching a topic, follow the sources rather than trusting the summary. If the consequences of an error are serious, verification is not an optional final polish; it is part of the task.

It also helps to make your own contribution visible. After using AI, ask yourself a slightly uncomfortable question: what did I add? Perhaps you supplied specialist knowledge, noticed a hidden assumption, rejected an inappropriate recommendation or reshaped a generic response for a real audience. If you cannot identify your contribution, you may have delegated more than you intended.

{{ story_checklist(page, "contribution_check") }}

Finally, keep practising important skills without assistance. A calculator is useful, but we still teach arithmetic because number sense helps us notice when the calculator's answer cannot possibly be right. The same principle applies to writing, programming, research and analysis. You do not need to avoid AI every day, but you should occasionally prove to yourself that you can still frame a problem, build an argument or debug some code when it is unavailable.

{{ story_pull_quote(page, "resilience_quote") }}

## Resilience matters

Even if you live nowhere near a remote island, this resilience matters. The digital services we use can appear distributed and almost indestructible, but much of the internet depends on a relatively small number of infrastructure providers.

In November 2025, a Cloudflare failure made large parts of the web inaccessible. Problems at Amazon Web Services and Microsoft Azure also disrupted services on which millions of people and organisations depend. Cloudflare's review of internet disruptions during 2025 recorded more than 180 significant incidents caused by cable damage, power failures, bad weather, network faults and armed conflict.

{{ story_facts(page, "outage_facts") }}

Recent global instability has made the physical nature of our digital world harder to ignore. Infrastructure can fail because of a faulty configuration file, but it can also be damaged by storms, accidents, power cuts or military action. In extreme circumstances, even data stored with major cloud providers may not be recoverable.

{{ story_chips(page, "outage_causes") }}

This is not an argument for abandoning online services or keeping every document in a filing cabinet. It is an argument for avoiding single points of failure: in our infrastructure and in ourselves.

For essential work, that might mean keeping local copies of important information, knowing what systems you depend on and having a workable alternative when they are unavailable. For AI, it means retaining enough knowledge and confidence to continue when the chatbot will not load (or when it confidently tells you something that is wrong).

The goal is not independence from technology. Humans have always extended their abilities through tools, from writing and printing to spreadsheets, search engines and machine learning. The goal is to remain capable within that relationship.

AI can help us explore more ideas, complete routine work faster and tackle problems that might otherwise have been beyond our reach. Those are benefits worth embracing. But the best use of AI should leave us more capable, not merely more dependent.

<section class="de-article-close-panel">
  <div>
    <p class="de-kicker">The next time an answer arrives in seconds</p>
    <h2>Pause before accepting it.</h2>
    <ol>
      <li>Ask what assumptions it has made.</li>
      <li>Check what it may have missed.</li>
      <li>Decide what you think.</li>
    </ol>
  </div>
  <aside>
    <h3>Alternative routes</h3>
    <p>Resilient systems have alternative routes when one connection fails. Our relationship with AI should be designed in the same way.</p>
  </aside>
</section>

Let AI become a powerful part of your intellectual network, but do not make it the single cable on which everything depends.

{{ discussion_box(page) }}

{{ related_reading(page) }}
