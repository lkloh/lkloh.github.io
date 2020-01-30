---
type: post
date: 2020-01-16
title: "#include in .h or .cc?"
---

Summarized from [here](https://stackoverflow.com/questions/3002110/include-in-h-or-c-cpp/3002124).

When you need to `#include` libraries in C++,
put as much in `.c` as possible, and as little in `.h`.

This speeds up compilation as `.h` files would be cross-referenced less.

The [Google Style Guide](https://google.github.io/styleguide/cppguide.html#Names_and_Order_of_Includes) recommends the following order of inclusion:
1. header file of what you're implementing 
2. C System headers
3. C++ standard library headers
4. Other libraries .h files
5. Your project's .h files