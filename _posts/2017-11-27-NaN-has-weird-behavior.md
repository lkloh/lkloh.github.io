---
layout: post
title:  "NaN behaves weirdly"
date:   2017-11-27
---

I was trying write a class somewhat like this:
```js
class Person {
	constructor(firstName, lastName, birthday, salary) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.birthday = birthday;
		this.salary = Number.isNumber(salary) ? salary : '';
	}
}
```
Most people (at least in the United States),
have a first name, last name, and birthday that is known.
Not everyone has a salary. 
For example, babies do not work.

```js
father = new Person('Harry', 'Potter', '07-31-1980', '7777');
son = new Person('Albus', 'Potter', '07-31-2009', 'No Salary available');
```

Then the `son`'s salary gets transformed to an empty string.

## Problem 1: Better to store non-existent values as NULL

`null` in JavaScript is meant to designate a variable is having no value. 
Should use `null` to represent no salary, instead of empty string.

## Problem 2: Don't use NaN to represent an non-existent number

I could have written
```js
class Person {
	constructor(firstName, lastName, birthday, salary) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.birthday = birthday;
		this.salary = Number.isNumber(salary);
	}
}
```
and then when no salary is available, it gets stored as `NaN`.
Unfortunately, `NaN` in JavaScript has weird behavior.
For example, `NaN != NaN`.

## Conclusion

Use `null` in JavaScript to represent a variable that has no value.
Not an empty string, not a NaN, not -1, and certainly not Undefined.
All those have potential for misintepretation
and can cause problems when using them for comparison later on.









