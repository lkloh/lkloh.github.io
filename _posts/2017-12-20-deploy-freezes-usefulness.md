---
layout: post
title:  "Deploy freezes - debate"
date:   2017-12-20
---

Deploy freezes 
[This article](https://www.xaprb.com/blog/2014/11/29/code-freezes-dont-prevent-outages/) 
argues that deploy freezes are bad because
* Stuff will still break anyway
* Lost productivity as people can't deploy stuff. Once they get back to work,
there are more dependencies because everyone is deploying stuff at the same time,
and people have to rebase on top of each others code - and that takes time
because something is going to be a breaking change.
If the end, less work got done due to the freeze, which did not even
help prevent the code from breaking because your users will still be
using your app while the freeze is in place.


Commenters stated it is still worth it before a holiday season,
so that developers prioritize getting large features out before the freeze to mitigate risk.
It also helps prevent burnout - devs get to wind down before the holiday season
instead of rushing to get stuff done,
and potentially worrying about whether their deploy causes any issues
while on vacation.

Of course people may rush to deploy stuff before the freeze 
and end up not testing stuff as well as they should

Personally I think a deploy freeze against major features should be
implemented before a long holiday,
but fixing small bugs as they pop up should be saidf to be ok over the break.
