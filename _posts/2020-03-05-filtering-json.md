---
type: post
date: 2020-03-05
title: "Filtering JSON"
---

[JQ](https://stedolan.github.io/jq/manual/) is a program to filter JSON.

Given a json data set structured like this:
```
// students.json

{
  student: "Alice",
  gpa: 3.4,
}
{
  student: "Bob",
  gpa: 3.2,
}
{
  student: "Carol",
  gpa: 3.9,
}
{
  student: "Dave",
  gpa: 2.7,
}
```
to extract only the student names, you run
```
cat students.json | jq .student > student_names.json
```
and you get this file
```
// student_names.json

Alice
Bob
Carol
Dave
```

Read more [here](https://stackoverflow.com/questions/39228500/extract-a-specific-field-from-json-output-using-jq).
