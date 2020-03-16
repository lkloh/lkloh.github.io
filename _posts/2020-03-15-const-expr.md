---
type: post
date: 2020-03-15
title: "Constexpr vs const in C++"
---

Summarized from [here](https://stackoverflow.com/questions/14116003/difference-between-constexpr-and-const).

## const 

`const` makes an object constant, so it can't be modified in the code. Thus, the compiler can use this to do optimizations. If the programmer accidentally tries to change the value of that object after initialization, the compiler will throw a warning.

`const` can only used for non-static member functions, but not all functions. It guarantees that the function does not modify any of the non-static data functions.

```c++
// ok
class foo {
  std::string bar_;
  
  const get_bar() {
    return bar_;
  }
};

// not ok
class foo {
  std::string bar_;
  
  const get_bar() {
    // error!
    return bar_.push_back('a');
  }
};
```

## constexpr

It tells the compiler that the expression results in a constant value at compile-time, so it can be used in places like array lengths, const var assignment, etc.

```c++
constexpr uint64_t factorial(uint64_t i) {
  if (i == 0 || i == 1) {
    return 1;
  }
  return i * factorial(i - 1);
}

int main() {
  int arr[factorial(3)];
  return 0;
}
```