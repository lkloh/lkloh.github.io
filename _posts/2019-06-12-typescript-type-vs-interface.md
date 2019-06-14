---
type: post
title: "Typescript: Type vs Interface"
date: 2019-06-12
---

Should you write
```js
interface Point {
  x: number;
  y: number;
}
```
or
```js
type Point = {
  x: number;
  y: number;
};
```
?

Since types can now be extended,
it is better to use a `type` instead of `interface`
as when using a `type`, errors will be throw for multiple type
declarations of the same name, while multiple interfaces of
the same name will be silently merged.

For example:
```js
interface Point {
  x: number;
}

enum Direction = {
  North = `north`,
  South = `south`,
  East = `east`,
  West = `west`,
}

interface Point {
  direction: Direction;
}
```
and now 

```js
const point: Point = {x: 1};
```
will throw and error due to a missing direction
which doesn't make a lot of sense initially.

