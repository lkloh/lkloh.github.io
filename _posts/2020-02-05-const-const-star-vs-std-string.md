---
type: post
date: 2020-02-05
title: "Const char * vs std::string"
---

When writing a C++ program, given the choice between writing
```c++
void file_reader(const char *input_file);
```
or 
```c++
void file_reader(std::string input_file);
```
which should you pick?

## When to use const char *

* Dealing with talking to OS. However `std::string::c_str` should cover that.
* Compatibility with old C code - though again `std::string::c_str` should cover that.
* When keeping memory utilization low is important, as `std::string` uses more memory. Not that much more as its highly optimized, so only if you're dealing with embedded platforms and the like.

## When to use std::string

* Most cases, as it gives access to all sorts of of helpful functions, like `substr`, `find`, etc. Even if you're not using those functions now, it could come in handy in future.
