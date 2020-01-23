---
type: post
date: 2020-01-23
title: "Static casts in C++"
---

Modified from [here](https://www.geeksforgeeks.org/static_cast-in-c-type-casting-operators/).

Cast operator converts one data type to another.
The way we do it in C++ is different from how it is done in C.

## Static cast

A compile time cast - so it catches errors early.
It's always good to catch errors at compile time instead of run time.

You make a static cast from `float` to `int` in C++ like this:

```cpp
// C++ way
int foo() {
  float f = 3.5;
  return static_cast<int>(f);
}
```

An alternative way to do integer casting in C++ is to follow the C way and do it implicitly:

```cpp
// C way
int foo() {
  float f = 3.5;
  int n = f;
  return n;
}
```

However there are dangers with doing casting the C way.

```cpp
int* bar() {
  char c = 'a'; 
      
  // pass at compile time, may fail at run time 
  int* q = (int*)&c;
  return q;
} 
```

To get errors thrown at compile time, do it the C++ way with static casts:

```cpp
int* bar() {
  char c = 'a'; 
  
  int* q = static_cast<int*>&c;
  return q;
} 
```

And you will get this error at compile time:
```
[Error] invalid static_cast from type 'char*' to type 'int*'
```







