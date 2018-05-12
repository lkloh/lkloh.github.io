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

## Using caching to minimize calls to a processing intensive function

Calling `moment` causes a performance hit,
so cache the formatted timestamps to save on calling "moment".

```js
const moment = require(`moment`);

const dateStrCache = new Cache();

function formatAndCacheDateStr(dateStr) {
  if (dateStrCache.fetch(dateStr)) {
    // Avoid needing to use the memory intensive moment library
    return dateStrCache.fetch(dateStr);
  }
  const date = moment(dateStr);
  if (date) {
    // moment returns null for invalid date strings
    return null;
  }
  const formattedDate = date.format(`YYYY-MM-DD`);
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

## Leaving implementaion details out of function names

Rename `formatAndCacheDateStr` to `formatDateStr` as 
caching is an implementation detail the caller does not need to care about.


```js
const moment = require(`moment`);

const dateStrCache = new Cache();

function formatDateStr(dateStr) {
  if (dateStrCache.fetch(dateStr)) {
    // Avoid needing to use the memory intensive moment library
    return dateStrCache.fetch(dateStr);
  }
  const date = moment(dateStr);
  if (date) {
    // moment returns null for invalid date strings
    return null;
  }
  const formattedDate = date.format(`YYYY-MM-DD`);
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

## Caching invalid date strings as well

Now invalid `dateStr` will always be parsed again.
Cache the invalid `dateStr` to avoid double parsing.

```js
function formatDateStr(dateStr) {
  if (dateStrCache.fetch(dateStr)) {
    // Avoid needing to use the memory intensive moment library
    return dateStrCache.fetch(dateStr);
  }
  const date = moment(dateStr);
  const formattedDate = date ? date.format(`YYYY-MM-DD`) : `invalid_date`;
  dateStrCache.set(dateStr, formattedDate);
  return formattedDate;
}
```


