---
type: post
title: "Debounce vs Throttle"
date: 2018-09-11
---

Summarized from [here](https://nolanlawson.com/2018/09/01/a-tour-of-javascript-timers-on-the-web/).
Both used to limit the frequency at which a function can fire.

## Debounce

Used to group multiple sequential calls into a single call.

## Throttle

Only let a function execute at most once every X seconds.

# Main difference with debounce and throttle

`throttle` ensures the function will be
executed regularly every X seconds, while `debounce` does not.

Thus you should use `throttle` for a callback that fires on a scrolling event,
to ensure the user gets regular feedback that their scrolling actions are workin,
while `debounce` is not good for scrolling as the callback only
executes after several scroll events have finished, so the user might get frustrated
as their scrolling actions don't seem to have any effect for a while.

