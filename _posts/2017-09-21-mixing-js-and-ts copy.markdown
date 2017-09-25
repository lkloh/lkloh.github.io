---
layout: post
title:  "Mixing Javascript and Typescript"
date:   2017-09-21 11:05:37 -0700
---

Suppose this is in TypeScript: 
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

performSexChangeSurgery(isMale = true): Person {
    return new Person(Object.assign({}, this, isMale));
}
```

And this bit of code uses that TypeScript model, but is written in JavaScript:
```js
const femaleAlex = new Person({
    firstName: `Alex`,
    lastName: `Roe`,
    age: 21,
    isMale: false,
});
const maleAlex = femaleAlex.performSexChangeSurgery({isMale: true});
```

Then the code will compile and work just fine.

The problem is that this is wrongly typed.
`performSexChangeSurgery` is called with a JavaScript object `{isMale: true}`,
but the function signature (in TypeScript) requires the argument to be a boolean.

But this bit of code is not caught by the compiler,
since JavaScript is dynamically typed, and this `performSexChangeSurgery`
just needs to be given some sort of Object.
And the function `performSexChangeSurgery` demands an argument that is an object.
In particular, it demands a boolean, which is a JavaScript Object.

The right way to write the JavaScript portion is

```js
const femaleAlex = new Person({
    firstName: `Alex`,
    lastName: `Roe`,
    age: 21,
    isMale: false,
});
const maleAlex = performSexChangeSurgery(true);
```

The pains of transitioning to new technology halfway in a large codebase.




