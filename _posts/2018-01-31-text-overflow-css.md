---
type: post
title: "Text overflow - ellipsis"
date: 2018-01-31
---

Given a box of this size:

```
 -------------------
|                   |
| Hello, World      |
|                   |
 -------------------
```

If text overflows the box:
```
 -------------------
|                   |
| Hello, San Francisco!
|                   |
 -------------------
```

One could truncate it using a variety of ways described [here](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow), such as using

```
// css
text-overflow: ellipsis
```

to get

```
 -------------------
|                   |
| Hello, San Fran...|
|                   |
 -------------------
```
to ensure the text is within the boundaries of its containing div.


