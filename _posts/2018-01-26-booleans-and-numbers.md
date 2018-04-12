---
type: post
title: "0 and 1 == 1 in Python"
date: "2018-01-26"
---

Recently I was working with a database that looked like this:

```
Students
 ------------------------------------
| id | first_name | last_name | car  |
 ------------------------------------
| 1  | Anna       | Anderson  | 45   |
 ------------------------------------
| 2  | Bob        | Brown     | NULL |
 ------------------------------------
| 3  | Charlie    | Chaplin   | 42   |
 ------------------------------------
| 4  | Dean       | Davis     | NULL |
 ------------------------------------
| 5  | Eliza      | Ellen     | 21   |
 ------------------------------------
```

and `car` was the foreign key to 
```
cars
 ----------------------
| id | Model    | Year |
 ----------------------
| 21 | Toyota   | 2005 |
 ----------------------
| 42 | Mercedes | 2000 |
 ----------------------
| 45 | Tesla    | 2017 |
 ----------------------
```

Then what's wrong with this line of code?

```py
def takes_public_transport(student):
  return not student.car
``` 

It only returns `True` for students whose car is is a positive integer.
If a student's car id is 0, then even though the student has a car,
that student is recorded as taking transport.

Instead, it would be better to write
```py
def takes_public_transport(student):
  return student.car is None
```




