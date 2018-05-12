---
type: post
title: "Increasing the timeout for one case in Mocha tests"
date: 2018-05-11
---

To increase the timeout for ONE Mocha test (maybe it is being used to do load testing?),
you can write

```js
it(`returns an empty array when given undefined values`, function() {
  // default 2 second timeout
  const result = doubleValues(null);
  expect(result).to.eql.([]);
});

it(`doubles the value of every element in an array`, function() {
  // default 2 second timeout
  const arr = [1, 2, 3];
  const result = doubleValues(arr);
  expect(result).to.eql.([2, 4, 6]);
});

it(`handles large volumnes of data fast`, function(done) {
  this.timeout(5000); // 5 second timeout
  const largeArr = new Array(100000).fill(23);
  doubleValues(largeArr); // attempt to process a HUGE array
  done();
});
```

Thanks [Stack Overflow](https://stackoverflow.com/questions/15971167/how-to-increase-timeout-for-a-single-test-case-in-mocha)!

