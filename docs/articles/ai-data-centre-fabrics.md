---
title: "AI Data Centre Fabrics: Is Artificial Intelligence Redesigning Networking from the Ground Up?"
description: "AI training clusters are putting demands on data centre networks that they were never designed for. Gary Martyn on GPUs, microseconds, Ethernet vs InfiniBand, and what it all means for IT support, network engineering and cyber security."
author: "Gary Martyn"
author_slug: "gary-martyn"
author_role: "Networking, Cyber Security and ICT Programme Lead"
date: "2026-11-26"
updated: "2026-11-26"
date_display: "26 November 2026"
read_time: "8 min read"
tags:
  - Networking
  - AI
  - Careers
type: article
render_macros: true
hero_pill: "Suddenly, microseconds matter"
hero_quote: "In many AI environments, the network is no longer simply connecting systems."
summary:
  - "When thousands of GPUs train a model together, they exchange enormous volumes of data constantly. The network becomes part of the computing platform, and microseconds start to matter."
  - "Ethernet and InfiniBand are competing to carry AI workloads. For now, Gary thinks both sides of the argument have merit."
  - "AI could renew interest in enterprise and co-location data centres, and it is pulling IT support, network engineering and cyber security closer together."
takeaways:
  - label: "Traffic that never stops"
    text: "Traditional applications create predictable traffic. AI training creates enormous, constant east-west traffic between GPUs."
  - label: "Idle GPUs are expensive"
    text: "If latency rises or bandwidth runs short, costly compute ends up waiting for data instead of processing it."
  - label: "Work across boundaries"
    text: "The most valuable professionals may be those whose skills span networking, cloud, security, automation and AI."
winners_quote:
  text: "The winners will not necessarily be the people who know the most commands or the most protocols. They will be the professionals who continuously learn, embrace new technologies and understand how AI is reshaping the entire technology landscape."
discussion:
  - "Which of the AI networking technologies in this article could you explain to a colleague today?"
  - "Where do IT support, networking and security already overlap in your organisation?"
  - "Would your organisation run large AI workloads in the public cloud or in its own data centre, and why?"
related:
  - tag: "Networking"
    title: "WiFi 7 vs Private 5G: Is WiFi Dying and Should We Ditch It Now?"
    description: "Gary Martyn on another networking debate, and why coexistence usually beats replacement."
    href: "../wifi-7-vs-private-5g/"
  - tag: "Security"
    title: "The AI Agent Security Problem Nobody Can Afford to Ignore"
    description: "Ant Lees on prompt injection, least privilege and securing AI that can take actions."
    href: "../ai-agent-security-problem/"
  - tag: "AI"
    title: "Don't Make AI Your Single Point of Failure"
    description: "Matt Lucas on sub-sea cables, outages, and why resilient systems need alternative routes."
    href: "../dont-make-ai-your-single-point-of-failure/"
---

# AI Data Centre Fabrics: Is Artificial Intelligence Redesigning Networking from the Ground Up?

{{ article_hero(page) }}

{{ article_summary(page) }}

{{ article_takeaways(page) }}

For decades, data centre networking evolved in a fairly predictable way. Organisations built networks to support familiar workloads such as email, databases, web applications, file storage and virtual machines. The web applications changed and evolved, and new database capabilities came along, but the fundamental use case didn't change.

Network upgrades were often driven by growth, but the underlying architecture remained relatively stable.

<figure class="de-speed-steps">
  <p class="de-speed-steps__lead">Speeds increased from 1GbE to 10GbE, then to 25GbE and 100GbE</p>
  <ol class="de-speed-steps__bars">
    <li style="--h: 10"><span>1GbE</span></li>
    <li style="--h: 41"><span>10GbE</span></li>
    <li style="--h: 53"><span>25GbE</span></li>
    <li style="--h: 72"><span>100GbE</span></li>
    <li class="is-ai" style="--h: 91"><span>400GbE</span></li>
    <li class="is-ai" style="--h: 100"><span>800GbE</span></li>
  </ol>
  <p class="de-speed-steps__key"><span>Familiar workloads</span><span class="is-ai">What AI is now demanding</span><em>Bar heights use a logarithmic scale</em></p>
  <figcaption>...but the basic principles of networking changed very little.</figcaption>
