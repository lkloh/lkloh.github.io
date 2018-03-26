---
type: post
title: HTML entities
date: 2018-03-25
---

Used to replace reserved characters in HTML.

Reserved characters in HTML are ampersand (&amp;) 
and left angle bracket (&lt;), that cannot appear literally,
but instead be written using their HTML entities `&amp` and `&lt`.

Some Unicode characters that are commonly used also have reserved characters.
A full list can be found [here](https://unicode-table.com).
Some common characters such as symbols for money have reserve characters 
(e.g. Pound (&pound;) has `&pound`) for ease of memorization.

On the other hand, a less commonly used symbol such as &#1421; 
has not HTML entity reference; its decimal representation is `&#1421`
and its hex representation is `U+058D`.

Unfortunately, browsers do not support all existing entity names,
so best to use hex or decimal names unless its for something really common
like &amp;.
