---
type: post
date: 2020-02-04
title: "Global const in C++"
---

Any introductory computer science class probably taught you not to do this:

```c++
// main.cc

int x = 5; // global variable

int foo(int y) {
  x *= 2;
  x += y;
  return x;
}

int main() {
  return foo(2);
}
```
since any function in our implementation could change `x`,
making it very difficult to keep track of what `x` should be.

What's so bad about this, though?
```c++
// person.h

class Person {
  const std::string DEFAULT_FIRST_NAME = "John";
  const std::string DEFAULT_LAST_NAME = "Doe";
  const std::string DEFAULT_GENDER = "Male";
  const int DEFAULT_AGE = 40;
  
  Person(std::string first_name, std::string last_name, std::string gender);
  
  set_age(int age);
};
```

All the global variables are `const` so no-one can change them - unless someone decides it's a good idea to get a
 pointer to one of the `const` variables and alter the data the pointer points to.

There are a few other reasons to avoid even `const` global variables.

It can make it harder to decouple then when
 writing unit tests. Sometimes you want to use toy values in unit tests for clarity's sake, as the actual values are
  much harder to test on.
 
Using `const` globals could lead to namespace pollution - for example you could accidentally reassign a global
 variable if you misspell a local variable.
 
Since local variables can only be used by one tiny part of a larger program, it is easier to reason about them; while
 global variables can be used by any part of a program so you have to think about a larger scope of possible use cases.

