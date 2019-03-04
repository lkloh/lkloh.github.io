---
type: post
title: "CSS to set default font"
date: 2019-02-07
---

Summarized from [here](https://stackoverflow.com/questions/18118530/using-css-to-set-default-font).

Given a template
```
<!-- html -->
<div class='container'>
  <div id='my-block'></div>
</div>
```
and a default css file, to set a default style for the div, do
```
<!-- CSS -->
.container {
  * {
    background: green;
    height: 100px;
    width: 100px;
  }
}
```
then `my-block` will have a green background and dimensions of 100 x 100 pixels.

To override the default, you can add another CSS selector like this:
```
<!-- CSS -->
.container {
  .my-block {
    background: green;
    height: 100px;
    width: 100px;
  }
}
```



