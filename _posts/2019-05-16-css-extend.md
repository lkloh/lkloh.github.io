---
type: post
title: "CSS extend"
date: 2019-05-16
---

Summarized from [here](https://css-tricks.com/the-extend-concept/).

`extend` allows one CSS selector to inherit styles from another.

For example,
```
.foo {
  color: red;
}
.bar {
  @extend .foo;
}
```
compiles to
```
.foo .bar {
  color: red;
}
```

Using `extend` is more efficient than using a `mixin` to do
```
@mixin redStyle {
  color: red;
}
.foo {
  @include redStyle;
}
.bar {
  @include redStyle;
}
```
as using `mixin`s compiles to
```
.foo {
  color: red;
}
.bar {
  color: red;
}

```


