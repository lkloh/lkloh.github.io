---
type: post
title: "Documenting callbacks in JSDoc"
date: 2018-08-21
---

There are [several recommended ways](https://stackoverflow.com/questions/24214962/whats-the-proper-way-to-document-callbacks-with-jsdoc)
to document callbackds in JSDoc, but it seems the general consensus is to use the @callback
tag like this:

```js
/**
 * Callback for manipulating an integer
 * @callback manipulateCallback
 * @param {int} sum - integer to manipulate
 */

/**
 * Manipuate two numbers
 * @param {number} x - an integer
 * @param {number} y - an integer
 * @param {manipulateCallback} callback - callback taking in an integer and returning another integer
 * @return result of the callback taking the sum of x and y and manipulating it
 */
function manipulateInts(x, y, callback) {
  return callback(x + y);
}
```
