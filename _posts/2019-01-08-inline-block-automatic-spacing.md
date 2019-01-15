---
type: post
title: "Inline block automatic spacing"
date: 2019-01-08
---

Using inline-block can create a space around your blocks
even if you didn't add it there yourself.

For example, the code below will result in elements looking sort of like this:
```
 -------------------------------
|                               |
|  -------   -------   -------  |
| | child | | child | | child | |
|  -------   -------   -------  |
|                               |
 -------------------------------
```
With a gap between each child element, though none is specified.

```
<!-- html -->
<div class="parent">
  <div class="child">child</div>
  <div class="child">child</div>
  <div class="child">child</div>
</div>

<!-- CSS -->
.parent {
	background: green;
	display: block;
	padding: 5px;
}

.child {
	background: red;
	display: inline-block;
	padding: 5px;
}
```

This is because inline block elements [respect the whitespace in the markip](https://stackoverflow.com/questions/19038799/why-is-there-an-unexplainable-gap-between-these-inline-block-div-elements). 

To avoid the whitespace, one needs to eliminate whitespace between
the inline block elements, for example in this way to preserve
the formatting.

```
<!-- html -->
<div class="parent">
   <div class="child">child</div><!--
--><div class="child">child</div><!--
--><div class="child">child</div>
</div>

<!-- CSS -->
.parent {
	background: green;
	display: block;
	padding: 5px;
}

.child {
	background: red;
	display: inline-block;
	padding: 5px;
}
```
