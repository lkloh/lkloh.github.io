---
type: post
date: 2020-03-11
title: "Buffer flushing: std::endl vs '\n'"
---

Summarized from [here](https://stackoverflow.com/questions/9651311/buffer-flushing-n-vs-stdendl).

There are two well known ways to output in C++:

```c++
std::cout << "Hello world!" << std::endl;
```

and

```c++
std::cout << "Hello world!" << '\n';
```

Which one should you use?

## When performance matters

Use 
```c++
std::cout << "Hello world!" << '\n';
```
when you are trying to write large amounts of text to a file, as `std::endl` flushes the output buffer immediately. File access is slow, so use `\n` instead to improve performance by allowing buffering to take place.

## When performance is not so important

```c++
std::cout << "Hello world!" << std::endl;
```

For clarity - that seems to be the standard convention.
