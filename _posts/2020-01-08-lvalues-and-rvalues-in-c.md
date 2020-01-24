---
type: post
date: 2020-01-08
title: "LValues and RValues in C"
---

Summarized from [here](https://www.internalpointers.com/post/understanding-meaning-lvalues-and-rvalues-c).

An lvalue points to a specific memory location.

For example, `horcrux_container` is an lvalue
```c++
//
string horcrux_container = "voldemort's soul fragment"; 
```

An rvalue does not point anywhere.
The string `"voldemort's soul fragment"` is an rvalue.

You can think of an lvalue as a container,
and an rvalue as a thing inside the container, which cannot exist without it.
Hence the Harry Potter analogy.

Therefore you can do something like
```c++
char* diary = horcrux_container.data();
```

but you can't do
```c++
"voldemort's soul fragment" = 7;
```
