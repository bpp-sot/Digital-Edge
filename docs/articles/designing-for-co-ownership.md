---
title: "Designing for Co-Ownership in the Age of Augmented Learning"
description: "A human can review AI output without ever exercising real judgement. What matters is whether removing them would change the decision."
author: "Mo Warsame"
author_slug: "mo-warsame"
author_role: "Head of AI Learning, Tech Apps &amp; HE"
date: "2026-08-15"
updated: "2026-08-15"
date_display: "15 August 2026"
read_time: "10 min read"
tags:
  - AI
  - Adoption
type: article
render_macros: true
hero_pill: "Key distinction"
hero_quote: "We risk reducing ourselves to carrier pigeons, ferrying messages from one AI system to another."
summary:
  - "Human presence and human agency are not the same thing. The question isn't whether a person remains in the loop, but whether they're still responsible for the parts that matter."
  - "How AI is designed to interact, asking questions versus rewriting, shapes how much ownership and judgement a learner or educator retains, not just how much it helps."
  - "As AI narrows the gap between weak and strong output, education needs evidence of the thinking behind the work, intellectual receipts, not just better finished products."
takeaways:
  - label: "Presence isn't agency"
    text: "A human can review AI output without ever exercising real judgement. What matters is whether removing them would change the decision."
  - label: "Interaction design matters"
    text: "AI that asks questions preserves ownership and diversity of thought. AI that rewrites improves the output but erodes both."
  - label: "We need receipts"
    text: "As AI narrows the gap between weak and strong output, education needs evidence of the thinking behind the work, not just the work itself."
discussion:
  - "Where in your own use of AI would removing the human genuinely change the outcome, and where would it just remove a rubber stamp?"
  - "Is asking AI to question your thinking a real substitute for asking a person, or does something get lost either way?"
  - "What would a \"receipt\" for your own thinking actually look like, and would you want to produce one?"
related:
  - tag: "AI"
    title: "Agentic Engineering"
    description: "The next gap education needs to close as AI agents move from advice into real workflows."
    href: "../agentic-engineering/"
  - tag: "Adoption"
    title: "From Mythos to Fable"
    description: "Why frontier AI moving into workflows makes governance and readiness more important."
    href: "../from-mythos-to-fable/"
---

# Designing for Co-Ownership in the Age of Augmented Learning

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

There is something deeply absurd about where AI could take education if we are not careful. And some of it is already visible: a learner asks AI to help draft an assignment. Their tutor, faced with dozens of submissions and an unforgiving deadline, uses yet another tool to help generate the feedback. The learner in turn feeds it right back into AI to improve the next draft. Everyone remains technically engaged, yet one is left wondering: who, exactly, is doing the thinking? At its logical extreme, we risk reducing ourselves to carrier pigeons, ferrying messages from one AI system to another.

The obvious response is to be adamant that humans remain "in the loop". But what exactly does that mean? Do proofreading and fact-checking AI-generated output count? Does approving it count? If an educator changes two sentences before sending AI-generated feedback to a learner, has human judgement genuinely shaped the outcome? Human presence and human agency are not the same thing.

The more important design question is not how much work AI performs, but whether the human remains responsible for the parts that matter.

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">Does more human involvement in an AI workflow always mean more human judgement?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That's the assumption most 'human-in-the-loop' policies rely on, but it doesn't hold up: an educator who just checks an AI evaluation for obvious errors is present without being consequential.">Yes, presence is what matters</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="Closer to the argument below. Two people can both be 'human-in-the-loop' and have completely different cognitive roles, depending on whether they're forming judgement or just checking a box.">No, it depends what they're asked to do</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

## A human in the loop may not be enough

Before placing human judgement on too high a pedestal, we should acknowledge that people are hardly paragons of consistency. One small study asked three experienced teachers to grade the same ten texts twice, two months apart. They awarded different marks in 73 per cent of cases (Weber and Hubbertz, 2025). The sample is too small to establish AI as a superior marker, but it does challenge the assumption that an outcome becomes trustworthy merely because a human produced it.

