---
type: post
date: 2020-01-17
title: "Passing optional arguments in C++"
---

Like this
```c++
void foo(int mandatory1, int mandatory2, int optional1 = 666, int optional2 = 777) {
  // ... 
}
```
with the mandatory arguments first, and the optional arguments last.

Then these are all legal ways to call `foo`:
```c++
foo(1, 2);
foo(1, 2, 11);
foo(1, 2, 11, 22);
```

Unfortunately, this is not legal:
```c++
foo(1, 2, , 22);
```

Instead, you probably want to refactor things to
```c++
static const int DEFAULT_OPTIONAL_1 = 666;
static const int DEFAULT_OPTIONAL_2 = 777;

void foo(int mandatory1, int mandatory2,
  int optional1 = DEFAULT_OPTIONAL_1,
  int optional2 = DEFAULT_OPTIONAL_2) {
  // ... 
}

foo(1, 2, DEFAULT_OPTIONAL_1, 22);
```
