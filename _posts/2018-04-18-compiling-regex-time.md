---
type: post
title: "Regex compilation takes time"
date: 2018-04-18
---

Compiling a regex can slow performance in JavaScript, so its worth
storing the regex as a constant and calling it to avoid compiling it too often
if you use it in a function.

Thus, write
```js
const POSSIBLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
function isUSPhoneNumberOptimized(n) {
  return REGEX.test(n);
}
```

instead of

```js
function isUSPhoneNumber(n) {
  return /^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$/.test(n);
}
```

As a matter of fact, it takes about twice as long when compiling the regex
each time vs calling the already compiled regex in the function.
[Proof](https://github.com/lkloh/javascriptPlayground/blob/master/regexPerf.js).

