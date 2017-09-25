---
layout: post
title:  "Code design best practices"
date:   2017-08-13
---

Things that are obviously good to do,
but harder to implement in practice.

* If anything is used twice, see if there's a way to refactor it into a common function.
	That will make it easier to avoid tweaking things if the code diverges.
* Functions that are called multiple times should try to be pure functions,
	those used only once can then easily use those pure functions. 
* If something is potentially reusable in more than once place,
	even if you are only using it once now,
	see if you can pull it out to a more accessible location
	where it is more reusable.
* If you need something else someone is working on that has not been merged it,
	you can always copy their code if its not too long,
	so you don't get blocked on it.
