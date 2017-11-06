---
layout: post
title:  "Django Operational Error 1054"
date:   2017-11-03
---

If you see this error in Django:
```
1054, Unknown column in field list
```

Is probably a change in the tables schema.
Can happen quite often if there's a bunch of people working on the same repo.
Run a migration to fix the issue.

