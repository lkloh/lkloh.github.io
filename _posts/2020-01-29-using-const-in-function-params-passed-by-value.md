---
type: post
date: 2020-01-29
title: "Using const in function params that are passed by value"
---

Summarized from [here](https://stackoverflow.com/questions/39848541/why-should-i-not-use-const-in-this-simple-function).

What's wrong with doing this?
```c++
// person.h
class Person {
public:
  Person(std::string name);

  void set_age(const int age);

private:
  std::string name_;
  std::string age_;
};

// person.cc
class Person {
public:
  Person(std::string name) : name_(name) {}

  void set_age(const int age) {
    age_ = age;
  }
}
```

Well 
```c++
set_age(const int age);
```
is redundant since `age` is already passed by value. Even if you change the value of `age`, the change won't affect
 the caller. So having that extra `const` declaration just clogs up space.
 
Now, in the implementation,
```c++
void set_age(const int age) {
  age_ = age;
}
``` 
You get a compiler error if you try to modify `age` since it is marked as `const`.

So really if you want to signal to the user that `age` should not be changed by `set_age`, you can do this:

```c++
// person.h
class Person {
public:
  Person(std::string name);

  void set_age(int age);

private:
  std::string name_;
  std::string age_;
};

// person.cc
class Person {
public:
  Person(std::string name) : name_(name) {}

  void set_age(const int age) {
    age_ = age;
  }
}
```

However when I tried to do just that and put it up for code review (not this exact little snippet obviously), people
 got confused because they thought that having different function definitions in header and implementation files
  would cause the compiler to throw an error.
  
Apparently my efforts to be `const` correct caused _more_ confusion, not less, so I ended up doing this:
```c++
// person.h
class Person {
public:
  Person(std::string name);

  void set_age(int age);

private:
  std::string name_;
  std::string age_;
};

// person.cc
class Person {
public:
  Person(std::string name) : name_(name) {}

  void set_age(int age) {
    age_ = age;
  }
}
```
