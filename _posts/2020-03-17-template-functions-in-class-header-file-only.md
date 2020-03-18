---
type: post
date: 2020-03-17
title: "Why class member template functions can only go into the header file (C++)"
---

Summarized from [here](https://stackoverflow.com/questions/495021/why-can-templates-only-be-implemented-in-the-header-file).

I was trying to make a class that looked like this:

```c++
// base.h

class Base {
  Base();

  int add_one(int n);
  
  template<typename T>
  std::string triple_val(T t);
};
```
With a header file

```c++
// base.cc;

class Base {
  Base() {}

  int add_one(int n) {
    return n + 1;
  }
  
  template<typename T>
  std::string triple_val(T t) {
    return std::to_string(t * 3);
  }
};
```
and an implementation file.

Then, I wanted to make a derived class to inherit from `Base`.

```c++
// derived.h

class Derived : public Base {
  Derived();
  
  void log();
};
```
With a header file too,

```c++
// derived.cc;

class Derived : public Base {
  Derived() {}
  
  void log() {
    int double val = Base::triple_val<int>(3) *  Base::triple_val<double>(2.4);
    std::cout << val << std::endl;
  }
};
```
And an implementation file.

But it wouldn't compile. I got a linker error instead. 

After a lot of hair pulling, I realized that I should have placed the implementation of `double_val` into the _header_ file of base.h, instead of the source file. 

```c++
// base.h

class Base {
  Base();
  
  int add_one(int n);

  template<typename T>
  std::string double_val(T t) {
    return std::to_string(t * 2);
  }
};
```
and

```c++
// base.cc;

class Base {
  Base() {}
  
  int add_one(int n) {
    return n + 1;
  }
};
```

The reason for this is that when instantiating a template function, the compiler creates a new class with the given template argument.

Thus calling
```c++
int double val = Base::triple_val(3) *  Base::triple_val(2.4);
```
in the derived class was the equivalent to the compiler generating
```c++
std::string triple_val(int t) {
  return std::to_string(t * 3);
}
```
and
```c++
std::string triple_val(double t) {
  return std::to_string(t * 3);
}
```

Thus, to instantiate template functions with the template arguments, the compiler needs access to the method implementation. If the implementations are omitted from the header, they are not accessible, thus the compiler cannot instantiate the template.

To fix, this, write the template implementation in the header file itself.

Alternatively, you can explicitly instantiate every template instance you need:

```c++
// base.h

class Base {
  Base();

  int add_one(int n);
  
  template<typename T>
  std::string triple_val(T t);
};
```
in the base header file,

```c++
// base.cc;

class Base {
  Base() {}

  int add_one(int n) {
    return n + 1;
  }
  
  template<typename int>
  std::string triple_val(T t) {
    return std::to_string(t * 3);
  }

  template<typename double>
  std::string triple_val(T t) {
    return std::to_string(t * 3);
  }
};
```
in the source file.