So perhaps the wrong question is whether a person remains somewhere inside the workflow. What matters is whether they are consequential or not. If removed, would the reasoning, judgement or final decision change?

Consider two educators, both "human-in-the-loop", with very different cognitive roles:

<section class="de-callout-grid">
  <article>
    <h3>Judgement-first</h3>
    <p>Reads the learner's work, forms an independent judgement, then uses AI to help phrase the feedback.</p>
  </article>
  <article>
    <h3>Check-first</h3>
    <p>Receives a completed AI evaluation and checks it for obvious errors before it goes out.</p>
  </article>
</section>

Jisc's work on AI-assisted marking points to the same problem: the workflow must still give the human something meaningful to decide (Moule, 2026). Otherwise, the human is still visible in the pipeline, but no longer carrying any real decision-making weight.

## The interaction itself shapes ownership

Maier, Schneider and Feuerriegel (2026) compared different forms of human-AI co-creation. In one condition, an LLM proactively rewrote participants' ideas; in others, it asked questions or made suggestions. The proactive model improved idea quality, yet reduced both diversity and participants' sense of ownership. Reflective interaction improved quality too while preserving considerably more of both.

The model had not changed. The role assigned to it had.

There is a substantial difference between asking a learner, "What evidence would strengthen this argument?" and rewriting it for them. Both might improve the essay. Only one requires the learner to work out what is wrong.

## Friction versus formative effort

This brings us to a distinction I think matters enormously: friction versus formative effort. Both can be laborious, but intellectually they are very different.

<section class="de-callout-grid">
  <article>
    <h3>Friction</h3>
    <p>Formatting, transcription, boilerplate, and repetitive checking. Laborious, but not where the thinking happens.</p>
  </article>
  <article>
    <h3>Formative effort</h3>
    <p>Interpreting evidence, choosing between alternatives, identifying weaknesses, and defending a conclusion. This is the thinking.</p>
  </article>
</section>

I have seen this boundary tested in tools developed by BPP's Generative AI and Digital Learning Team. ConCraftr, for example, removes genuine friction in producing learning materials: arranging layouts, formatting slides and building visual scaffolding. More interesting was where educators drew the line.

In working with the tool, the boundary quickly became apparent. Producing layouts and visual scaffolding could readily be delegated; deciding what the material should actually say could not. A module lead can explain why one worked example belongs in week three while a technically equivalent one does not. That judgement depends on sequencing, learner readiness and lesson purpose. An educator need not spend their expertise aligning boxes on a slide or producing a diagram. They should still decide whether the explanation deserves to be taught.

## Better output can conceal weaker capability

Education has historically treated outputs as proxies for capability. A well-written essay suggests someone can construct an argument; a correctly solved problem suggests understanding. Generative AI weakens that relationship.

Fan and colleagues (2025) found that students using ChatGPT produced stronger essays, but without equivalent gains in knowledge or transfer. Bastani and colleagues (2025) found something even more striking in mathematics. Students with unrestricted GPT access performed much better while AI was available, only to perform worse than the control group once it disappeared. A more constrained AI tutor, designed to provide hints rather than solutions, avoided much of that penalty.

<p class="de-reflection"><strong>Reflection:</strong> If AI disappeared from your own work tomorrow, what would you be worse at than you think you are today?</p>

We may therefore be getting better at improving what learners produce while becoming less certain about what they can actually do. AI does more than reduce workload. It redistributes cognition. If reasoning gradually migrates from the learner into the model, the finished product may never reveal that quiet shift.

## So what should good augmentation look like?

The first principle is relatively simple: AI should support a train of thought rather than terminate it.

One approach within FeedbackHub at BPP is deliberately question-led. Instead of telling learners how to fix their work, it uses Socratic questioning to push the problem back towards them. The model could rewrite the paragraph or identify every weakness. But should it?

