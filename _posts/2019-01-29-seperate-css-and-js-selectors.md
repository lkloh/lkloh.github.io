---
type: post
title: "Seperate CSS and JS selectors"
date: 2019-01-29
---

What's wrong with doing this?

```
<!-- html -->
<div class="block"></div>

<!-- css -->
.block {
  background: yellow;
  display: block;
}

<!-- js -->
document.querySelector(`.block`).hide();
```

You are using the same `.block` selector for CSS styling
and JavaScript functionality.

If you ever want to change the designs by changing the `.block` class,
you need to ensure the behavior did not break due to the shared selector
used by JavaScript.

If you want to rename the JavaScript selector to better
reflect some new or changed behavior,
you'll need to go update the CSS file as well, which is annoying.

Read more [here](https://coderwall.com/p/qktuzw/decouple-javascript-classes-from-css-ones-by-using-prefix) and [here](https://css-tricks.com/stop-using-css-selectors-non-css/).


