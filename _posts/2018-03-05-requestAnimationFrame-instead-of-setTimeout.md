---
type: post
title: "requestAnimationFrame instead of setTimeout"
date: 2018-03-05
---

`setTimeout` can be used for animations, but does not care about what else is happening in
the browser. For example, if the browser is hidden and the user is doing something else,
the animations are still running and using CPU when it does not need to.

Also, `setTimeout` does not update the screen efficiently.
For example, when several elements are animated, 
the screen must be repainted whenever any one element is updated, which drains resources unnecessarily.

`requestAnimationFrame` uses less CPU by only updating when the system resources
are not being overloaded, so it optimizes performance by taking into account the surroundings,
instead of naively updating things are regular time intervals like `setTimeout` does.

Read more [here](http://creativejs.com/resources/requestanimationframe/index.html).