Sometimes good educational design means withholding an answer so the learner still has something to work out. This is why I increasingly favour multi-turn conversations over one-shot generation. A one-shot prompt invites substitution: "write this", "improve this", "solve this". A multi-turn exchange reveals how the learner responds, what they reject and when their position changes.

Those intermediate decisions are where agency becomes visible.

## Can the learner challenge the AI?

Someone can interact extensively with AI while still treating it as an authority. That is hardly the form of AI literacy education should cultivate.

One idea being explored for FeedbackHub reverses the relationship. A Critical Evaluator persona would mix useful feedback with planted mistakes, requiring learners to identify where AI was wrong and defend that judgement. Rejecting everything would also be the wrong strategy.

The learner has to discriminate.

Responsible AI use requires someone capable of saying:

<div class="de-chip-list" aria-label="What responsible AI use sounds like">
  <span>This is useful</span>
  <span>This is wrong</span>
  <span>This needs modification</span>
  <span>Here is my reasoning</span>
</div>

A learner who cannot disagree with AI for good reason has not yet learned to use it intelligently.

## Does the human decision actually matter?

MarkAssist produces formative feedback for academic review before anything reaches the learner. Yet improving models create an uncomfortable future problem.

Suppose a tutor agrees with the generated feedback 95 per cent of the time. Then 98 per cent. Eventually, perhaps, almost always. At what point does reviewing become confirming?

A human-shaped box at the end of an AI workflow tells us little. The person must retain both the ability to challenge the system and the authority to change what ultimately happens. Otherwise, they remain technically engaged while becoming cognitively redundant.

## We need receipts for human thinking

If the finished artefact tells us less about who performed the underlying cognition, we need evidence of the process that produced it. Not surveillance of every keystroke, nor vague declarations of AI use, but a useful trail of intellectual receipts.

What did the learner ask first? Which outputs were accepted or rejected? What evidence did they introduce? Where did they challenge the model, and can they explain why? A multi-turn conversation naturally leaves traces of those decisions.

Those traces might include prompt logs, selected extracts, rationale notes or a record of significant interventions. They would not be foolproof. A determined learner could manufacture a convincing trail, which is why receipts should complement rather than replace occasional oral vivas. The point is to make human judgement more visible and harder to bypass.

That changes the role of AI provenance:

<div class="de-before-after">
  <article>
    <span>Old question</span>
    <h3>Did you use AI?</h3>
    <p>A yes/no question that tells us almost nothing about what actually happened.</p>
  </article>
  <article>
    <span>New question</span>
    <h3>What did you contribute, and can you defend it?</h3>
    <p>Asks for the trail of decisions: what was accepted, rejected, challenged, and why.</p>
  </article>
</div>

## AI should multiply intelligence, not replace it

None of this requires us to surrender AI's productivity gains. There is little virtue in forcing people to perform repetitive work that machines can do reliably in seconds. AI can accelerate feedback, remove friction and widen access to expertise.

> The true value of augmentation depends on there still being something human to augment. Once judgement and reasoning have been completely surrendered, productivity may rise while capability quietly falls.

If learners repeatedly outsource the retrieval, synthesis, interpretation, judgement and expression through which expertise develops, those abilities will not simply remain waiting underneath. Cognitive capability, like most capability, develops through use.

Education therefore has to embrace AI without quietly deskilling people out of thinking: designing for conversation rather than command, preserving evidence of human intervention and rewarding the ability to challenge AI output. For our own AI programmes, that means helping learners understand that their value lies not in competing with the machine, but in bringing the human judgement, context, passion and perspective that allows its capabilities to be used intelligently.

Used this way, AI becomes a multiplier of human intelligence. Used as a stand-in for human intelligence, it risks becoming something very different. And if we get that distinction wrong, the carrier pigeon may eventually forget how to read the message it carries.

{{ discussion_box(page) }}

{{ related_reading(page) }}
