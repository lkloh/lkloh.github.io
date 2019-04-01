---
type: post
title: "Reference other functions in JSDoc using @see"
date: 2019-03-29
---

To reference another function in JSDoc, use [@see](http://usejsdoc.org/tags-see.html).

```js
/*
 * This function links to the @see {@link bar} function
 */
function foo() {
  bar();
  console.log(`foo`);
}

function bar() {
  console.log(`bar`);
}
```


