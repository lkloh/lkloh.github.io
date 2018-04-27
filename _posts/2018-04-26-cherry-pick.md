---
type: post
title: "Cherry pick"
date: 2018-04-26
---

I was working on a code base on `branch_lkloh`.
`branch_lkloh` has these commits:

```
// branch_lkloh

commit-2018-04-15T17:00:00
author: lkloh

commit-2018-04-14T13:00:00
author: lkloh
```

Meanwhile, many other people where doing things to `master` while I was working on `branch_lkloh`.

```
// branch master

commit-2018-04-15T16:00:00
author: alice

commit-2018-04-11T12:00:00
author: bob

commit-2018-04-10T09:00:00
author: charlie
```

And then I rebased and somehow ended up with this mess:
```
// branch_lkloh

commit-2018-04-15T17:00:00
author: lkloh

commit-2018-04-15T16:00:00
author: alice

commit-2018-04-14T13:00:00
author: lkloh

commit-2018-04-11T12:00:00
author: bob

commit-2018-04-10T09:00:00
author: charlie
```

To fix this locally on my machine, I checked out another branch from master:
```
// branch_lkloh_diff

commit-2018-04-15T16:00:00
author: alice

commit-2018-04-11T12:00:00
author: bob

commit-2018-04-10T09:00:00
author: charlie
```

and cherry picked my commits on `branch_lkloh` in this order:

```
git cherry-pick commit-2018-04-14T13:00:00
author: lkloh
```

and then

```
git cherry-pick commit-2018-04-14T13:00:00
author: lkloh
```

Now `branch_lkloh_diff` looks like this:
```
// branch_lkloh

commit-2018-04-15T17:00:00
author: lkloh

commit-2018-04-14T13:00:00
author: lkloh

commit-2018-04-15T16:00:00
author: alice

commit-2018-04-11T12:00:00
author: bob

commit-2018-04-10T09:00:00
author: charlie
```

And I could squash my two commits and only get the changes I made,
so it is easier to get them reviewed.

Figured it out by reading [this article](http://technosophos.com/2009/12/04/git-cherry-picking-move-small-code-patches-across-branches.html).


