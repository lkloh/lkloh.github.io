---
layout: post
title:  "Designing Interfaces"
date:   2017-09-22
---

Interfaces should be designed to abstract 
away as much of the functionality as possible,
but sometimes it's tempting to include details of the implenentation
if it would consolidate things.

Here's an example: 

Extending the Person class from yesterday, people here can
transition their gender and update their name to reflect their new identify.

```js
Person {
    firstName: String;
    lastName: String;
    age: number;
    isMale: boolean;

    constructor(firstName: String, lastName: String, age: number, isMale: boolean) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.isMale = isMale;
    }
}

updatePerson(params): Person {
    return new Person(Object.assign({}, this, params));
}
```

Now, given the person below:

```js
const female = new Person({
    firstName: `Jane`,
    lastName: `Roe`,
    age: 21,
    isMale: false,
});
```

to transition this person from a female to a male and rename them, we could do:

```js
const male = female.updatePerson({firstName: `John`, isMale: false});
```

But this isn't the greatest thing to do, since it requires the person
using the `People` class to understand the underlying details of how
`updatePerson` is implemented.
And it isn't so clear to a new reader about what the above is doing.

Now contrast with this implementation of Person:

```js
Person {
    firstName: String;
    lastName: String;
    age: number;
    isMale: boolean;

    constructor(firstName: String, lastName: String, age: number, isMale: boolean) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.isMale = isMale;
    }
}

performSexChangeSurgery(isMale: boolean): Person {
    return new Person(Object.assign({}, this, {isMale}));
}

changeFirstName(firstName: String): Person {
    return new Person(Object.assign({}, this, {firstName}));
}
```


Now to transition the person, we could do

```js
const male = female
    .performSexChangeSurgery(true)
    .changeFirstName(`John`);
```

And its clear that the gender was changed, and so was the first name.
Furthermore, it's clear how to update the person's characteristics:
just call the function that changes a particular characteristic.
It's obvious from just looking the function signature, what
the type of the characteristic is.
