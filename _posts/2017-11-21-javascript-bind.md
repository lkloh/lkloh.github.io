---
layout: post
title:  "JavaScript Bind"
date:   2017-11-21
---

Recently saw a bug that occurred because someone forgot to 
bind `this` to an iframe, 
but still replied on the context of `this`.
Here's a [useful discussion](https://stackoverflow.com/questions/2236747/use-of-the-javascript-bind-method) 
about how you can bind `this` to new objects.

## Did not bind this

```
function Rachel() {
   this.name = 'Rachel Green';
   this.total = 500;
   console.log(getMonthlyFee()); // error, this.name and this.total not specified
}


function getMonthlyFee() {
  	var remaining = this.total - 50;
	this.total = remaining;
	return this.name +' remaining balance:' + remaining;
}

new Rachel();
```



## With binding this

```
function Rachel() {
   this.name = 'Rachel Green';
   this.total = 500;
   var rachelFee = getMonthlyFee.bind(this);
   console.log(rachelFee()); // prints 'Rachel Green remaining balance: 450'
}


function getMonthlyFee() {
  	var remaining = this.total - 50;
	this.total = remaining;
	return this.name +' remaining balance:' + remaining; 
}

new Rachel();
```




