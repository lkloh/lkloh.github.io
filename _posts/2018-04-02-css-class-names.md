---
type: post
title: "CSS conditional class names"
date: 2018-04-02
---

Given a form like this

```
<!-- .pug file -->
.user_info(
  class={`text_in_green`: isStaff}
)
  .label#name user.name
  .label#birthday user.birthday
  .label#lastLogin user.lastLogin

<!-- .styl file -->
.user_info
  .label
    color grey

  &.highlight_in_green
    color green
```

the class name should be `is_staff` instead of `text_in_green`
as it should explain characteristics of information that describes what
members of the class have,
not the type of styling the class should have.


```
<!-- .pug file -->
.user_info(
  class={`is_staff`: isStaff}
)
  .label#name user.name
  .label#birthday user.birthday
  .label#lastLogin user.lastLogin

<!-- .styl file -->
.user_info
  .label
    color grey

  &.is_staff
    color green
```
