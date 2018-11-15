---
type: post
title: "Naming best practices"
date: 2018-10-17
---

Name variables after their functionality, not their implementation.
Also, try to go one level above their abstraction when naming things
so you don't get too verbose.

Remember that there are two hard things:
naming things and cache invalidation,
so keep getting feedback from reviewers who are not as deeply
involved in implementation as you are.

When naming a boolean variable, call it something that
suggests a factual statement, not an action.

```js
const isHidden = true; // suggests a fact
```

versus

```js
const hideElement = true; // suggests "hideElement" is a function hiding something, not a static variable
```

