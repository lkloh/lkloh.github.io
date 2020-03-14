---
type: post
date: 2020-03-12
title: "Pure virtual function vs virtual function in C++"
---

Summarized from [here](https://stackoverflow.com/questions/2652198/difference-between-a-virtual-function-and-a-pure-virtual-function).

## Pure virtual function

A pure virtual function that is usually not (but can be) implemented in the base class, and must be implemented in the subclass instead. It's denoted by appending `= 0` to the declaration:

```c++
class Base {
public:
    virtual void foo(const std::string &name) = 0;
}
```

Then if you want to instantiate a subclass of `Base`, you need to implement the pure virtual function:

```c++
class Derived: public Base {
public:
  virtual void foo(const std::string &name) override {
    name_ = name;
  }

private:
  std::string name;
};
```

The `override` keyword ensures the compiler will check that the derived function has the same function signature as the parent class'.

Having a pure virtual function in a class makes it abstract. This means that the class cannot be instantiated, and a derived class that is to be instantiated needs to implement all the inherited pure virtual functions.

## Virtual function

In contrast, a virtual function does _not_ need to be implemented by the derived class.
```c++
class Base {
public:
  void foo(const std::string &name) {
    name_ = name;
  };

private:
  std::string name_;
};

class Derived : public Base {
public:
  void bar() {
    std::cout << "Name: " << name_ << std::endl;
  }
};
```
