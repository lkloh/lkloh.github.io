---
layout: post
title:  "Writing readable code"
date:   2017-09-25
---

Today I saw some code that looked a little bit like this:
```js
Student {
    firstName: String;
    lastName: String;
    age: number;
    isFreshman: boolean;

    constructor(firstName: String, lastName: String, age: number, isFreshman: boolean) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.isFreshman = isFreshman;
    }

    isNonTraditionalStudent(): boolean {
    	const under18 = this.age < 18;
    	const aFreshman = this.isFreshman;
    	return (under18 and not aFreshman) or (not under18 and aFreshman);
    }
}
```

Traditional freshmen are usually 18 years old.
Any student who is under 18 and not a freshman (unusually young to start college),
or above 18 but still a freshman (ususually old to start college),
is considered to be a non-traditional student. 
On this post anyway.

The function `isNonTraditionalStudent` could be rewritten more concisely as:

```js
isNonTraditionalStudent(): boolean {
	return (this.age < 18) ^ (this.isFreshman);
}
```
since it just checks that (this.age < 18) and (isFreshman)
must have the same truth value,
but then it's not immediately obvious what this function is checking for,
though it uses less lines of code.

So optimize for readability over conciseness.









