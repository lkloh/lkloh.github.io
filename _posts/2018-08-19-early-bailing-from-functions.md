---
type: post
title: "Early bailing from functions"
date: 2018-08-19
---

If a function only does something if it fulfils a conditional:

```js
function update_state(params) {
  if (params.loaded) {
    this.helpers.update_state(pick(params, [`id`, `name`]));
  }
}
```
it is better to bail early if the conditional is not met,
as the `else` branch does nothing:


```js
function update_state(params) {
  if (params.loaded) return;
  this.helpers.update_state(pick(params, [`id`, `name`]));
}
```

In this way, you can also avoid heavily nested functions.