</figure>

<p class="de-article-interjection">Now, however, Artificial Intelligence is challenging those established norms.</p>

The rise of Large Language Models, AI training clusters and increasingly sophisticated AI applications is creating demands that traditional enterprise networks were never designed to handle. This raises an interesting question:

<figure class="de-fabric-question">
  <p class="de-fabric-question__main">Is AI fundamentally changing how networks are designed?</p>
  <p class="de-fabric-question__or"><span>Or</span></p>
  <p class="de-fabric-question__alt">Is this simply another technology cycle that will eventually settle into the existing networking landscape?</p>
</figure>

## Why AI is different

Most traditional enterprise applications generate predictable patterns of network traffic. For example, a database server communicates with an application server, users connect to SaaS platforms, or backup jobs move data overnight.

AI workloads are very different. When thousands of GPUs work together to train a model, they constantly exchange enormous volumes of data.

In many AI environments, the network is no longer simply connecting systems.

<figure class="de-traffic">
  <div class="de-traffic__panel de-traffic__panel--classic">
    <p class="de-traffic__label"><strong>Traditional workloads</strong><span>Predictable patterns</span></p>
    <ul class="de-traffic__flows">
      <li><span>Database server</span><i aria-hidden="true"></i><span>Application server</span></li>
      <li><span>Users</span><i aria-hidden="true"></i><span>SaaS platforms</span></li>
      <li><span>Backup jobs</span><i aria-hidden="true"></i><span>Overnight</span></li>
    </ul>
  </div>
  <div class="de-traffic__panel de-traffic__panel--ai">
    <p class="de-traffic__label"><strong>AI training</strong><span>Constant, enormous exchange</span></p>
    <div class="de-traffic__mesh" aria-hidden="true">
      <i class="de-traffic__wire de-traffic__wire--h" style="--pos: 16.66%; --d: 1.1s; --delay: 0s"></i>
      <i class="de-traffic__wire de-traffic__wire--h" style="--pos: 50%; --d: 0.9s; --delay: 0.3s"></i>
      <i class="de-traffic__wire de-traffic__wire--h" style="--pos: 83.33%; --d: 1.2s; --delay: 0.6s"></i>
      <i class="de-traffic__wire de-traffic__wire--v" style="--pos: 12.5%; --d: 1s; --delay: 0.2s"></i>
      <i class="de-traffic__wire de-traffic__wire--v" style="--pos: 37.5%; --d: 0.8s; --delay: 0.5s"></i>
      <i class="de-traffic__wire de-traffic__wire--v" style="--pos: 62.5%; --d: 1.1s; --delay: 0.1s"></i>
      <i class="de-traffic__wire de-traffic__wire--v" style="--pos: 87.5%; --d: 0.9s; --delay: 0.4s"></i>
      <b>GPU</b><b>GPU</b><b>GPU</b><b>GPU</b>
      <b>GPU</b><b>GPU</b><b>GPU</b><b>GPU</b>
      <b>GPU</b><b>GPU</b><b>GPU</b><b>GPU</b>
    </div>
    <p class="de-traffic__note">Thousands of GPUs working together</p>
  </div>
  <figcaption>The network effectively becomes part of the computing platform itself, in a way unlike any workload before it.</figcaption>
</figure>

This has created demand for technologies such as:

<div class="de-chip-list" aria-label="Technologies in demand for AI networking">
  <span>400 and 800 Gigabit Ethernet</span>
  <span>Remote Direct Memory Access (RDMA)</span>
  <span>Ultra-low latency network fabrics</span>
  <span>Lossless Ethernet technologies</span>
  <span>High-performance spine-leaf architectures</span>
</div>

<p class="de-article-interjection">Suddenly, microseconds matter!</p>

Network bottlenecks or latency that would have gone unnoticed in a traditional data centre can significantly impact the performance and cost of AI workloads.

## Are traditional data centre designs under pressure?

For many years, enterprise data centres were designed around application availability and resilience. AI introduces a different priority.

