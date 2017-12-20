---
layout: post
title:  "Hiding stuff with CSS"
date:   2017-12-18
---

I was hiding something in a Jade template like this:

```
// jade
.element-container
  .element-main(class={'show': showElement}) The element

// css
.element-main
  display none

  &.show
    display block
```

where `showElement` is a conditional statement variable.

Instead we should do this:

```
// jade
.element-container
  if showElement
    .element-main The element

// css
.element-main
  display none

  &.show
    display block
```

for readability and so that we don't have to worry about potential exceptions
and timeouts in the JavaScript code that sets `showElement`.

