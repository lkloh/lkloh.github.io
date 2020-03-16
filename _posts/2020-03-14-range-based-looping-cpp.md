---
type: post
date: 2020-03-14
title: "Range based looping in C++"
---

Summarized from [here](https://www.geeksforgeeks.org/range-based-loop-c/).

Added in C++-11 - executes a `for` loop over a range for increased readability and less risk of out-of-range issues.

```c++
for (auto var : object_to_range_over) {
  // do something with "var"
}
```

As an example, we have:
```c++
std::map<std::string, int> values = {
  {"Alice", 34},
  {"Bob", 27},
  {"Carol": 29},
};
int sum_of_counts = 0;
for (auto entry : map) {
  sum_of_counts += entry.second;
}
```