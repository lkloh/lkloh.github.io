---
type: post
title: 'Whitespace in pug'
date: 2018-02-07
---

To write something like this in pug:
```
<!-- html -->
<div class="hello"> This is a link to <a href="https://www.google.com">Google</a>, a well known search engine </div>
```

you should do
```
// pug
.hello
  | This is a link to
  |
  a(href="https://www.google.com") Google,
  |
  | a well known search engine.
```

