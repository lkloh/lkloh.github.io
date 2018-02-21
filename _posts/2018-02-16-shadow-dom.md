---
type: post
title: 'Shadow Dom'
date: 2018-02-16
---

Making a shadow dom:
```
<!DOCTYPE html>
<html>
<head>
<script>
window.onload = function() {
  var root = document.getElementById('welcome_msg').createShadowRoot();
  root.textContent = 'Hi Shadow';
};
</script>
</head>

<body>
<div id='welcome_msg'>Welcome to my world</div>
</body>
</html>
```

Now when the HTML page is rendered in browsers that support shadowDom (Chrome is your best bet),
you see "Hi Shadow" rendered instead of "Welcome to my world",
and you open the div using the inspector, you see the DOM looks like
```
<html>
<head>...</head>
<body>
  <div id='welcome_msg'> == $0
    #shadow-root (open)
      "Hi Shadow"
    "Welcome to my world"
  </div>
</body>
</html>
```
Incidentally, if you type `$0` into the browser console, it returns
```
<div id='welcome_msg'>
  #shadow-root (open)
    "Hi Shadow"
  "Welcome to my world"
</div>
```
