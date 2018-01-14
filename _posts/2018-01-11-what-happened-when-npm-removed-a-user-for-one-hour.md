---
layout: post
title:  "What happened when NPM removed a user for one hour"
date:   2018-01-11
---

On Jan 6, 2018, [NPM removed a legitimate user, `floatdrop`, for an hour](http://blog.npmjs.org/post/169582189317/incident-report-npm-inc-operations-incident-of),
and broke lots of people's code.

NPM automatically checks every new package published to ensure it is not spam.
If the system flags a new package as spam, NPM employees can opt
to remove the user and any packages the user published to NPM.

On Jan 6, 2018, a package was published with spam content,
along with some code from a package that the legitimate user `floatdrop` had published.
An NPM employee deleted all the content that `floatdrop` had written
as part of the anti-spam actions to be taken upon receiving a spam report. 

Right after `floatdrop` was deleted, some other NPM users published 
new packages that used the names of some of the delete packages authored by `floatdrop`. 

And soon afterwards, NPM realised that `floatdrop` was not actually a spammer
and restored their account and packages quickly, as `floatdrop` had
published several packages that were used as dependencies in the NPM ecosystem. 

NPM also had to examine the packages published between `floatdrop`'s deletion
and restoration that used the names of `floatdrop`'s packages.
Luckily non of those packages were malicious.
However this could easily have turned into a security issue as 
a malicious user could have published malware under the name of `floatdrop`'s
widely used packages and caused it to be downloaded and executed by users 
of `floatdrop`'s work.

Subsequently, NPM decided that the main takeaway is that after
any NPM package is deleted, new packages may not be published under 
that deleted package's name for 24 hours,
to allow some time for the impact of deleting a package to become clearer,
and also to prevent bad actors from publishing malware under the name of
a useful package that was delete. 


