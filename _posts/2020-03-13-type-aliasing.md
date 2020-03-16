---
type: post
date: 2020-03-13
title: "Type aliasing in C++"
---

Summarized from [here](https://www.internalpointers.com/post/differences-between-using-and-typedef-modern-c).

You can give synonyms to types that are too complex. These types keep the code understandable.

For example, this isn't very fun to parse,
```c++
std::map<std::string, std::set<std::string>> enrolled_students;
```
and then
```c++
bool num_students_in_class(
    const std::string& class_name,
    std::map<std::string, std::set<std::string>> enrolled_students) {
  return enrolled_students.get(class_name).size();
}
```
instead, you can use type aliasing to make it more readable:
```c++
typedef std::set<std::string> Students;
typedef std::map<std::string, Students> StudentInClasses;

bool num_students_in_class(
    const std::string& class_name,
    StudentInClasses enrolled_students) {
  return enrolled_students.get(class_name).size();
}
```

C++-11 introduced the `using` keyword:
```c++
using Students = std::set<std::string>;
using StudentInClasses = std::map<std::string, Students>;

bool num_students_in_class(
    const std::string& class_name,
    StudentInClasses enrolled_students) {
  return enrolled_students.get(class_name).size();
}
```
