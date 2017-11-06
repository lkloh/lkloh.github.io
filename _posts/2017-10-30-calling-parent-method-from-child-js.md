---
layout: post
title:  "Calling a parent method from a child method in JavaScript"
date:   2017-10-30
---

Given this parent class

```
class Parent {

	constructor(firstname, lastname, age, bankBalance) {
		this.firstname = firstname;
		this.lastname = lastname;
		this.age = age;
		this.bankBalance = bankBalance;
	}

	goShopping(itemValue) {
		this.updateBankBalance(itemValue, '-');
		this.updateBankBalance(itemValue * 0.05, '+');

		this.age += 10;
	}

	updateBankBalance(delta, operator) {
		if (operator === '+') {
			this.bankBalance += delta;
		} else if (operator === '-') {
			this.bankBalance -= delta;
		} else {
			throw new Exception('invalid operator');
		}
	}

}
```

And this child class that calls a parent function

```
class ChildForeverRich extends Parent {

	constructor(firstname, lastname, age, bankBalance) {
		super(firstname, lastname, age, bankBalance);
	}

	goShopping(itemValue) {
		var FOREVER_RICH = 1000;
		Parent.prototype.goShopping.call(this, itemValue); // call parent function
		this.bankBalance = FOREVER_RICH;
	}
}

alice = new ChildForeverRich('Alice', 'ForeverRich', 21, 100);

console.log(alice);
alice.goShopping(10);
console.log(alice);
```
alice is rich as she updated the bank balance back to $1000 after shopping.


```
class ChildNotSoRich extends Parent {

	constructor(firstname, lastname, age, bankBalance) {
		super(firstname, lastname, age, bankBalance);
	}

	goShopping(itemValue) {
		var FOREVER_RICH = 1000;
		this.bankBalance = FOREVER_RICH;
		Parent.prototype.goShopping.call(this, itemValue); // call parent function
	}
}

bob = new ChildNotSoRich('Bob', 'NotSoRich', 21, 100);
console.log(bob);
bob.goShopping(10);
console.log(bob);
```

Bob is not so rich as he updated the bank balance before shopping,
and his shopping draws a percentage of his bank balance.

Be careful about the order in which things are done when calling a parent function.


