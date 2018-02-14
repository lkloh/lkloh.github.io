---
type: post
title: 'Whitespace in pug'
date: 2018-02-07
---

To write something like this in pug:
```
<!-- html -->
<div class="hello"> This is a link to <a href="https://www.google.com" target='_blank'>Google</a>, a well known search engine </div>
```

you should do
```
// pug
.hello
  | This is a link to
  |
  a(
    href="https://www.google.com"
    target="_blank"
  ) Google,
  |
  | a well known search engine.
```
Incidentally, setting `target="_blank"` will open the link in a new tab or page, depending on browser settings.

