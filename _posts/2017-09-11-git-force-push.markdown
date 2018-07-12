---
layout: post
title:  "Git force push forces comments to disappear"
date:   2017-09-11
---

I've used `git --force push` to forcefully push commits to master
after rebasing with other people's changes.
Unfortunately this tends to make earlier comments disappear in Github.
There are certainly [ways to recover it](https://stackoverflow.com/questions/3973994/how-can-i-recover-from-an-erronous-git-push-f-origin-master),
but its really troublesome to have to dig into it.
I think I'll stick with saving comments I may want to go back and take a look by
taking a screenshot instead.

Edit (2018) - Comments don't actually disappear, they just become outdated. But they are still preserved in the pull request.
The one issue Git force push causes is that if someone was working off your branch as well,
the tracking will disappear. And they will get pissed off.
Though the solution is probably to avoid having two people branching off a dev branch
and instead branch off separately from master.
It just needs less communication, and thus less potential reasons for accidents to happen.
