---
type: post
title: "performance.now() vs date.now()"
date: 2018-04-09
---

Condensed from [here](https://stackoverflow.com/questions/30795525/performance-now-vs-date-now).

In JavaScript, `performance.now()` is relative to page load,
while `Date.now()` is relative to Unix Epoch and dependent on system clock.

Since `performance.now()` is also more precise than `Date.now()`,
it is better to use it for measuring how long a function takes to run in the browser.



