---
type: post
date: 2020-03-17
title: "No virtual class member function templates in C++"
---

Summarized from [here](https://stackoverflow.com/questions/2354210/can-a-class-member-function-template-be-virtual).

C++ class member function templates cannot be virtual, because of the difficulties of implementing this.

The compiler generates the class member templated code at compile-time. 

In contrast, given a class, the system needs to figure how many instances of that class to generate at run-time. By the time the run-time system realizes it needs to call a templated class member virtual function, compilation is done, so the compiler cannot generate that particular instance anymore. Thus class member virtual function templates are not allowed. 

So you'll just have to work around things.
