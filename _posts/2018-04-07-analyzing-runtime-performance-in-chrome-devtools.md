---
type: post
title: "How to find out which functions are causing a performance hit at runtime"
date: 2018-04-07
---

[Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools),
in particular the [Performance](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference)
section.
Hitting the "Record" button lets you record what happens when you perform a certain action in the webapp
(e.g. hitting the "buy") button,
and profiles how long each function that was called took.
Now you know exactly which functions need to be optimized.

