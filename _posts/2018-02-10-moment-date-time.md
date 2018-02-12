---
type: post
title: "Moment JS - getting the different between two libraries"
date: 2018-02-10
---

Given two dates
```js
var moment = require('moment');

var d1 = moment.utcnow();
var d2 = moment('2018-02-10T10:18:27Z').utc();
var diff = d1.diff(d2, 'seconds');

if (diff < 0) {
  console.log(`d1 is before d2`);
} else {
  console.log(`d2 is before d1`);
}
```


