---
type: post
title: "In programming its always your fault?"
date: 2018-07-24
---

If something is wrong in a feature you shipped, > 99% of the time it's your fault.
Studies show that at least 95% of bugs are caused by devs,
not a third-party library or the hardware.
So if something went wrong, assume its your fault.
If you really can't find out what's wrong,
it may possibly be an error somewhere else,
as you can't assume anything.

Today I spend hours looking for a bug on code I deployed (I was testing on my dev environment),
only to realize that I couldn't reproduce the bug after rebasing on master.

