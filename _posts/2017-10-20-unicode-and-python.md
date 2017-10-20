---
layout: post
title:  "Unicode and Python"
date:   2017-10-20
---

This information is available at [Python's official docs](https://docs.python.org/2.7/howto/unicode.html), but lots of programmers probably didn't read it that closely.
Including me, until now.

Python's default encoding is ASCII.

How Python converts unicode code points ("characters") to ASCII: 
* Code point < 128: each byte is the same as the value of the code point
* Code point >= 128: Raise a `UnicodeEncodeError`

# Example gotcha with unicode encodings

In which I stole the unicode string from 
[here](https://stackoverflow.com/questions/6048085/writing-unicode-text-to-a-text-file).

Because Python functions use ASCII encodings by default,
when writing a unicode string to a file in Python
one must specify the encoding.
Otherwise, you will get an error if any of the code points
of the unicode strings are >128.

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def example_unicode_encode_error():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
	print 'type: %s' % type(unicode_str)

	file.write(unicode_str)

	file.close()

def why_unicode_encode_errors_are_hard_to_catch():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Hello world'
	print 'type: %s' % type(unicode_str)

	file.write(unicode_str)

	file.close()

def example_unicode_encode_correct():
	file = open('unicode_demo.txt', 'w')

	unicode_str = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
	print 'type: %s' % type(unicode_str)

	ascii_str = unicode_str.encode("utf-8")

	file.write(ascii_str)

	file.close()

if __name__ == '__main__':
	example_unicode_encode_correct()
	why_unicode_encode_errors_are_hard_to_catch()
	example_unicode_encode_error()
```

