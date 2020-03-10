---
type: post
date: 2020-03-08
title: "Class function declaration with DEFAULT"
---

Summarized from [here](https://stackoverflow.com/questions/6502828/what-does-default-mean-after-a-class-function-declaration?rq=1).

## The "default" keyword

Having the `default` keyword after a function declaration allows you to use the compiler-generate version of that function, so you don't need to specify a body.

```c++
// student.h
class Student {
public:  
  Student() = default;
};
```

## The "delete" keyword

Use `= delete` to specify that you don't want to compiler to generate that function automatically. 

For example, this makes the `Student` non-copyable.

```c++
// student.h
class Student {
public:  
  Student() = default;

  Student(const Student &s) = delete;

  Student& operator=(const Student&) = delete;
};
```

If you try to copy an instance of a `Student`, the compiler will throw an error.
