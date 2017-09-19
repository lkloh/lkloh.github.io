---
layout: post
title:  "Javascript: Const, Let or Var?"
date:   2017-07-11 01:57:45 -0700
---

`const`.

[This article](https://medium.com/javascript-scene/javascript-es6-var-let-or-const-ba58b8dcde75) 
explains why.
Essentially,
`const` only allows one variable to be assigned to it,
so a variable cannot change in the program,
making it easier to understand what any one variable is for,
and thus better for long term maintainence.

`let` allows variable reassignment.
If you find yourself using `let` for any reason,
it probably means you need to do some refactoring to simplify things.

