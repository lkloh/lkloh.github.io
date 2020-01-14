---
type: post
date: 2020-01-14
title: "Static const vs const in C++"
---

Summarized from [here](https://www.quora.com/What-is-the-difference-between-constant-and-static-constant-in-C).

`static const` and `const` mean the same thing inside a function.
```
function foo() {
  static const int x = 3;
  const int y = 3;
}
```

but outside of it
```
// bar.h
static const int w = 4;
const int z = 4;
```
means that `z` is visible to any file that imports `bar.h` but `w` is only visible in its source file.

Thus
```
// foobar.h
import "bar.h"

int main() {
  int h = z + 1;
  std::cout << h << std::endl; // outputs
  return w; // compile error
}
```

