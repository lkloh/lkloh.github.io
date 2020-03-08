---
type: post
date: 2020-01-29
title: "Optional function arguments in C++"
---

Optional arguments in C++ can be added
```c++
void foo(int mandatory, int optional1 = 0, int optional2 = 1) {
  std::cout << "Mandatory: " << mandatory
    << ", Optional 1: " << optional1 
    << ", Optional 2: " << optional2 << std::endl;
}
```
And when you run
```c++
foo(1000, 2000);
```
You will get
```
Mandatory: 1000, Optional 1: 2000, Optional 2: 1
```
However there is no way to option-bag arguments like the way JavaScript does it,
so you need to be strategic about the way you order arguments in C++ to avoid needing to declare a long chain of arguments.
