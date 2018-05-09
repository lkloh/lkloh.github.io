---
type: post
title: "How many characters should there be in a line of code?"
date: 2018-04-15
---

## 80 characters

Pros
* Good rule of thumb - it makes Github reviews easier to read as most of the code
would fit onto one line.

Cons
* Too restrictive; for some verbose languages (e.g. JavaScript), it may
  force devs to linebreak at inconvenient places and in fact decrease readability.

## 100 characters

Pros
* Accomodates most professional code. Can fit comfortably in most modern monitors.

Cons
* What if you're using your laptop to debug an emergency issue in the middle of the night?

## 120 characters

Pros
* Flexible enough to accomodate most dev styles and languages. 
Sometimes when the indent has to be 4 characters and you use a verbose language,
even 100 characters is too short.

Cons
* Encourages people to write too much inlined code,
  that may be better broken up into a block to enhance understandability.

