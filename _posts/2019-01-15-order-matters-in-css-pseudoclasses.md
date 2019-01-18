---
type: post
title: "Order matters in CSS pseudoclasses"
date: 2019-01-15
---

I've been asked to order CSS styles in alphabetical order,
so of course I tried this first:
```
<!-- styl file -->
button
  background white

  &:active
    background red

  &:hover
    background blue
```

Button turned blue once I moused over it, refused to change to red
when I tried clicking on it.

A bit of Googling [told me](https://www.w3schools.com/css/css_pseudo_classes.asp)
that the `:hover` state had to come 
before the `:active` state, probably because you need to
hover over a button before you can click on it.

