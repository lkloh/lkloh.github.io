---
type: post
title: 'Shadow DOM encapsulation'
date: 2018-02-21
---

Shadow DOM are used to encapsulate code so that CSS selectors and scripts
don't mess up certain elements on the page.
Essentially, it prevents needing to use `border: 1px solid blue !important` everywhere.

One way to encapsulate things is to use and iFrame, 
but that has all sorts of baggage included.
The Shadow DOM is used to set a boundary between the host and the shadow DOM
that cannot be crossed in either way.

Example:
```
<html>
<head>
<script>
  window.onload = function() {
    var root = document.querySelector('#shadow_host').createShadowRoot();
    root.innerHTML = '<h3>Shadow Header not affected by normal styles.</h3>';
  };
</script>

<style>
  h3 {
    color: red;
  }
</style>
</head>

<body>
  <div id='shadow_host'>
    <h3> Red header <h3>
  </div>
  <div id='normal'>
    <h3> Normal </h3>
  </div>
</body>
</html>
```

You will node that the Shadow DOM's h3 element is not affected by the CSS selector
changing to color to red.


