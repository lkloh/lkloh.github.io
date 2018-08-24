---
type: post
title: "Backbone - pass silent:true when updating models"
date: 2018-08-16
---

Summarized from [here](https://eric.blog/2014/10/08/update-backbone-model-with-no-change-events/).

When updating a backbone model, you want to do

```js
model.set({attribute: value});
```

By this triggers a change event on every changed attribute by default.
To avoid triggering unnecessary change events, write

```js
model.set({attribute: value}, {silent: true});
```
