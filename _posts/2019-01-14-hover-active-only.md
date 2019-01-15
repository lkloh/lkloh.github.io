---
type: post
title: "Making the disabled state on a button truly disabled"
date: 2019-01-14
---

Inspired by [this](https://stackoverflow.com/questions/11600687/hover-and-active-only-when-not-disabled).

```
<!-- CSS -->
button:hover {
  background: green;
}

button:active {
  background: blue;
}

button:disabled {
  background: grey;
}

<!-- HTML -->
<button>
```

In the above case, the button 
```
<button disabled=true>
```
still shows as `green` when hovering over it.

To make the `disabled` state truly disabled:

```
<!-- CSS -->
button:hover:not([disabled]) {
  background: green;
}

button:active:not([disabled]) {
  background: blue;
}

button:disabled {
  background: grey;
}

<!-- HTML -->
<button>
```

Now clicking or hovering on a disabled button still shows only the grey background.

