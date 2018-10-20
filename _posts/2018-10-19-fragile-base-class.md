---
type: post
title: "Fragile Base Class"
date: 2018-10-19
---

The [Fragile Base Class](https://en.wikipedia.org/wiki/Fragile_base_class)
occurs in OOP languages as base classes are 'fragile'
as modifications made to them can cause their derived classes to malfunction.

So when making any changes to a base class at all,
your first question should be: "Can I avoid changing the base class"?

Sometimes its unavoidable if you're dealing with a legacy code base.

Sometimes, you just need to find another way,
perhaps by using [function composition](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-function-composition-20dfb109a1a0)
instead, which is immune to the fragile base class problem.


