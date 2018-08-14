---
type: post
title: "Displaying a truncated list"
date: 2018-07-30
---

I wanted to format a tooltip for a list of fruits that could get really long,
so I was only going to format at most 3 fruits and truncate the rest.

## Before

```
.pug file

- var fruits = formatElements()
- var MAX_ITEMS_TO_DISPLAY = 3
for fruit, index in fruits
  if index < MAX_ITEMS_TO_DISPLAY
    if index > 0
      |
      .inline_text and
    - var formatted_fruit = fruit
    include `format_fruit_file`
- var num_remaining_fruits = fruits.length - MAX_ITEMS_TO_DISPLAY
if num_remaining_fruits > 0
  .inline_text ` and ${num_remaining_fruits} other fruits`
```

```js
.js file

function formatElements() {
  const formatted = [];
  this.fruits.forEach(fruit => {
    formatted.push(_.pick(fruit, [`name`, `color`]));
  });
  return formatted;
}
```

But I should really have shifted as much of the business logic into the 

## After

```
.pug file

- var fruits = formatElements(raw_fruits)
for fruit in fruits
  if fruit.item
    - var formatted_fruit = fruit.item
    include `format_fruit_file`
  .inline_text fruit.connector
```

with a simple HTML file as desired and most of the logic shifted into a JS function
which is also more easily testable.

```js
.js file

function formatElements(fruits) {
  const formatted = [];
  const MAX_ITEMS_TO_DISPLAY = 3;
  fruits.forEach((fruit, index) => {
    if (index < MAX_ITEMS_TO_DISPLAY) {
      formatted.push({
        'item': _.pick(fruit, [`name`, `color`]),
        'connector': 'and',
      });
    }
  });
  const num_remaining_fruits = fruits.length - MAX_ITEMS_TO_DISPLAY;
  if (num_remaining_fruits > 0) {
    formatted.push({
      'item': null,
      'connector': ` and ${num_remaining_fruits} other fruits.`,
    });
  }
  return formatted;
}
```


