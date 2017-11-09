---
layout: post
title:  "Pug: Using variables to declare the class name"
date:   2017-11-08
---

In Pug, 

```
// Pug, wrong
- var myClassName = 'exciting_name'
div.=myClassName My dog is a Pug!
```

would compile to
```
<!-- HTML, wrong -->
<div> myClassName My dog is a Pug! </div>
```

instead of
```
<!-- HTML, correct -->
<div class='myClassName'> My dog is a Pug! </div>
```

Instead do
```
// Pug, correct
div(class=myClassName) My dog is a Pug!
```

