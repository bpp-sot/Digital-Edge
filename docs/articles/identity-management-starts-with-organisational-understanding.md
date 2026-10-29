---
title: "Why Effective Identity Management Starts with Organisational Understanding"
description: "An ICT learner working in a large, decentralised organisation explains why identity and access management depends as much on people, relationships and structure as it does on technology."
author: "An ICT learner"
date: "2026-10-29"
updated: "2026-10-29"
date_display: "29 October 2026"
read_time: "4 min read"
tags:
  - Security
  - Workflows
type: article
render_macros: true
hero_pill: "Learner perspective"
hero_quote: "Some of the biggest challenges don't come from the technology itself. They come from the complexity of the organisation that the technology is trying to represent."
summary:
  - "To most users, identity is a username, a password and an MFA prompt. The hardest problems sit underneath, in the organisation the technology is trying to represent."
  - "People rarely fit one category, and access tends to accumulate as they change roles, finish projects and help out elsewhere, which is why regular permission reviews matter."
  - "Automation only helps when the data about who someone is, what they need and when that should change is accurate."
takeaways:
  - label: "Start with the organisation"
    text: "A clear picture of roles, responsibilities and data ownership comes before any technical fix."
  - label: "Access creeps"
    text: "Department moves, finished projects and 'temporary' access with no end date all leave permissions behind."
  - label: "Least access over convenience"
    text: "Urgency and seniority make it easier to say yes than to ask why the access is needed."
questions:
  - label: "Identity"
    text: "How do you know who someone is?"
  - label: "Access"
    text: "What should they have access to?"
  - label: "Change"
    text: "When should that access change?"
user_groups:
  - "Undergraduate students"
  - "Postgraduate students"
  - "Researchers"
  - "Visiting academics"
  - "Professional services staff"
  - "Contractors"
  - "Committee members"
  - "External collaborators"
overlaps:
  - label: "Two roles at once"
    title: "Researcher and student"
    text: "A researcher may also be a student."
  - label: "An account with a past"
    title: "Staff, formerly a student"
    text: "A member of staff may have previously been a student and already have an account history from that department."
  - label: "A new team"
    title: "Contractor, new team"
    text: "An external contractor may have worked with one project in the past but now needs to support a different team."
automation:
  - title: "Create accounts"
    text: "Automatically creating new user accounts."
  - title: "Grant access by role"
    text: "Granting role-based permissions."
  - title: "Disable leavers"
    text: "Disabling accounts when somebody leaves."
automation_quote:
  text: "Technology can automate decisions, but it cannot necessarily determine whether the decisions are correct."
discussion:
  - "Which security groups in your organisation could nobody explain the purpose of?"
  - "When did you last see 'temporary' access actually removed?"
  - "If you automated account creation, permissions and leavers tomorrow, how accurate would the data behind it be?"
related:
  - tag: "AI"
    title: "AI Under Pressure: Analysing the OpenAI Sandbox Leak"
    description: "What a security incident reveals about access, containment and accountability in AI systems."
    href: "../ai-under-pressure-openai-sandbox-leak/"
  - tag: "Networking"
    title: "WiFi 7 vs Private 5G"
    description: "Gary Martyn on whether WiFi is dying, and the skills network and ICT professionals will need next."
    href: "../wifi-7-vs-private-5g/"
  - tag: "AI"
    title: "Don't Make AI Your Single Point of Failure"
    description: "Matt Lucas on resilience, and why every system needs an alternative route."
    href: "../dont-make-ai-your-single-point-of-failure/"
---

# Why Effective Identity Management Starts with Organisational Understanding

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

When thinking about IT accounts, most people probably imagine a username, password and perhaps a multi-factor authentication prompt on their phone. To the non-technical end user, their account either works or it doesn't; it gives them access to what they need or it doesn't.

To add on a technical layer underneath this, we may understand something about how an identity platform authenticates users, the security checks that look for suspicious sign-in attempts, the permissions that have been given to that account to access certain resources, and the synchronisation that takes place between the various systems and services involved.

But my experience within a large, decentralised organisation has shown that some of the biggest challenges don't come from the technology itself. They come from the complexity of the organisation that the technology is trying to represent, and they require an understanding of people, relationships and organisational structure in order to work towards an effective identity management solution.

<figure class="de-iceberg">
  <div class="de-iceberg__sky">
    <div class="de-iceberg__layer de-iceberg__layer--tip">
      <span>What end users see</span>
      <strong>A username, a password, and perhaps an MFA prompt</strong>
    </div>
  </div>
  <div class="de-iceberg__sea">
    <div class="de-iceberg__layer de-iceberg__layer--technical">
      <span>The technical layer</span>
      <strong>Authentication, sign-in security checks, permissions and synchronisation</strong>
    </div>
    <div class="de-iceberg__layer de-iceberg__layer--deep">
      <span>Where the biggest challenges are</span>
      <strong>People, relationships and organisational structure</strong>
    </div>
  </div>
  <figcaption>Most people only see the tip. The hardest problems sit deepest.</figcaption>
</figure>

Universities, global businesses, government departments and healthcare institutions, to name a few, all face the same questions:

{{ story_callouts(page, "questions") }}

## One person, many roles

Take a university, for example. The end users consist of:

{{ story_chips(page, "user_groups") }}

Each group requires different access to different systems; some people fit neatly into one category, but many do not.

{{ story_cards(page, "overlaps") }}

Key questions that may be asked by a central IT service desk who manage user permissions, such as why this access is required, who ought to approve it and how long should it stay in place, may not have clear answers.

