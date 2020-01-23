---
type: post
date: 2020-01-22
title: "Static casts in C++"
---

Modified from [here](https://stackoverflow.com/questions/3987640/variable-creation-on-heap-or-stack-in-c).

There are two ways to create an object:

```cpp
// Method 1: on the stack
Circle make_circle() {
  Circle c;
  c.set_radius(3);
  return c;
}

int main() {
  Circle c = make_circle();
  get_circle_area(&c);
}
```

or

```cpp
// Method 2: on the heap
Circle* make_circle() {
  Circle* c = make_unique<Circle>();
  c->set_radius(3);
  return c;
}

int main() {
  Circle* c = make_circle();
  get_circle_area(c);
}
```

It is better to create the object on the stack if possible, 
since the compiler will automatically manage the memory for you.

Now, the use of `unique_ptr` in Method 2 will also allow for automatic memory management,
but the problem with pointers is that there are lots of ways to misuse them, so its
better not to use pointers unless absolutely necessary to let the object live beyond a
function's scope. Returning the object itself will accomplish that too.

