---
type: post
title: "JavaScript:void(0) evaluates an expression and returns UNDEFINED"
date: 2019-06-11
---

Sometimes you see something like this:
```js
<a href="javascript:void(0);" ondblclick="alert('YOLO')">
  Double click
</a>
```

To prevent the page from refreshing when you click the first time,
we added `javascript:void(0)` to `href`.

I first found out about this when writing
```js
const maybeLinkOrUndefined = getRandomLink();
<a href="${maybeLinkOrUndefined}">
  Click me and be surprised!
</a>
```