<figure class="de-access-request">
  <div class="de-access-request__bar">
    <strong>Access request</strong>
    <span>Awaiting review</span>
  </div>
  <dl>
    <div>
      <dt>Why is this access required?</dt>
      <dd>Not clear</dd>
    </div>
    <div>
      <dt>Who ought to approve it?</dt>
      <dd>Not clear</dd>
    </div>
    <div>
      <dt>How long should it stay in place?</dt>
      <dd>Not clear</dd>
    </div>
  </dl>
</figure>

An organisational chart with departments, management structures and approval requirements may help in some instances, but what about where projects involve people from multiple departments, committees are made up of internal and external members, and research collaborations link together local participants with those from other organisations?

An identity system needs to be able to take all of these complex relationships and translate them into something that can be captured and stored in a structured way, and this can be surprisingly difficult. This is one of the reasons why regular reviews of permissions are so important.

## How access accumulates

Over time, the tendency is for users' access to accumulate. A staff member may move to a new department but retain their access from the previous role. A project may conclude but the associated groups remain active. Someone may be given 'temporary' access to a shared mailbox to assist with a heavy workload, with no fixed end date, and the access still existing several years later.

<figure class="de-access-creep">
  <ol>
    <li>
      <span class="de-access-creep__when">Joins</span>
      <strong>Starts in a department</strong>
      <ul>
        <li>Department A groups</li>
      </ul>
    </li>
    <li>
      <span class="de-access-creep__when">Moves</span>
      <strong>Moves to a new department</strong>
      <ul>
        <li class="is-stale">Department A groups</li>
        <li>Department B groups</li>
      </ul>
    </li>
    <li>
      <span class="de-access-creep__when">Project ends</span>
      <strong>A project concludes</strong>
      <ul>
        <li class="is-stale">Department A groups</li>
        <li>Department B groups</li>
        <li class="is-stale">Project groups, still active</li>
      </ul>
    </li>
    <li>
      <span class="de-access-creep__when">Years later</span>
      <strong>"Temporary" help with a heavy workload</strong>
      <ul>
        <li class="is-stale">Department A groups</li>
        <li>Department B groups</li>
        <li class="is-stale">Project groups, still active</li>
        <li class="is-stale">Shared mailbox, no end date</li>
      </ul>
    </li>
  </ol>
  <figcaption><span class="de-access-creep__key" aria-hidden="true"></span> No longer needed. An illustration of one person's access built from the examples above: four sets of access, one still needed.</figcaption>
</figure>

Another challenge exists where there is not clear documentation about the purpose and usage of a security group. New users may be added to groups such as 'All Staff' or 'All Staff in My Department' or 'All Staff in My Building', which were set up longer ago than the living memory of anyone currently in the organisation and which do not have any associated descriptions about where these groups are used and what resources they give access to.

<div class="de-mystery-groups" aria-label="Security groups with no documentation">
  <article>
    <h3>All Staff</h3>
    <dl>
      <dt>Description</dt>
      <dd>None</dd>
      <dt>Gives access to</dt>
      <dd>Unknown</dd>
    </dl>
  </article>
  <article>
    <h3>All Staff in My Department</h3>
    <dl>
      <dt>Description</dt>
      <dd>None</dd>
      <dt>Gives access to</dt>
      <dd>Unknown</dd>
    </dl>
  </article>
  <article>
    <h3>All Staff in My Building</h3>
    <dl>
      <dt>Description</dt>
      <dd>None</dd>
      <dt>Gives access to</dt>
      <dd>Unknown</dd>
    </dl>
  </article>
</div>

## Convenience versus least access

There is a natural tendency to prioritise convenience of access over the strict principle of least access. If a new starter *probably* needs to be part of a particular security group, then it can seem better to add them to avoid any future issues. If a request comes through asking for access for a senior member of staff, or with a sense of urgency, it feels easier to comply than to question it.

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">An urgent request arrives: a senior member of staff needs access today. What do you do?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="It feels easier to comply than to question it, and that is the trap. The benefits of granting access are visible straight away; the risks of access that should not have been granted are not.">Grant it, it's urgent</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That is the principle of least access in practice. Urgency and seniority do not answer why the access is needed, who should approve it, or how long it should stay in place.">Ask why it's needed, who approves it, and for how long</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

The immediate benefits of providing access to those who need it are more visible than the potential risks of not denying access or of not removing it once a legitimate need has passed.

## Start with the organisation

My experience is showing that, aside from having a technical system that is capable of performing the task, identity and access management starts with a clear and accurate picture of the organisation as a whole, the role and responsibilities of each user, and the hierarchy of data ownership and responsibility.

Many organisations are pursuing automation within their processes for greater efficiency and to reduce human error with, for example:

{{ story_steps(page, "automation") }}

Yet this only works if the underlying data about who a person is, what they need access to, and when that access should change, is accurate.

{{ story_pull_quote(page, "automation_quote") }}

<section class="de-article-close-panel">
  <div>
    <p class="de-kicker">What it takes</p>
    <h2>Solid data, clear governance and good communication.</h2>
    <p>A robust identity management programme requires solid data, clear governance and good communication between users, managers, system owners and administrators.</p>
  </div>
  <aside>
    <h3>Why it matters now</h3>
    <p>As organisations increase their reliance on digital infrastructure, and the risks of misuse become ever-more threatening in today's world, the essential task of unpicking the complexity of an organisation's structure and the way in which it maps to the identities and access of its users has never been more important.</p>
  </aside>
</section>

{{ discussion_box(page) }}

{{ related_reading(page) }}
