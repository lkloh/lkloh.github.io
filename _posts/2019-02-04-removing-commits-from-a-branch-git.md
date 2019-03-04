---
type: post
title: "Removing commits from a branch"
date: 2019-02-04
---

I had a branch `dev_branch` whose git log looked similar to this:
```
commit 76e69f69d5bc6394d2d6413543a18199fc77ad99
Author: LK Loh <lkloh2410@gmail.com>
Date:   Sun Mar 3 17:29:49 2019 -0800

    aligning items vertically

commit 58680ad20cc5954f1091c6c6425594e80fd19691
Author: LK Loh <lkloh2410@gmail.com>
Date:   Sun Mar 3 17:15:02 2019 -0800

    handling exceptions

commit b7d12bfdb901fd53448d2b873ab32b8f8b5ffcf6
Author: LK Loh <lkloh2410@gmail.com>
Date:   Sun Mar 3 16:43:20 2019 -0800

    css default font

commit 2a95c3c30489657aab67448bde86365f152159f2
Author: LK Loh <lkloh2410@gmail.com>
Date:   Sun Mar 3 16:24:36 2019 -0800

    many to one django

...
```

and I really wanted to get rid of 
```
commit 58680ad20cc5954f1091c6c6425594e80fd19691
Author: LK Loh <lkloh2410@gmail.com>
Date:   Sun Mar 3 17:15:02 2019 -0800

    handling exceptions
```

To do so, I did an interactive rebase
```
git rebase -i 2a95c3c30489657aab67448bde86365f152159f2^
```

which opend an editor to show a list of commits.

```
pick b7d12bf css default font
pick 58680ad handling exceptions
pick 76e69f6 aligning items vertically
```

I deleted the second line and the editor now looked like this:
```
pick b7d12bf css default font
pick 76e69f6 aligning items vertically
```
I saved it, did this:
```
git rebase --continue
```
and then forced pushed again.
```
git push -f origin dev_branch
```

Summarized from [here](https://stackoverflow.com/questions/3293531/how-to-permanently-remove-few-commits-from-remote-branch).

