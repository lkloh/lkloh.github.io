---
type: post
title: "Freezing time in JavaScript"
date: 2018-02-20
---

When writing JavaScript tests on December 14, 2017,
if you check that the date should be December 14, 2017, the test will pass today,
but fail tomorrow and forevermore.

The way around this is to freeze the time by using `sinon.useFakeTimers` to keep the time
to December 14, 2017, and then unfreeze once the test is done.

```
var sinon = require('sinon');
var moment = require('moment');

var fakeDate = new Date(`2017-12-14T12:00-08:00`).getTime();
var clock = sinon.useFakeTimers(fakeDate);
new Date(); //=> return the fake Date 'Dec 14, 2017 at 12pm in UTC-08:00'

console.log(`time now: ${moment.utc()}`);

clock.restore();
new Date(); //=> will return the real time again (now)

console.log(`real time: ${moment.utc()}`);
```
