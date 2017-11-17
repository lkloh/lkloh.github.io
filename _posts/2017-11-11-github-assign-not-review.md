---
layout: post
title:  "Github assign not review"
date:   2017-11-11
---

Github allows `assignees` and `reviewers`.

Seems that it is better to add people as `assignees` instead of `reviewers` 
(even if you want them to review your pull request),
since only `assignees` will automatically be notified of updates by Github.

Apparently its because `assignees` have a looser requirement
(assigned to review code/ fix an issue/ be kept in the loop as project lead),
while `reviewer` is just meant to ask someone to review code.

Thus it may be more critical for an `assignee` to get updates.
For example, by assigning someone on a large open source project to an issue,
they could get notifications on an issue to see how many people are being affected by it,
so they can decide whether to prioritize a bug fix.

While a `reviewer` is expected to be actively reviewing code
and thus keep to make himself in the loop of what is going on
at all times, so notifications are not sent so often
as it is assumed they are unnecessary.


