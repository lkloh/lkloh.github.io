---
type: post
title: "CSS containment"
date: 2019-01-16
---

Summarized from [here](https://developers.google.com/web/updates/2016/06/css-containment).

## What it does

Changing any part of the DOM can affect other parts,
so every time the DOM changes, all of the DOM needs to be recomputed for styling purposes.

Allows you to [limit the scope of the browser' styles and layout](https://developers.google.com/web/updates/2016/06/css-containment), helping to improve performance as some parts of the webapp do not need to be
recomputed when a change to the DOM is made.



## Example

Given a DOM like this
```
<!-- css -->
.container2 {
  left: 10px;
}
div {
  display: block;
}

<!-- html -->
<div id="container1">
  Section 1
</div>
<div id="container2">
  Section 2
</div>
<div id="container3">
  Section 3
</div>
```

and if you add a new element to one of the divs to get


Given a DOM like this
```
<!-- css -->
.container2 {
  left: 5px; // changed
}
div {
  display: block;
}

<!-- html -->
<div id="container1">
  Section 1
</div>
<div id="container2">
  Section 2
</div>
<div id="container3">
  Section 3
</div>
```

The entire DOM is in scope, so all the layouts and paint have to be calculated
again due to the change from `left:10px` to `left:5px`, causing a performance hit,

## Avoiding a performance hit with containment

Add `contain: layout` for the elements, so
nothing outside the element can affect its internal layout and vice versa.
So only `container2` needs to be checked again,
instead of all three.

```
<!-- css -->
.container2 {
  left: 5px; // changed
}
div {
  contain: layout;
  display: block;
}

<!-- html -->
<div id="container1">
  Section 1
</div>
<div id="container2">
  Section 2
</div>
<div id="container3">
  Section 3
</div>



