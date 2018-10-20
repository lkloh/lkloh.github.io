---
type: post
title: "Avoiding special characters in urls"
date: 2018-10-13
---

$p€¢ial ¢ha®a¢t€®s in urls can cause [security vulnerabilities](https://perishablepress.com/stop-using-unsafe-characters-in-urls/), and thus need to be encoded in a url. 

They also make it difficult to give someone a url on a piece of paper when necessary.

To avoid having to deal with $p€¢ial ¢ha®a¢t€®s,
try to avoid the use of strings in a url slug where possible.
I was using a unique id + string in a url generator when I ran into the issue,
so I ended up refactoring things to that only the unique id (a number) as used as part of the url.
It also had a added benefit of shortening the url as we avoided using a string
that could be set by a user.

