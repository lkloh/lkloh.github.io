---
layout: post
title:  "CSS styles best practices"
date:   2017-11-12
---

[Best practices](https://www.thoughtco.com/avoid-inline-styles-for-css-3466846): 
No inline styles, hard to maintain.
Separate stylesheet for styles.

## No

```
// html
<div styles="color:red; width: 80px; padding: 6px 12px;"><div>
```


## Yes

```
// css
.btn {
	color:red;
	width: 80px;
	padding: 6px 12px;
}

// html
<div class='btn'><div>
```
