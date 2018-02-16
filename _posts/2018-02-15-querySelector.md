---
type: post
title: 'querySelector'
date: 2018-02-15
---

`querySelector` lets you select the first element in the DOM that matches a particular 
CSS selector for the element.

For example, given a DOM like this:
```
<div class='example'>
  <div id='name'></div>
  <div id='email'></div>
</div>
```

You can select `<div id='name'></div>` by doing
`var nameDiv = document.querySelector('#name')`.
