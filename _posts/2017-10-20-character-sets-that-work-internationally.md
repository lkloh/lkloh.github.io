---
layout: post
title:  "Characters sets that work internationally"
date:   2017-10-20
---

This [article](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) is from 2003 but is still relevant,
as people still make the same mistakes about non-English characters.
He explains how to avoid basic mistakes, such as assuming everyone speaks only English.
Here is a summary of the key points.

## Making character sets that work internationally

* ASCII - Works if everyone uses only English.
Uses 4 bits to encode characters, 
and rpresents characters using a number between 32 - 127.
This means two characters can be represented in a byte.
* Eventually people realized that by using the entire byte
	to store a character, they could store more than english characters.
	For example, the Chinese languages has thousands of characters.
* Unicode as developed to create a single character set that could
	include all widely used characters on Earth. 
	It uses 2 bytes to store (16 bits), so that is 65536 possible characters.


## How unicode works

A string 
```Hello
``` 
in unicode corresponds to the codepoints
```
U+0048 U+0065 U+006C U+006C U+006F
```

## UTF-8: Conservation of bits

A way to store a string of Unicode code points 
in memory using 8 bit bytes.

* Code points from 0-127 stored in a one byte
* Code points < 128 stored using 2 bytes, up to 6 bytes

Thus English looks exactly the same in UTF-8 as in ASCII.

There are other encodings of Unicode if you want to save bits
or use more, but they aren't that widely uses due to 
excessive waste or excessive complexity.

# A string's encoding must be specified

Due to globalization, you cannot assume all strings are in ASCII.

## Sending pages to a web serve from different countries

Because all encodings are identical from 32 - 127, 
a webserver can figure out how to decode a page it gets
by looking at the Content-Type header.
```
<html>
<head>
<meta http-equiv=“Content-Type” content=“text/html; charset=utf-8”>

```

If Content-Type header is not specified,
browser will guess the encoding used by character frequency analysis.























