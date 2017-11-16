---
layout: post
title:  "CSS Flex Box"
date:   2017-11-14
---

CSS Flex box is useful for [accomodating different screen sizes and display devices](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Using_CSS_flexible_boxes).
They are popular now as they make it easier to position things inside a parent div.
It even makes it quite easy to center a div:

```
// html
<div class='parent'>
	<div class='child'></div>
</div>

// less
.parent {
	align-items: center;
	background: red;
	display: flex;
	height: 100px;
	justify-content: center;
	width: 100px;
	
	.child {
		background: blue;
		display: block;
		height: 50px;
		width: 50px;
	}
}
```

This actually produces this:
```
 -------------
|   parent    |
|   -------   |
|  |       |  |
|  | child |  |
|  |       |  |
|   -------   |
|             |
 -------------
```

