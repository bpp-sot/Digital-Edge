---
title: "The Humbling Power of Being a Beginner (Again)"
description: "Francesca Tagliaferri teaches machine learning and AI. Studying cloud engineering has put her back in the learner's seat, and changed how she sees her students."
author: "Francesca Tagliaferri"
date: "2026-11-18"
updated: "2026-11-18"
date_display: "18 November 2026"
read_time: "5 min read"
tags:
  - Learning
  - Careers
type: article
render_macros: true
hero_pill: "Back in the learner's seat"
hero_quote: "Struggle is not a sign of inadequacy but a sign of growth and courage."
summary:
  - "Francesca teaches machine learning and AI. Now studying for an MSc in Software Engineering, she has found that cloud engineering makes her a beginner again."
  - "Expertise turns out to be brutally domain-specific: being fluent in neural networks doesn't make you fluent in infrastructure design."
  - "Feeling that vulnerability herself has changed how she reads hesitation in her apprentices, and in her own children."
takeaways:
  - label: "Expertise doesn't travel"
    text: "Confidence in one field doesn't automatically carry over to the next."
  - label: "Hesitation isn't disengagement"
    text: "A capable professional who apologises before asking a question may be feeling exposed."
  - label: "Normalise confusion"
    text: "Telling learners it's reasonable not to understand straight away makes it easier for them to stay in that space."
discussion:
  - "When did you last feel like a beginner at work, and what did it teach you?"
  - "How do you make it easier for experienced people to ask basic questions?"
  - "What would you study if you had the chance to step outside your own domain?"
related:
  - tag: "Learning"
    title: "What Happens to Learning When AI Gives Us the Answers?"
    description: "Gemma McKay on the gym, showing your working, and the effort we might not want AI to take away."
    href: "../what-happens-to-learning-when-ai-gives-us-the-answers/"
  - tag: "AI"
    title: "Designing for Co-Ownership in the Age of Augmented Learning"
    description: "Mo Warsame on what real human judgement looks like when AI is part of the work."
    href: "../designing-for-co-ownership/"
  - tag: "Security"
    title: "Why Effective Identity Management Starts with Organisational Understanding"
    description: "An ICT learner on why identity and access management is as much about people as technology."
    href: "../identity-management-starts-with-organisational-understanding/"
---

# The Humbling Power of Being a Beginner (Again)

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

Last week, I spent three hours trying to deploy a simple app to AWS, the kind of task I had confidently assumed would take thirty minutes. I reread the documentation twice, then a third time, slowly enough to feel my confidence thinning with each pass.

<figure class="de-time-overrun">
  <div class="de-time-overrun__row is-expected">
    <span>What I assumed</span>
    <div class="de-time-overrun__track"><strong style="--value: 16.67">30 minutes</strong></div>
  </div>
  <div class="de-time-overrun__row is-actual">
    <span>What it took</span>
    <div class="de-time-overrun__track"><strong style="--value: 100">3 hours <em>6× longer</em></strong></div>
  </div>
  <figcaption>Deploying a simple app to AWS. Each notch is 30 minutes.</figcaption>
</figure>

I teach Machine Learning and AI. I supervise dissertations, design assessments, and I stand at the front of a (virtual) room explaining gradient descent, bias-variance trade-offs, and transformer architectures with confidence.

<p class="de-article-interjection">And yet there I was, staring at a cloud console, feeling distinctly... <small>small.</small></p>

## Cloud engineering is hard

I recently had the brilliant idea of taking advantage of the BPP study scheme and enrolling in our MSc in Software Engineering. After surviving Programming and Application Development, my second module this term is Cloud Engineering. For two hours each week, I sit in a webinar learning about infrastructure as code, deployment pipelines, identity and access management, and distributed systems thinking.

It is hard.

<div class="de-kinds-of-hard">
  <p><strong>Not mathematically hard</strong> in the way machine learning can be.</p>
  <p><strong>Not abstract</strong> in the way theoretical AI can be.</p>
  <p class="is-this-one"><strong>But operationally effing hard.</strong></p>
</div>

Everything is connected to everything else. A small misconfiguration ripples across services. Permissions fail silently. Networking rules block traffic in ways that are technically correct but practically maddening. In fact, it feels even harder than that, hard enough that I asked ChatGPT to help me write the above examples, because I am still at the stage where I don't know what I don't know.

In machine learning, I am comfortable exploring uncertainty. If a model underperforms, I know how to reason about it, where to look, and which assumptions to challenge. Not because I am particularly clever, but because experience has made the terrain familiar.

In the cloud, I do not have that intuition yet. And that is the difference.

## The identity shift

The most difficult part has not been the content itself, at least not entirely. It has been the identity shift.

I am used to being the person who understands things quickly, the one who synthesises complexity, who provides relatable examples, who translates difficult ideas into everyday language (one day I will tell you about the Ofsted inspector who crashed my SVM lesson).

Now I am the one asking what feel like embarrassingly basic questions:

<div class="de-beginner-questions" aria-label="Questions Francesca finds herself asking">
  <p>What does this service actually do?</p>
  <p>Why isn't this connecting?</p>
  <p>Have I misunderstood how this is supposed to work?</p>
</div>

