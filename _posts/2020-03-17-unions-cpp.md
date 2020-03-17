---
type: post
date: 2020-03-17
title: "When to use unions C++"
---

Summarized from [here](https://stackoverflow.com/questions/2310483/purpose-of-unions-in-c-and-c).

One of the uses of unions is to save memory by using the same memory to store different objects at different times. Similar to how a single hotel room with a single bed can hold many people comfortably over the course of a month, since the hotel ensures that only one person gets to book the room at any given time. 

If several objects in your program hold different values on non-overlapping timelines, you can merge them in a union to save memory, since the union has only one active member at any given moment. Just likely how the hotel room has only one guest at any given time. 

For example:
```c++
union FooBar {
  int foo;
  double bar;
};

FooBar fb[10];
for (int i = 0; i < 10; i++) {
  if (i % 2 == 0) {
    fb[i].foo = i;
  } else {
    fb[i].bar = static_cast<double>(i) + 0.5;
  }
}
```
