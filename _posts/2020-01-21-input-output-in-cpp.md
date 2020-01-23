---
type: post
date: 2020-01-21
title: "Input/Output in C++"
---

Summarized from [here](http://www.cplusplus.com/reference/iostream/).

## cout: printing to console

To print something generic to the console in C++,
such as an explanation of what a program does, use `cout`:

```c++
#include <iostream>
  
int main() {
  std::cout << "Hello, world!" << std::endl;
}
```

## cin: input from user

```c++
#include <iostream>

int main() {
  string name;
  std::cout << "Please your name: ";
  std::cin >> name;
  std::cout << "Hello, " << name << std::endl;
}
```

## cerr: flagging an error in a program

```c++
#include <iostream>

int main() {
  int i;
  std::cout << "Please enter an even number: ";
  std::cin >> i;

  if (i % 2 == 0) {
    std::cout << "Congradulations, " << i << " is an even number!" << std::endl;
  } else {
    std::cerr << "Sorry, " << i << " is an odd number :(" << std::cerr;
  }
}
```

## clog: buffered logging

If you have a lots of data to log, use `clog`.
It is buffered and therefore more efficient than unbuffered output.
Information written to `clog` is saved to a variable and written to disk in one go,
while `cerr` writes to disk immediately.
Thus, `clog` is more efficient than `cerr` and therefore better to use to log non-critical errors.

```c++
#include <iostream>

void generate_even_ints() {
  int count = 0;
  while (count < 100) {
    int i = get_random_int();
    if (i % 2 == 1) {
      std::clog << "Sorry, " << i << " is not an integer." << std::endl;
    }
    count++;
  }
}
```
