---
type: post
date: 2020-02-27
title: "C++ Constructors cannot be virtual"
---

Summarized from [here](https://www.tutorialspoint.com/virtual-constructor-in-cplusplus).

`virtual` can only be used when there is a base class pointer to a derived class object.

Thus a constructor cannot be virtual, as when a constructor of a class is executed, there is no virtual table in memory, so no pointer is defined. This a constructor always has to be implemented.

However a virtual destructor is allowed.
