---
type: post
date: 2020-03-11
title: "Using std::optional"
---

Summarized from [here](https://stackoverflow.com/questions/56082568/use-stdoptional-as-a-regular-pointer-vs-use-has-value-and-value).

What's wrong with doing this?
```c++
std::string graduation_year(std::optional<std::string> graduation_year) {
  if (graduation_year.has_value()) {
    return graduation_year.value();
  } 
  return 'still studying!';
}
```

It takes longer than it should. The check for `if (graduation_year.has_value())` already guarantees that `graduation_year` has a value, so you could just dereference it to get the value out, instead of doing another check inside the body with takes extra time.

```c++
std::string graduation_year(std::optional<std::string> graduation_year) {
  if (graduation_year.has_value()) {
    return *graduation_year;
  } 
  return 'still studying!';
}
```
