---
type: post
date: 2020-01-06
title: "Don't use namespace std"
---

Summarized from [here](https://stackoverflow.com/questions/1452721/why-is-using-namespace-std-considered-bad-practice).

Given these two namespaces
```c++
// foo.h
namespace foo {
void foo_func();
}
```
and
```c++
// bar.h
namespace bar {
void bar_func();
}
```
what's wrong with doing this?
```c++
using namespace foo;
using namespace bar;

int main() {
  foo_func();
  bar_func();
}
```
Well - imagine we upgraded `foo` to version 2.0, and added a new function
```c++
namespace foo {
void foo_func();

void bar_func();
}
```
Now we get a conflict as foo 2.0 and bar both import `bar_func` into the global namespace.

Alright - so don't import custom-made namespaces in.

But how about this?

```c++
// student.h file

using namespace std;

class Student {
private:
  double gpa_;
  uint16_t id_;
  string name_;
  
public:  
  Student(id, name) {
    id_ = id;
    name_ = name;
  }

  double get_gpa() const {
    return gps_;
  }

  uint16_t get_id() const {
    return id_;
  }

  void set_gpa(gpa) {
    gpa_ = gpa;
  }

  string get_name() const {
    return name_;
  }

  double print() const {
    cout << name_ << endl;
  }
};
```
Surely it's ok to import the standard library in?

Well, no. `using namespace std;` forces anyone who calls the `student.h` file to 
also "use" the `std` library.

Also, just prefacing everything with `std::` makes it easy to see at first glance
that a method called is from the standard library.
