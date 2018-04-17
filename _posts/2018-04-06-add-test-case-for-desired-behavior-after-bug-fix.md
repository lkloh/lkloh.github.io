---
type: post
title: "Add a test case for desired behavior after a bug has been fixed"
date: 2018-04-06
---

If you've fixed the root cause for a bug that was reported...
hopefully by someone doing QA, most likely by an upset customer,
the best practice is to add a unit test verifying that the expected behavior occurs.

Oh and of course take a close look before and after deploying.
Meaning verify the fix actually worked in production.

Once I had to revert a fix I made because it broke something else.
There wasn't enough test coverage on that project, and the issue that broke was subtle enough that
testing it manually with an impartial third party didn't catch it. 

