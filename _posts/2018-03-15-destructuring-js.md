---
type: post
title: "Destructuring JavaScript"
date: 2018-03-15
---

Normally, if you want to pass ing arguments to a JavaScript function, you need to remember the order carefully:
```js
function transformHuman(name, id, email, birthday) {
  // do something
}
```

and carefully make sure you're calling it as
```js
transformHuman('Jane Roe', 42, jane.roe@gmail.com, '2007-07-17');
```

and not 

```js
transformHuman('Jane Roe', 'jane.roe@gmail.com, 42, '2007-07-17');
```

for example, or you will get lots of weird issues.

Instead, you can write things as
```js
function transformHuman({name='John Doe', email='john.doe@gmail.com', id=1, birthday='1970-01-01'}) {
  // do something
}
```

In that case you can now call the function as
```js
transformHuman({
  name: 'Jane Roe',
  id: 42,
  email: 'jane.roe@gmail.com',
  birthday: '2007-07-17',
});
```

or


```js
transformHuman({
  id: 42,
  birthday: '2007-07-17',
  email: 'jane.roe@gmail.com',
  name: 'Jane Roe',
});
```
And you will still get the correct results.

Here's an implementation to show how the typecasting works in action.
```js
// Javascript destructuring: no order needed
let p = {x: 10, y: 20, z: 30};
let {z, y, x} = p;
console.log(`x: ${x}, y: ${y}, z: ${z}`);

let pp = {xx: 10, yy:20};
let {zz, yy, xx} = pp;
console.log(`xx: ${xx}, yy: ${yy}, zz: ${zz}`);


function destructure({z=30, y=20, x=10}) {
    console.log(`x: ${x}, y: ${y}, z: ${z}`);
}

destructure({x: 11, y: 22, z: 33}); // all arguments present
destructure({x: 11, y: 22}); // one argument missing
```
Also known as `option bagging` arguments for readability.