They are honest questions, possibly necessary questions, but they are definitely not the questions of an expert.

There is a quiet discomfort in not being the most competent person in the room, in hesitating before speaking, in realising that someone with five years of industry DevOps experience sees patterns that you simply cannot see yet.

It is humbling and, if I am honest, quite unsettling.

## Expertise is domain-specific

One of the most important lessons I am relearning is that expertise is brutally domain-specific.

<figure class="de-domain-gap">
  <div class="de-domain-gap__head" aria-hidden="true">
    <span>Machine learning</span>
    <span>Cloud</span>
  </div>
  <div class="de-domain-gap__row">
    <p>Being fluent in neural networks</p>
    <i aria-hidden="true"></i>
    <p>does not make you fluent in infrastructure design.</p>
  </div>
  <div class="de-domain-gap__row">
    <p>Understanding backpropagation</p>
    <i aria-hidden="true"></i>
    <p>does not mean you instinctively grasp cloud networking boundaries.</p>
  </div>
  <figcaption>Intellectual confidence does not automatically transfer across domains.</figcaption>
</figure>

That is a useful, if uncomfortable, realisation.

In academia especially, it is easy to let competence solidify into identity. You become "the AI person", the specialist, the expert. But the moment you step outside that domain, you are simply another learner navigating unfamiliar terrain.

And that is healthy, or at least that is how I am choosing to see it.

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">When did you last feel like a beginner at work?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="Then you know the feeling: hesitating before speaking, asking questions that feel basic. Francesca's experience is that it also makes you a more patient teacher and colleague.">Recently</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="Francesca's case for stepping outside your domain: it is humbling, and it changes how you see the people you teach or manage.">I can't remember</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

## Seeing my students differently

The most profound shift, however, has happened in my classroom.

I teach many Level 6 and Level 7 professionals on degree apprenticeships. They work full time, manage teams, and deliver real-world projects. They are capable, experienced individuals who carry significant responsibility in their organisations.

Then they come into my lectures.

Sometimes they hesitate before answering.

<figure class="de-lecture-chat">
  <div class="de-lecture-chat__moment">
    <p class="de-lecture-chat__note">Sometimes their uncertainty is visible even behind a chat window:</p>
    <div class="de-lecture-chat__window">
      <p class="de-lecture-chat__typing"><span>Jack is typing…</span><i></i><i></i><i></i></p>
    </div>
    <p class="de-lecture-chat__note">and then no message appears.</p>
  </div>
  <div class="de-lecture-chat__moment">
    <p class="de-lecture-chat__note">Sometimes they apologise before asking a question, softening it with:</p>
    <div class="de-lecture-chat__window">
      <p class="de-lecture-chat__msg">This may be a silly question…</p>
    </div>
    <p class="de-lecture-chat__note">(spoiler: it almost never is)</p>
  </div>
</figure>

I used to interpret this primarily as cognitive load. Balancing work and study is objectively demanding. Now I see something deeper: identity vulnerability.

Because I am feeling it myself.

When you are competent in your profession and then sit in a classroom where you do not immediately understand something, it can be destabilising. You are no longer the expert. You are no longer fully fluent. You are exposed, and it takes courage to remain in that space.

My students have been doing that all along.

As I began to see them differently, I realised I was seeing my children differently too. I started noticing that familiar flash of frustration at home: the tightened jaw, the quick "I can't do this," the moment where confidence wavers. What looks like resistance is often just the discomfort of not knowing yet. What looks like disengagement is often vulnerability. And instead of correcting it, I began to recognise it, because it is the same vulnerability I feel when I am out of my depth.

## The courage of showing up

There is a particular kind of bravery in being a beginner when you are used to being capable. It would be easier not to enrol, not to stretch, and to remain in the domain where you are respected and confident.

<p class="de-article-interjection">But growth lives precisely in that discomfort.</p>

As I wrestle with cloud architectures and deployment failures, I find myself becoming more patient in my teaching. I pause longer. I normalise confusion explicitly. I tell students, "It is completely reasonable not to understand this immediately."

Because now I know, not abstractly but viscerally, what that feels like. I am relearning the emotional landscape of learning.

## What this is changing

Going back to being a student has changed how I think about education in technology.

It has reminded me that:

<ul class="de-not-the-same">
  <li><strong>Speed</strong><em aria-hidden="true">≠</em><strong>intelligence</strong><span class="de-not-the-same__say">Speed is not the same as intelligence.</span></li>
  <li><strong>Confidence</strong><em aria-hidden="true">≠</em><strong>competence</strong><span class="de-not-the-same__say">Confidence is not the same as competence.</span></li>
  <li class="is-growth"><strong>Struggle</strong><em aria-hidden="true">≠</em><strong>inadequacy</strong><span class="de-not-the-same__say">Struggle is not a sign of inadequacy</span><span>but a sign of growth and courage.</span></li>
</ul>

It has also made me more aware of the subtle power dynamics in a classroom. When you stand at the front as the "expert," it is easy to forget what it feels like to sit in the audience.

Cloud engineering has forced me back into that seat.

<p class="de-article-interjection">And I am grateful for it.</p>

{{ discussion_box(page) }}

{{ related_reading(page) }}
