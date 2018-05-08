---
type: post
title: "Test fixtures"
date: 2018-05-05
---

Test fixtures are a set of objects use to run tests that are constant,
so that test run in a stable environment and can be repeated.
More [here](https://github.com/junit-team/junit4/wiki/test-fixtures).
If the tests find a random bug, it is important to be able to reproduce the bug
as needed to fix it.

Randomness in tests should be [used sparingly](https://stackoverflow.com/questions/636353/is-it-a-bad-practice-to-randomly-generate-test-data) or in addition to repeatable tests,
never as a substitute for repeatable tests for "additional coverage of edge cases".

According to [Wikipedia](https://en.wikipedia.org/wiki/Test_fixture),
if you use randomness in a test fixture, its no longer a "test fixture"
as a key characteristic of a test fixture is that it is consistent.
Instead, you could call it "fuzz testing".

