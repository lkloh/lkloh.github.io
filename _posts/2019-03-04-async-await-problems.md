---
type: post
title: "Async/Await problems"
date: 2019-03-04
---

Summarized from [here](https://medium.freecodecamp.org/avoiding-the-async-await-hell-c77a0fb71c4c).

People misusing async/await end up causing performance issues.
Let's look at an example.

```js
async function handleDinner() {
  const pizzaOrder = await getPizzaOrder(); // async call
  const drinkOrder = await getDrinkOrder(); // async call
  await placeOrder(pizzaOrder);
  await placeOrder(drinkOrder);
  eatDinner();
}
```

This function does the expected thing - placing an order for pizza and drinks.
However, it causes performance issues as the pizza order and drink orders
execute one-by-one, so there is no parallization.

To streamline things, consider that we don't need to wait
for the drink orders to be fulfilled before placing an order for pizza.
This achieves the same goal in less time:

```js
// group dependent calls in an async function
async function orderPizza() {
  const pizzaOrder = await getPizzaOrder(); // async call
  placeOrder(pizzaOrder);
}

// group dependent calls in an async function
async function orderDrinks() {
  const drinkOrder = await getDrinkOrder(); // async call
  await placeOrder(drinkOrder);
}

async function handleDinner() {
  // concurrently order pizza and drinks
  const pizzaPromise = orderPizza();
  const drinkPromize = orderDrinks();

  // wait for pizza and drinks to arrive before eating 
  await pizzaPromise;
  await drinkPromise;
  eatDinner();
}
```
