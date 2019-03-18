---
type: post
title: "Why you should avoid Moment.js and alternatives"
date: 2019-03-13
---

Summarized from [here](https://inventi.studio/en/blog/why-you-shouldnt-use-moment-js).

## Why people use [moment.js](https://momentjs.com/)

JavaScript's native functions to manipulate time
isn't very useful.

## Reason to avoid: moment.js is slow

If you have many dates to parse into moment.js objects
from a database (~10000), that takes about 9 seconds
which is very long.

## Reason to avoid: moment.js is a large library and lengthens loading time

moment.js is a large library (~232kB) which can be reduced to
~68kB at most when zipped. There are other libraries like
[Day.js](https://github.com/iamkun/dayjs) which are much smaller,
about 3kB when zipped.

## Reason to avoid: moment.js is mutable which can create confusion

Given
```js
const now = moment(); 
const tomorrow = now.add(1, `day`);
```
`now` and `tomorrow` reference the same object.

The workaround is to force moment.js to return a new instance
each time:
```js
const now = moment();

// passing a moment object as an argument creates a new instance
const tomorrow = moment(now).add(1, `day`);
```

## Reason to avoid: moment.js design sometimes does unintuitive things

Instead of throwing an error when passed an undefined variable,
moment.js just behaves like `moment()` instead.
```js
const lastVisitedAt = moment(`2013-10-24T00:00:00.000Z`);
console.log(moment(lstVlsitedAt).format(`YYYY`)); // 2019
```

## Advantages

* Big community ==> more support for moment.js
* Good timezone support

## Conclusion

Keep using moment.js, except when size/speed is crucial.

