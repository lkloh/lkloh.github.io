---
type: post
title: "Caching moment"
date: 2018-05-09
---

I was processing lots of data and had to parse it

```js
const hugeArray = [
  `2018-04-14T00:01:00Z`: 2,
  `2018-04-14T00:01:00Z`: 8,
  `2018-04-14T00:01:00Z`: 7,
  `2018-04-14T00:02:00Z`: 11,
  `2018-04-14T00:02:00Z`: 54,
  `2018-04-14T00:02:00Z`: 4,
  ...
];

function processRow(arr) {
  return arr.map(([dateStr, value]) => {
    const formattedDate = moment(dateStr).format(`YYYY-MM-DD`);
    return [formattedDate, value];
  });
}
```

That took a long time to process a huge array of data.
To fix this, one thing to try is:
```js
const moment = require(`moment`);

const dateStrCache = new Cache();

function formatAndCacheDateStr(dateStr) {
  if (dateStrCache.fetch(dateStr)) {
    // Avoid needing to use the memory intensive moment library
    return dateStrCache.fetch(dateStr);
  }
  const formattedDate = moment(dateStr).format(`YYYY-MM-DD`);
  dateStrCache.set(dateStr, formattedDate);
  return formattedDate;
}

function processRow(arr) {
  return arr.map(([dateStr, val]) => {
    const formattedDate = formatAndCacheDateStr(dateStr);
    return [formattedDate, value];
  });
}
```

One more thing: rename `formatAndCacheDateStr` to `formatDateStr` as 
caching is an implementation detail the caller does not need to care about.


```js
const moment = require(`moment`);

const dateStrCache = new Cache();

function formatDateStr(dateStr) {
  if (dateStrCache.fetch(dateStr)) {
    // Avoid needing to use the memory intensive moment library
    return dateStrCache.fetch(dateStr);
  }
  const formattedDate = moment(dateStr).format(`YYYY-MM-DD`);
  dateStrCache.set(dateStr, formattedDate);
  return formattedDate;
}

function processRow(arr) {
  return arr.map(([dateStr, val]) => {
    const formattedDate = formatDateStr(dateStr);
    return [formattedDate, value];
  });
}
```

