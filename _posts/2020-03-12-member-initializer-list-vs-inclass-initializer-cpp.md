---
type: post
date: 2020-03-12
title: "Member initializer lists vs in-class initializer in C++"
---

Summarized from [here](https://stackoverflow.com/questions/24149924/has-the-new-c11-member-initialization-feature-at-declaration-made-initializati).

There are two ways to initialize a class variable in C++:

```c++
// in-class initializer

class Foo {
  Foo() {
  }  

  std::string bar_(40);
};
```

and then

```c++
// member initialization list

class Foo {
  Foo() : bar_(40) {}  

  std::string bar_;
};
```

So which one should you use?

Probably the second example (member initialization list). If a variable has an in-class member initializer and member initializer in the constructor, the constructor initializer takes precedence. 

So specify a default value for a class variable via an in-class initializer, which will be used if the constructor does not have an explicit member initializer for that variable. Otherwise, the constructor's member initializer will override the in-class initializer.  

This is useful for classes with multiple constructors. If we used member initializers, our class looks like this:
```c++
// member initialization

class Foo {
  Foo() : bar_(40) {}  
  
  Foo(std::string name_) : bar_(40), name_(name) {}  

  std::string name_
  std::string bar_;
};
```
So things are messy and duplicated.

By using common member initializer for all the constructors, instead we can factor things to:
```c++
// in-class initialization

class Foo {  
  Foo() {}  
  
  Foo(std::string name_) : name_(name) {}  

  std::string name_
  std::string bar_(40);
};
```




