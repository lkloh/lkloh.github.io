---
type: post
title: "When copying code, save the copy changes in a commit"
date: 2018-09-30
---

When copying large chunks of code to a different file during a refactor,
save the copy changes in a commit for clarity and historical tracing,
so you reviewer doesn't think you wrote everything freshly in that diff
and feel the need to review it again.

Similarly, if you're the reviewer, check the commits carefully for hints
that something was copied (especially if you know that branch was for a refactor).

I sometimes tempted squash all my commits into one before submitting for review,
since a branch I work on for a long time can potentially have ~100 or more commits
if its a big feature.