<figure class="de-gpu-wait">
  <div class="de-gpu-wait__shift">
    <p class="de-gpu-wait__was"><span>Designed around</span><strong>Availability</strong><strong>Resilience</strong></p>
    <i aria-hidden="true">→</i>
    <p class="de-gpu-wait__now"><span>AI's priority</span><strong>Immediacy</strong><small>in terms of both bandwidth and latency</small></p>
  </div>
  <div class="de-gpu-wait__racks">
    <div class="de-gpu-wait__rack is-flowing">
      <p class="de-gpu-wait__rack-label">Data arriving in time</p>
      <ul>
        <li><b>GPU</b><span>Processing</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li><b>GPU</b><span>Processing</span></li>
      </ul>
    </div>
    <div class="de-gpu-wait__rack is-starved">
      <p class="de-gpu-wait__rack-label">Latency up, bandwidth constrained</p>
      <ul>
        <li class="is-waiting"><b>GPU</b><span>Waiting for data</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li class="is-waiting"><b>GPU</b><span>Waiting for data</span></li>
        <li class="is-waiting"><b>GPU</b><span>Waiting for data</span></li>
        <li><b>GPU</b><span>Processing</span></li>
        <li class="is-waiting"><b>GPU</b><span>Waiting for data</span></li>
      </ul>
    </div>
  </div>
  <figcaption>If network latency increases or bandwidth becomes constrained, expensive compute resources can end up waiting for data instead of processing it.</figcaption>
</figure>

Large AI clusters often require thousands of accelerators working simultaneously. As a result, many organisations are redesigning their data centres around AI clusters rather than traditional applications.

This has led some industry commentators to suggest that AI may represent the biggest change in data centre networking since the adoption of cloud computing.

If that proves to be true, network engineers may need to rethink assumptions that have remained largely unchanged for decades.

## The Ethernet vs InfiniBand debate

No discussion about AI networking would be complete without addressing one of the hottest debates in the industry.

<p class="de-article-interjection">Will Ethernet dominate AI networking, or will InfiniBand remain the preferred choice?</p>

Traditionally, InfiniBand has been the technology of choice for high-performance computing environments, and what it offers has made it attractive for large AI training environments. However, Ethernet continues to evolve, with each new generation bringing new abilities.

Many organisations already possess extensive Ethernet expertise and operational processes, which introduces an obvious question:

<figure class="de-fabric-question de-fabric-question--single">
  <p class="de-fabric-question__main">If Ethernet can deliver AI performance that is "good enough", why introduce an entirely different networking technology?</p>
</figure>

<figure class="de-fabric-faceoff">
  <p class="de-fabric-faceoff__title">The key differences and merits of InfiniBand and RoCE Ethernet</p>
  <div class="de-fabric-faceoff__ring">
    <article class="de-fabric-faceoff__corner de-fabric-faceoff__corner--ib">
      <span class="de-fabric-faceoff__tag">The traditional choice for HPC</span>
      <h3>InfiniBand</h3>
      <ul>
        <li>Extremely low latency</li>
        <li>High throughput</li>
        <li>Efficient GPU-to-GPU communication</li>
        <li>Mature support for high-performance computing workloads</li>
      </ul>
      <p class="de-fabric-faceoff__case"><span>Its supporters counter</span>The largest AI deployments continue to demand the absolute lowest latency and highest efficiency available.</p>
    </article>
    <p class="de-fabric-faceoff__vs" aria-hidden="true">VS</p>
    <article class="de-fabric-faceoff__corner de-fabric-faceoff__corner--eth">
      <span class="de-fabric-faceoff__tag">Evolving with every generation</span>
      <h3>Ethernet <small>with RoCE</small></h3>
      <ul>
        <li>400GbE and 800GbE connectivity</li>
        <li>RDMA over Converged Ethernet (RoCE)</li>
        <li>Improved congestion management</li>
        <li>Ultra-low latency capabilities</li>
      </ul>
      <p class="de-fabric-faceoff__case"><span>Its supporters argue</span>Lower operational complexity, a broader ecosystem and an existing skills base make it the logical long-term winner.</p>
    </article>
  </div>
  <figcaption>At the moment, both arguments have merit.</figcaption>
</figure>

## So, could AI actually help make enterprise data centres relevant again?

