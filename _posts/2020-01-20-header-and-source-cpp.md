---
type: post
date: 2020-01-20
title: "Header and source files in C++"
---

## Why C++ has header and source files

Summarized from [here](http://www.cplusplus.com/forum/articles/10627/).

* Speed compile time up. If everything is in the same file,
a small change requires a full recompilation.

* Code is more organized as you can have one concept per file.

* Separates interface from implementation.

## C++ file extensions

Modified from [here](https://stackoverflow.com/questions/1545080/c-code-file-extension-cc-vs-cpp/1545085).

* Header files use one of: `.h | .hpp | .hxx`

* Source files use one of: `.cc | .cpp | .cxx`

Either of the nonmenclatures work, the important thing is consistent naming within your repository.

Different environments have commonly used conventions.
For example Unix uses `.cc | .cxx`, while Windows `.cpp | .cc | .cxx`.
