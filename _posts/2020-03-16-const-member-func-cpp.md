---
type: post
date: 2020-03-16
title: "Const member functions in C++"
---

Summarized from [here](https://www.geeksforgeeks.org/const-member-functions-c/).

## Const objects

Objects of a class can be declared as `const`. An object declared as `const` cannot be modified, so it cannot modify the object it is called with. If someone tries to change a const object, the compiler will throw an error.

```c++
const std::string name = "John Doe";

name = "John Roe"; // compile time error, error!
```

## Const functions

If a function is declared as `const`, it cannot modify the object on which they are called. It is good to make as many functions `const` as possible, so that users do not accidentally change the function.

```c++
class Foo {
  Foo(const std::string& bar) : bar_(bar) {}
  
  const std::string get_bar() {
    return bar_;
  }
  
  std::string bar_;
};
```
Now, if you try to do this, you get an error:
```c++
class Foo {
  Foo(const std::string& bar) : bar_(bar) {}
  
  const std::string get_bar() {
    bar_ += " testing"; // compiler error
    return bar_;
  }
  
  std::string bar_;
};
```

When a function is declared as const, it can be called on any type of object.
```c++
const std::string foo(const std::string &name) {
  return name + " test";
}

const std::string bar(std::string &name) {
  return name.substr(0, 5, "testing");
}
```

Non-const functions can only be called by non-const objects.
```c++
std::string foo(const std::string &name) {
  return name.substr(0, 5, "testing"); // compiler error
}

std::string bar(std::string &name) {
  return name.substr(0, 5, "testing"); // ok
}
```