For years, many predicted that public cloud would gradually absorb increasingly large portions of enterprise infrastructure, and this has largely proven to be the case so far. Increasingly, enterprises prefer to utilise cloud-based computing and avoid the expense, risk and human resource management costs of in-house enterprise data centres.

<p class="de-article-interjection">But AI may complicate that prediction.</p>

<figure class="de-dc-rack">
  <div class="de-dc-rack__cabinet">
    <p class="de-dc-rack__lead">Training and operating large AI models requires</p>
    <ol class="de-dc-rack__units">
      <li><i aria-hidden="true"></i>Massive power consumption</li>
      <li><i aria-hidden="true"></i>Specialised cooling</li>
      <li><i aria-hidden="true"></i>High-speed networking</li>
      <li><i aria-hidden="true"></i>Large GPU clusters</li>
      <li class="is-more"><i aria-hidden="true"></i>And more</li>
    </ol>
  </div>
  <p class="de-dc-rack__tag"><span>Not to mention</span>significant capital investment</p>
</figure>

For some organisations, the economics of AI may encourage investment in private infrastructure again, rather than relying entirely on public cloud services. Of course, that does not mean cloud computing is disappearing.

<p class="de-article-interjection">Far from it...</p>

<figure class="de-dc-swing">
  <div class="de-dc-swing__track" aria-hidden="true">
    <span class="de-dc-swing__end de-dc-swing__end--cloud">Public cloud</span>
    <span class="de-dc-swing__end de-dc-swing__end--dc">Enterprise and co-location</span>
    <i class="de-dc-swing__rail"><b class="de-dc-swing__marker"></b></i>
  </div>
  <div class="de-dc-swing__cols">
    <div class="de-dc-swing__col de-dc-swing__col--cloud">
      <span>For years</span>
      <p>Public cloud gradually absorbed increasingly large portions of enterprise infrastructure.</p>
    </div>
    <div class="de-dc-swing__col de-dc-swing__col--dc">
      <span>With AI</span>
      <p>AI could create a renewed interest in enterprise and co-location data centres as organisations seek greater control over:</p>
      <ul>
        <li>Performance</li>
        <li>Data sovereignty</li>
        <li>Long-term operating costs</li>
      </ul>
    </div>
  </div>
  <figcaption>In an unexpected twist, AI might be helping to drive a new era of data centre investment rather than accelerating its decline.</figcaption>
</figure>

## What does this mean for IT support, network engineering and cyber security professionals?

Perhaps the most important question is not what happens to the technology. It is what happens to the people responsible for designing, deploying, supporting and securing it.

AI infrastructure is already transforming expectations across multiple IT disciplines. The emergence of AI data centre fabrics is not simply creating a new networking challenge. It is creating a new skill set that spans infrastructure, networking, cloud, security and operations.

Whether you work in IT Support, Network Engineering or Cyber Security, the growth of AI workloads is likely to influence your role over the coming years.

<nav class="de-role-jump" aria-label="Jump to your role">
  <a class="is-support" href="#it-support-supporting-ai-powered-infrastructure"><span>IT Support</span><small>Supporting AI-powered infrastructure</small></a>
  <a class="is-network" href="#network-engineering-the-network-becomes-part-of-the-compute-platform"><span>Network Engineering</span><small>The network becomes part of the compute platform</small></a>
  <a class="is-security" href="#cyber-security-protecting-ai-infrastructure"><span>Cyber Security</span><small>Protecting AI infrastructure</small></a>
</nav>

### IT support: supporting AI-powered infrastructure

For support professionals, AI infrastructure introduces technologies that many help desk and infrastructure teams have rarely encountered before.

<figure class="de-support-queue">
  <div class="de-support-queue__col is-then">
    <p class="de-support-queue__head">Historically, support engineers focused on</p>
    <ul>
      <li>End-user devices</li>
      <li>Server administration</li>
      <li>Microsoft 365 and business applications</li>
      <li>Virtual machines</li>
      <li>General network troubleshooting</li>
    </ul>
  </div>
  <div class="de-support-queue__col is-now">
    <p class="de-support-queue__head">Increasingly, they may support environments that include</p>
    <ul>
      <li>GPU-enabled workstations</li>
      <li>AI development platforms</li>
      <li>Large-scale data processing workloads</li>
      <li>High-performance storage systems</li>
      <li>AI-assisted monitoring platforms</li>
      <li>Intelligent automation tools</li>
    </ul>
  </div>
