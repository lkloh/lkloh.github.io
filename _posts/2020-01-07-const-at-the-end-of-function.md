---
type: post
date: 2020-01-07
title: "Const at the end of a function declaration"
---

When you add a `const` to the end of a function,
that function is not allow to change member data.

```c++
class Foo {
private:
    int counter_;

public:
  Foo() {
    counter_ = 0;
  }
  
  void increment_counter {
    // compiles
    counter++;
  };

  void increment_counter const {
    // does not compile
    counter++;
  }
};

```

Adding `const` is a way to communicate that the method will not alter
members of the class.

Well, mostly. You can mark a member as `mutable` and then a `const` function
can change it, but try not to do that since its confusing.
