---
type: post
title: "Promises vs Callbacks"
date: 2018-09-12
---

When writing an async function, you should return a promise instead of passing a callback in,
as callbacks don't scale well when you need a function to execute only after multiple async functions
have successfully returned.

For example, if you have three async functions,
`get_students`, `get_gpas`, and `get_class_years` that need to return before you can
execute the function `get_students_qualified_to_graduate`,
then with callbacks you'll be doing:

```js
get_students(get_gpas(get_class_years(get_students_qualified_to_graduate))));
```

which is very messy and does not scale well when there are a large number of async functions
that need to return in order to execute another function.
You'll end up with async functions passed as callbacks to async functions,
which gets messy and hard to debug very quickly when something goes wrong.

Now if all the functions returned a promise instead, you could do:
```js
Promise.all([
  get_students,
  get_gpas,
  get_class_years,
]).then(() => {
  get_students_qualified_to_graduate();
}, () => {
  throw Exception(`did not fetch all the data needed to compute graduating students`);
});
```

and now `get_students_qualified_to_graduate` only returns if all the three required functions
had successfully returned as well.

Inspired by [this post](https://medium.com/devnetwork/moving-to-promises-and-async-await-from-callback-a003e09fe91c).

