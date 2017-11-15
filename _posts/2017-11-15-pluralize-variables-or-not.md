---
layout: post
title:  "To pluralize variables or not"
date:   2017-11-15
---

Recently I wrote something like this:
```js
var errorMessageArray = ['This is incorrect', 'Even more wrong', 'No.', 'Wrong number'];
```

And someone suggested changing it to 

```js
var errorMessages = ['This is incorrect', 'Even more wrong', 'No.', 'Wrong number'];
```

for conciseness.

Stack Overflow is [divided](https://stackoverflow.com/questions/395739/do-you-name-your-arrays-plurally-or-singularly) 
on whether it is better to call it `errorMessages` or `errorMessageArray`.

Seems that its better to follow whatever other people prefer to use, 
as here are some arguments for either case:

## Using errorMessages

Concise

## Using errorMessageArray

Specifies the type clearly (its an array, not a set!)
