---
type: post
title: "Who should be an instance method on a class?"
date: 2018-11-12
---

Given this class,

```js
class Person {
  constructor(firstname, lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
  }

  updateLastname(newLastname) {
    this.lastname = newLastname;
  }

  get name() {
    return this.format_name(this.firstname, '', this.lastname);
  }

  format_name(first, middle, last) {
    const array = [first, middle, last];
    return array.join(' ');
  }
}
```

we should rewrite it to

```js
format_name(first, middle, last) {
  const array = [first, middle, last];
  return array.join(' ');
}

class Person {
  constructor(firstname, lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
  }

  updateLastname(newLastname) {
    this.lastname = newLastname;
  }

  get name() {
    return format_name(this.firstname, '', this.lastname);
  }
}
```

and pull out functions that don't need access to `this` within the class.
They don't need to be instance methods and clog up the class.






