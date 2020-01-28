---
type: post
date: 2020-01-27
title: "#ifndef and #define in C++ header files"
---

Summarized from [here](https://stackoverflow.com/questions/1653958/why-are-ifndef-and-define-used-in-c-header-files).

Why do header files have code like this?`

```c++
// file circle.h

#ifndef CIRCLE_H // What does this do?
#define CIRCLE_H // What does this do?

class Circle {
public:
  Circle(uint16_t radius) : radius_(radius) {}
  
  uint16_t area() const;

private:
  uint16_t radius_;
};

#endif
```

These are `#include` guards.

Suppose we have a program like this
```c++
// main.cc
1 #include circle.h
2 #include <iostream>
3 #include <vector>
4 #include circle.h

int main() {
  Circle c(4);
  return 0;
}
```

When you try to compile `main.cc`, first the compiler sees that the header `circle.h` is included in `main.cc`.
The compiler checks that the unique value `CIRCLE_H` is defined.
It's not defined, so the compiler defines it and moves on.

Now it includes `iostream` and `vector`, then sees the second inclusion of `circle.h`
that the author accidentally added again. Since the compiler
checks and see that the unique value `CIRCLE_H` is already defined, 
so it throws a compilation error to warn the author to remove
the second `#include circle.h`.

This is fairly obvious for our tiny example program,
but it's easy to include things twice in larger production codebases.
