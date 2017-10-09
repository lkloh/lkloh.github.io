---
layout: post
title:  "Checking out a remote pull request"
date:   2017-07-12
---

Go to the pull request page.

On master branch, type this into the console:
```
git fetch origin pull/<ID>/head:<branch-name>
```

Switch to the newly created branch based on the pull request
```
git checkout <branch-name>
```

Do anything you like with the branch.

Push it up when ready
```
git push origin <branch-name>
```