</figure>

At the same time, AI will almost certainly become part of the support toolkit itself.

AI-powered observability platforms are already becoming capable of detecting issues, analysing root causes and recommending remediation actions before users even raise a support ticket.

<ol class="de-observe-flow" aria-label="What AI-powered observability platforms are becoming capable of">
  <li><span>1</span>Detect the issue</li>
  <li><span>2</span>Analyse the root cause</li>
  <li><span>3</span>Recommend remediation</li>
  <li class="is-skipped"><span aria-hidden="true">✕</span><s>User raises a ticket</s><small>Before users even get there</small></li>
</ol>

This may mean future support professionals spend less time reacting to incidents and more time validating AI recommendations, managing complex systems and supporting business adoption of AI technologies.

The role is unlikely to disappear. Instead, it is likely to become more technical, analytical and automation focused.

### Network engineering: the network becomes part of the compute platform

Network engineers may experience some of the most significant changes. Traditional enterprise networking has primarily focused on connecting users to applications and services.

AI fundamentally changes this relationship.

Large AI clusters generate enormous amounts of east-west traffic (moving data between servers inside the data centre) as GPUs continuously exchange information during training and inference operations. In many environments, the network is no longer simply transporting data. The network becomes part of the computing platform itself.

As a result, network engineers are increasingly being asked to understand:

<figure class="de-switch">
  <div class="de-switch__chassis">
    <p class="de-switch__brand"><strong>AI fabric switch</strong><span>Light up each port you could explain today</span></p>
    <div class="de-switch__ports">
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>AI training clusters</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>400GbE and 800GbE networking</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>Spine-leaf architectures</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>RDMA and RoCE technologies</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>Ultra-low latency design</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>High-density optical networking</span></label>
      <label class="de-switch__port"><input type="checkbox"><i aria-hidden="true"></i><span>AI infrastructure performance metrics</span></label>
    </div>
    <p class="de-switch__count" aria-hidden="true"></p>
  </div>
</figure>

Perhaps more importantly, network engineers may need to work much more closely with cloud, compute and storage teams than ever before.

The traditional boundaries between infrastructure disciplines are becoming increasingly blurred.

### Cyber security: protecting AI infrastructure

AI also presents significant opportunities and challenges for cyber security professionals. Large AI environments create entirely new attack surfaces.

<figure class="de-attack-surface">
  <p class="de-attack-surface__lead">Security teams must now consider risks associated with</p>
  <div class="de-attack-surface__map">
    <p class="de-attack-surface__core">Large AI environment</p>
    <ul>
      <li>AI models</li>
      <li>Training data</li>
      <li>GPU infrastructure</li>
      <li>High-performance data networks</li>
      <li>AI supply chains</li>
      <li>Model theft and intellectual property protection</li>
    </ul>
  </div>
</figure>

At the same time, many existing security tools are beginning to integrate AI-powered capabilities.

<figure class="de-soc-console">
  <p class="de-soc-console__bar"><i aria-hidden="true"></i><i aria-hidden="true"></i><i aria-hidden="true"></i><strong>SOC: AI-assisted platform</strong></p>
  <p class="de-soc-console__lead">Security Operations Centres (SOCs) are increasingly using AI-assisted platforms to</p>
  <ul>
    <li><code>detect</code>Detect threats faster</li>
    <li><code>correlate</code>Correlate events automatically</li>
    <li><code>prioritise</code>Prioritise incidents</li>
    <li><code>reduce</code>Reduce alert fatigue</li>
    <li><code>hunt</code>Support threat hunting activities</li>
  </ul>
</figure>

<p class="de-article-interjection">This creates an interesting paradox...</p>

Cyber security professionals will increasingly need to understand both how to leverage AI and how to defend against it.

The challenge is no longer simply securing servers and networks. It is securing intelligent systems operating at unprecedented scale and speed.

## The rise of the infrastructure professional

The most interesting development may be that these disciplines are gradually moving closer together. In the past, support teams, network engineers and cyber security professionals often operated as distinct specialisms.

