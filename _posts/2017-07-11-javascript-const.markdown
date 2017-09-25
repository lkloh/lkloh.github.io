---
layout: post
title:  "Javascript: Const, Let or Var?"
date:   2017-07-11
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
You might want to use it to declare a loop iterator.
It is also scoped within the block
Outside of that, if you use `let` instead of `const`
it probably means you need to do some refactoring.

`var` should be depreciated. It causes terrible scoping confusion
and doesn't communicate anything to the user about how a variable declared
with `var` is going to be used.

