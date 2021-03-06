---
type: post
title: "Do you need jQuery?"
date: 2018-07-09
---

JQuery was [built to make it easier to use JavaScript](https://www.w3schools.com/jquery/jquery_intro.asp),
during a [time when browsers were not standardized](https://hackernoon.com/you-truly-dont-need-jquery-5f2132b32dd1).

But now the trend seems to be to migrate away from it,
as there are now more tools to do the things jQuery was supposed to be used for.
See [here](http://youmightnotneedjquery.com/) for some of them.

So try to avoid using jQuery in new projects for the following reasons:
* Avoid having an additional dependency that needs to be periodically updated
* Avoid having extra code (the JQuery library) that your webapp needs to load
* Get faster performance by using the default JavaScript selectors

All this without losing any functionality but omitting JQuery.

