---
type: post
title: "How does regex work?"
date: 2018-04-18
---

## UNIX: optimizing a regex's equivalent finite automaton

A regex has an equivalent finite automaton which is optimized during compilation.
How exactly this is done is the subject of most compiler classes.

## Modern programming languages (e.g. Python): recursive backtracking

The regex is compiled into a tree representing its subchunks.
One reason modern languages do things this way is to enable backreferences,
which cannot be represented in finite automata.

## When should regex be used?

When searching for complex patterns, regex are usually faster.
If you're looking for a really trivial one-off match, 
writing your own basic algorithm may be better,
as the regex engine may initialize structures that are not needed
to solve the trivial matching problem.

But in general, you should use a regex, as it offers a language agnostic
way to express a pattern you want.

Thanks [Stack Overflow!](https://softwareengineering.stackexchange.com/questions/122440/how-do-regular-expressions-actually-work)



