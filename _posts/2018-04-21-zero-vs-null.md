---
type: post
title: "Zero vs Null"
date: 2018-04-21
---

## Question

What's wrong with this function?

```js
function getPeopleWithSetSalary(arr) {
  arr.filter(person => person.salary);
}
```

## Answer

It filters out people with a defined salary of $0.
This what happens when you call it:
```js
const arr = [
  {name: 'Alice', salary: 30},
  {name: 'Bob', salary: 25, email: 'bob@example.com'},
  {name: 'Charlie', salary: 0},
  {name: 'Dave', email: 'dave@me.com'},
]

arrSalary = getPeopleWithSetSalary(arr); 
```
and `arrSalary` becomes
```
[
  {name: 'Alice', salary: 30},
  {name: 'Bob', salary: 25, email: 'bob@example.com'},
]
```

Instead, you should write:
```js
function getPeopleWithSetSalary(arr) {
  arr.filter(person => {
    return person.salary && !isNaN(person.salary);
  });
}
```

and `arrSalary` becomes

```
const arr = [
  {name: 'Alice', salary: 30},
  {name: 'Bob', salary: 25, email: 'bob@example.com'},
  {name: 'Charlie', salary: 0},
  {name: 'Dave', email: 'dave@me.com'},
]
```

as should be the case.

