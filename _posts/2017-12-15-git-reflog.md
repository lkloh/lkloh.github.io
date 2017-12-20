---
layout: post
title:  "Git reflog"
date:   2017-12-15
---

If many people are working on a git repo,
and you accidentally pull master into your branch,
you may see somthing like this when you do a `git log`:

```
commit 727367e8e7faf7bf619ea2f57512653ab27c475f
Author: charlie <charlie@gmail.com>
Date:   Tue Dec 19 21:16:49 2017 -0800

    Linting

commit 214f5e3b97ff277d66abad38039f31a088502dd2
Author: bob <bob@gmail.com>
Date:   Mon Dec 18 18:22:08 2017 -0800

    Edit

commit 59744c0bda64d0185be1adaab4a5ee77adb25a33
Author: me <me@gmail.com>
Date:   Mon Dec 18 17:01:22 2017 -0800

commit c3c248263ec70981079f00d72d577a26dda2d80e
Author: Alice <alice@gmail.com>
Date:   Mon Dec 18 16:08:38 2017 -0800

    The bright side

commit 59744c0bda64d0185be1adaab4a5ee77adb25a33
Author: me <me@gmail.com>
Date:   Mon Dec 18 15:01:22 2017 -0800
	
	Reset

commit d3c248263ec60981079f00d72d577a26dda2d80e
Author: Alice <alice@gmail.com>
Date:   Mon Dec 18 16:08:38 2017 -0800

    More tests
```

And it looks like your commits are all merged with other peoples and you're messed up your pull request.

```
git reflog
```

Lets you find the commit to go back to before you pull form master.


