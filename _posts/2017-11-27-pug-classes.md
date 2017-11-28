---
layout: post
title:  "Pug classes"
date:   2017-11-27
---

I was working on a Pug template to highlight in input field's border in red
if the user entered an invalid value, and did it like this:

```
- var hasError = errors.length > 0
input(class=hasError ? 'error' : '')
```

But actually there is a [better way](https://pugjs.org/language/attributes.html#class-attributes):

```
input(class={'error': errors.length > 0})
```


