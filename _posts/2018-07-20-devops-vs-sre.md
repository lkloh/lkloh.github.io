---
type: post
title: "Devops vs SRE"
date: 2018-07-20
---

[This post](https://cloudplatform.googleblog.com/2018/05/SRE-vs-DevOps-competing-standards-or-close-friends.html)
explains that DevOps is a culture that encourages development practices that minimize production issues,
while SRE (Site Reliability Engineering) does the work required to succeed at DevOps.
The explanation for this is `class SRE implements DevOps`.

## Availability targets

To succeed at DevOps practices, SRE decides on a system's availability targets,
measures it, and decides what to do when availability falls short.

To do so, SRE had to talk to individual contributors up to VPs and executives
to come up with metrics:
* Service Level Indicators (SLIs):
  metrics over time converted to a rate (e.g. request latency, failures per request) that are subject to a threshold
* Service Level Objectives (SLOs):
  targets for cumulative success of SLIs over a window of time (e.g. "this quarter")

Also there are Service Level Agreements (SLAs) that are promises by service providers to
consumers about availability of a service,
and the consequences of failing to deliver on the level of service,
which are defined and negotiated by account executive for customers.

## Risk and error budgets

SREs need to balance availability and feature development.

Availability cannot be too high (such as 99.9999999%),
or no feature work would ever get done in a reasonable amount of time,
as new features tend to end up causing bugs.

Also, there is no point extending an extreme amount of effort having 99.9999999% availability,
as customer's likely won't even get that much more benefit over a 99.9% availability
as other components out of your control such as ISPs and WiFi will also affect the quality of their service.

Thus, when shipping many new features, service owners should get less stringent SLOs 
to continue shipping even when bugs occur.
When focusing on reliability, a high SLO should be choser in lieu of slowing shipping.

## Toil budgets 

"Toil" is what occurs when a human being needs to manually touch a production system during normal operations.
It is work that manual, repetitive, and does not have long-term value,
that tends to scale linearly with the size of the service.

At Google, SRE's ideally spend 50% of their time on engineering projects and the other 50% on toil,
to strike a balance between minimizing toil and accepting that it does not make sense to automate everything.

## Customer reliability engineering

Teaching SRE practices to customers, 
so that you spend less time on fixing issues that come up when you have millions of customers.
That means more time for you to innovate and less time fighting fires.







