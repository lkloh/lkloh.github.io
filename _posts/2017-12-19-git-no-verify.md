---
layout: post
title:  "Git no verify"
date:   2017-12-19
---

If you use a linter, but don't want to have to refactor all the old code
in a file to obey the new linting rules, commit the file like this:

```
git commit -m 'Will not refactor the entire file' --no-verify
```

So that the linter will let the file pass through the commit.

