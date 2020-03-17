---
type: post
date: 2020-03-14
title: "Variadic templates in C++"
---

Summarized from [here](https://kevinushey.github.io/blog/2016/01/27/introduction-to-c++-variadic-templates/) and [here](https://thispointer.com/c11-variadic-template-function-tutorial-examples/).

Variadic templates are used to write functions with an arbitrary number of arguments.

```c++
template <typename... Ts> 
void do_nothing(Ts... ts) {
  (void) ts;
}
```

In the example above, `typename... Ts` is used to declare `Ts` as a template parameter pack. The `...` operator emphasises that this denotes an arbitrary number of types.

The function signature `void do_nothing(Ts... ts)` accepts a function parameter pack - a pack of parameters whose types are given by the template parameter pack `typename... Ts`. Those arguments are declared as `Ts... ts`, in which `...` is used to indicate that `Ts` refers to types for an arbitrary number of arguments.

This is the equivalent of 
```c++
template <typename T1, typename T2, ..., typename Tn>
void do_nothing(T1 t1, T2 t2, ..., Tn tn) {
  (void) t1;
  (void) t2;
  // ...
  (void) tn;
}
```

Thus, calling
```c++
do_nothing("name", 2.3, 1);
```

is the equivalent of doing
```c++
do_nothing<std::string, double, int>("name", 2.3, 1);
```

To use the arguments in a variadic function, you need to write them recursively. Meaning:

```c++

template<typename T, typename ... Args>
void log(T first, Args ... args) {
 
	// Print the First Element
	std::cout << first << " , ";
 
	// Forward the remaining arguments
	log(args ...);
}
```

To see how this works on a caller 
```c++
log(2, 3.4, false);
```

the compiler internally creates this function out of the variadic template function:
```c++
void log(int first, double b, bool c) {
  std::cout << first << " , ";
  log(b, c);
}
```
It prints the first parameter, `2`, and forwards the remaining parameters to the log function.

```c++
void log(double first, bool c) {
  std::cout << first << " , ";
  log(c);
}
```
It prints the first parameter, `3.4`, and forwards the last parameter to the log function

```c++
void log(bool first) {
  std::cout << first << " , ";
  log();
}
```
Now it prints the first parameter, `false`, and calls the `log` function with no arguments, then returns. So we must define a `log` function that takes no arguments.

So the stack trace looks like this:

```c++
void log();
void log(bool first);
void log(double first, bool c);
void log(int first, double b, bool c);
```

The entire program looks like this:
```c++
#include <iostream>

void log() {
  // do nothing
}

templace<typename Fst, typename Ts... ts)
void log(Fst first, Ts... ts) {
  std::cout << first << ", ";
  log(ts ...);
}

int main() {
  log(2, 3.4, false);
  return 0;
}
```
and the output is
```
2, 2.4, false,
```
 
