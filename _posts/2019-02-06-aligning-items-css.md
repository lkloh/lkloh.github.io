---
type: post
title: "Aligning items in CSS"
date: 2019-02-06
---

`align-items` defines how flex items are laid out vertically.
I've found it useful in this scenario:

```
<! -- jade file -->
.row-of-text
  .text He said that he wanted to buy 
  .input.number_of_fruits(type='text')
  .text fruits.
```

and I want the result to look like this:
```
                               -----
He said that he wanted to buy |  5  | fruits.
                               -----
```
with the text box centered.

I used
```
<!-- css -->
.row-of-text
  .number_of_fruits
    align-items center
```
to achieve that.


