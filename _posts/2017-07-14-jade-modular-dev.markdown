---
layout: post
title:  "Modular Development in Jade"
date:   2017-07-14 04:42:23 -0700
---

[Jade](https://webapplog.com/jade/) is a template language,
meaning it is halfway between something like a macro
and a full programming language like JavaScript.
It's useful in web apps to generate dynamic pages with a single template.

Jade allows you to add JavaScript code to a Jade Template,
but it's best to place the actual JavaScript somewhere else in a `.js` file
and call a helper from the template. Mixing two languages should be done sparingly.

Easier said than done, of course, 
especially when developing a new feature.