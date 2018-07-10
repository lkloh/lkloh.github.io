---
type: post
title: "Nothing is something"
date: 2018-07-10
---

This talk discusses the [Null object pattern](https://www.youtube.com/watch?v=OMPfEXIlTVE).
In summary, code is full of hidden assumptions,
and the talk explains how to expose those hidden assumptions to make the code easier to understand.
By being explicit about hidden ideas, your code becomes simpler and clearer.

If you're talking to a NULL object, you're talking to something, not nothing.
NULL refers to the empty value, not "nothing".
So you should use a NilClass to handle null objects instead of doing a check for `if (obj)` everywhere.

Null object pattern is called the "Active nothing",
and it can be used to reduce the number of `if` statements used in your code,
which will make your life easier the next time you do a big refactor.

In short, instead of writing

```js
_.each(animals, animal => {
  if (animal) {
    console.log(animal.name);
  } else {
    console.log('no animal');
  }
});
```

you want to use the null object pattern to handle the empty animal so you can write
```js
_.each(animals, animal => {
  console.log(animal.name);
});
```

which makes your code cleaner.

Oh, and don't use function inheritance, but instead function composition,
as its easier to combine the functionality of two children that inherited
from a parent, than to try and duplicate code from both the children.
It's known as dependency injection.






