---
type: post
date: 2020-01-14
title: "Static const vs const in C++"
---

Summarized from [here](https://www.quora.com/What-is-the-difference-between-constant-and-static-constant-in-C).

`static const` and `const` mean the same thing inside a function.
```cpp
function foo() {
  static const int my_x = 3;
  const int my_y = 3;
}
```

but outside of it
```cpp
// bar.h
static const int my_w = 4;
const int my_z = 4;
```
means that `my_z` is visible to any file that imports `bar.h` but `my_w` is only visible in its source file.

Thus
```cpp
// foobar.h
import "bar.h"

int main() {
  int my_h = my_z + 1;
  std::cout << my_h << std::endl; // outputs
  return my_w; // compile error
}
```

This has the additional benefit of ensuring that 
`my_w` doesnt' have a name that collides with another variable inside `foobar.h`.

