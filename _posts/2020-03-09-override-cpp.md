---
type: post
date: 2020-03-09
title: "Override in C++"
---

Summarized from [here](https://stackoverflow.com/questions/18198314/what-is-the-override-keyword-in-c-used-for).

The `override` keyword is used to mark a method as  overriding a virtual method of the base class. It also tells the compiler that a method is override a base class method, so it checks that the programmer has not modified or implemented a new method that he mistakenly assumes is overriding the base class.

```c++
class base {
public:
  virtual int foo(std::string &num_str) = 0;
};

class DerivedCorrect : public base {
public:
  int foo(std::string &num_str) override { // OK
    return stoi(num_str, nullptr);
  }  
};

class DerivedWrong: public base {
  public:
    int foo(const char *num_str) override { // ERROR
      return stoi(num_str, nullptr);
    }
};
```