<figure class="de-converge">
  <div class="de-converge__circles">
    <span class="is-support">IT Support</span>
    <span class="is-network">Network Engineering</span>
    <span class="is-security">Cyber Security</span>
  </div>
  <figcaption>AI infrastructure increasingly requires collaboration across all three.</figcaption>
</figure>

<figure class="de-question-swap">
  <p class="de-question-swap__but">We are moving away from asking</p>
  <p class="de-question-swap__old"><s>"How do we support the network?"</s></p>
  <p class="de-question-swap__but">And instead asking</p>
  <p class="de-question-swap__new">"How do we build, secure and optimise an entire AI-enabled infrastructure ecosystem?"</p>
</figure>

This requires professionals who can understand networking, cloud, security, automation, data protection, AI and business requirements across a range of technologies and types of infrastructure.

The organisations that gain the greatest value from AI are likely to be those whose technical teams can work effectively across these traditional boundaries.

## The skills that may matter most

While specialist knowledge remains important, the most valuable professionals may be those who develop skills that apply across multiple disciplines.

<figure class="de-t-skills">
  <p class="de-t-skills__label">Skills that apply across multiple disciplines</p>
  <ul class="de-t-skills__bar">
    <li>Automation and Infrastructure as Code</li>
    <li>Python and API integration</li>
    <li>AI fundamentals</li>
    <li>Cloud architecture</li>
    <li>Data analysis</li>
    <li>Observability and monitoring</li>
    <li>Security by design</li>
    <li>Critical thinking and problem solving</li>
  </ul>
  <p class="de-t-skills__stem"><strong>Specialist knowledge</strong><span>still important</span></p>
</figure>

The future may belong less to narrowly defined technology specialists and more to adaptable infrastructure professionals who can understand how networking, security, support and AI platforms work together.

## So, what do I think?

I don't believe AI data centre fabrics will reduce the demand for IT professionals.

<p class="de-article-interjection">I believe they will change the nature of the work.</p>

<div class="de-role-forecast" aria-label="How Gary expects each role to change">
  <article class="is-support"><span>Support engineers</span><p>will increasingly work alongside AI tools.</p></article>
  <article class="is-network"><span>Network engineers</span><p>will need to understand how networks enable AI workloads.</p></article>
  <article class="is-security"><span>Cyber security professionals</span><p>will face entirely new AI-driven threats while using AI to improve defence.</p></article>
</div>

{{ story_pull_quote(page, "winners_quote") }}

<p class="de-article-interjection">And for those willing to adapt, that presents a tremendous opportunity.</p>

## What do you think?

<div class="de-article-poll" data-article-poll aria-label="Quick poll">
  <p class="de-article-poll__question">Will Ethernet eventually become the dominant fabric for AI networking, or will InfiniBand retain its position at the highest end of AI computing?</p>
  <div class="de-article-poll__choices">
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That's the case Ethernet's supporters make: lower operational complexity, a broader ecosystem and a skills base most organisations already have. For now, Gary thinks both arguments have merit.">Ethernet will dominate</button>
    <button type="button" class="de-article-poll__choice" data-poll-choice aria-pressed="false" data-feedback="That's the InfiniBand camp's argument: the largest AI deployments still demand the absolute lowest latency and highest efficiency available. For now, Gary thinks both arguments have merit.">InfiniBand keeps the high end</button>
  </div>
  <p class="de-article-poll__feedback" data-poll-feedback hidden></p>
</div>

<figure class="de-equal-weight">
  <p class="de-equal-weight__q">And are technical professionals prepared for a future where understanding</p>
  <div class="de-equal-weight__pans">
    <ul class="is-new">
      <li>GPUs</li>
      <li>AI workloads</li>
      <li>Data centre fabrics</li>
    </ul>
    <p class="de-equal-weight__eq"><b aria-hidden="true">=</b><span>becomes just as important as understanding</span></p>
    <ul class="is-familiar">
      <li>Monitoring tools</li>
      <li>Routing configuration</li>
      <li>Switching optimisation</li>
      <li>Firewall rules</li>
    </ul>
  </div>
  <p class="de-equal-weight__mark" aria-hidden="true">?</p>
</figure>

{{ discussion_box(page) }}

{{ related_reading(page) }}
