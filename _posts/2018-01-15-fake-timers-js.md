---
type: post
title: "Fake timeers in JavaScript"
date: 2018-01-15
---

Summarized from [here](http://sinonjs.org/releases/v1.17.7/fake-timers/).

Fake timers overwrite functions such as `setTimeout` to make it easier
to test (JavaScript) code. You can get it [here](http://sinonjs.org/).
This allows you to test code the needs a few seconds delay in unit tests
without _actually_ waiting that long.
Similar to what [freezegun](https://github.com/spulec/freezegun) does really.

