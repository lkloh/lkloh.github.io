---
type: post
title: "Webpack dependency ordering matters"
date: 2018-07-16
---

Turns out the way you order your dependencies in the webpack configuration file matters.

```
// FILENAME: webpack.bundles.js
module.exports = {
  ...,
  'entry': [
    './childClass.js',
    './parentClass.js',
  ],
  ...,
}
```

This didn't work as the child class inherits from the parent class,
but the parent class was loaded _after_ the child class.
I spent hours wondering whether I did something wrong in the inheritance within `childClass.js`
before someone told me that it was likely an "order of loading" issue
because one of the errors I got said: `error superclass not found`.

```
// FILENAME: webpack.bundles.js
module.exports = {
  ...,
  'entry': [
    './parentClass.js',
    './childClass.js',
  ],
  ...,
}
```

