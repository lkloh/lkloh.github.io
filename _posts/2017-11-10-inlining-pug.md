---
layout: post
title:  "Inlining Pug"
date:   2017-11-10
---

How to show a class?

```
// pug
- var showClass = true
.conditional_div(class=showClass ? 'awesomeClass': '')
```

compiles to

```
// html
<div class='conditional_div awesomeClass'></div>
```

and

```
// pug
- var showClass = false
.conditional_div(class=showClass ? 'awesomeClass': '')
```

compiles to

```
// html
<div class='conditional_div'></div>
```