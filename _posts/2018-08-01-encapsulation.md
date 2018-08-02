---
type: post
title: "OOP Encapsulation"
date: 2018-08-01
---

I was working on a class like this:

```js
// filename: student.js
function Student(name, gpa, phone) {
  this.name = name;
  this.gpa = gpa;
  this.phone = phone;
}

function getName() {
  return this.name;
}

function getPhone() {
  return this.phone;
}
```

and I had a method using the `student` class as such:
```js
// filename: manipulate_student.js
const student = new Student(`John`, 3.45, 123-456-7890)
```

and I really wanted to update his GPA, so I did this
```js
// filename: manipulate_student.js
const student = new Student(`John`, 3.45, 123-456-7890)
student.gpa = 3.54;
```

Though what I really should have done to avoid manipulating a structure that `manipulate_student.js`
didn't have access to was this:


```js
// filename: student.js
function Student(name, gpa, phone) {
  this.name = name;
  this.gpa = gpa;
  this.phone = phone;
}

// add new function
function updateGpa(newGpa) {
  this.gpa = newGpa;
}

function getName() {
  return this.name;
}

function getPhone() {
  return this.phone;
}
```

and then call the new function to update the gpa.


```js
// filename: manipulate_student.js
const student = new Student(`John`, 3.45, 123-456-7890)
student.updateGpa(3.54);
```

Somehow it wasn't as obvious what to do when I was looking at a big hairy legacy file instead 
of a toy example like that for illustration.


