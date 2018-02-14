---
type: post
title: "Converting a date to UTC time in MomentJS"
date: 2018-02-09
---

From [here](https://stackoverflow.com/questions/23299950/convert-date-to-utc-using-moment-js):

Timestamp in UTC (milliseconds)
```js
var utc_timestamp = moment.utc('2018-02-14 15:30:18').valueOf();
```

while to get the timestamp in local timezone:
```js
var local_timestamp = moment('2018-02-14 15:30:18').valueOf();
```

