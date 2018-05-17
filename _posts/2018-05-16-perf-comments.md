---
type: post
title: "Comments for performance tests"
date: 2018-05-16
---

I was writing a comment for a MochaJS performance test:
```js
it(`handles large amounts of data`, function(done) {
  this.timeout(10000); // test runs in < 3000ms but set timeout to 10000ms to reduce flakyness
  const hugeArray = generateHugeArray();
  processArray(hugeArray);
  done();
});
```

What I should have written for the comment was this:
```js
it(`handles large amounts of data`, function(done) {
  this.timeout(10000); // Set timeoutTime > runTimeOfTest to reduce flakyness
  const hugeArray = generateHugeArray();
  processArray(hugeArray);
  done();
});
```
so that if the performance of `processArray` _improved_ in future due to refactoring/upgraded servers,
I would not need to update the comment.


