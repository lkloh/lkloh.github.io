---
layout: post
title:  "Describing mocha tests properly"
date:   2017-08-02
---

There's more [here](http://samwize.com/2014/02/08/a-guide-to-mochas-describe-it-and-setup-hooks/) 
on how to write good tests and set them up,
so I tried implementing them in practice on an example function.
The entire repo of tests described in this article is 
[here](https://github.com/lkloh/javascriptPlayground/tree/master/mochaTestExample_aug2_2017).

Given this javascript function to test:

```js
isLeapYear: function(year) {
	if (Number.isInteger(year) && (year >= 0)) {
		if (year % 4 == 0) {
			if (year % 100 == 0) {
				if (year % 400 == 0) {
					return true;
				} else {
					return false;
				}
			} else {
				return true;
			} 
		} else {
			return false;
		}
	} else {
		throw 'Year must be an integer >= 0';
	}
}
```

Good tests are descriptive english of what you expect the function to do:
```js
var assert = require('assert');
var typesOfYears = require('./typesOfYears');

describe('isLeapYear', function() {
	describe('for years divisible by 4', function() {
	  	it('should return "true" when the year is not multiple of 100', function() {
		  	assert.equal(typesOfYears.isLeapYear(1996), true);
		});

		it('should return "false" when the year is a multiple of 100, and not a multiple of 400', function() {
		  	assert.equal(typesOfYears.isLeapYear(1900), false);
		});

		it('should return "true" when the year is a multiple of 400', function() {
		  	assert.equal(typesOfYears.isLeapYear(2000), true);
		});
	});

	describe('for years not divisible by 4', function() {
	  	it('should return "false" when the year is not multiple of 100', function() {
		  	assert.equal(typesOfYears.isLeapYear(2001), false);
		});
	});
});
```

while bad tests focus too much on implementation details.
```js
var assert = require('assert');
var typesOfYears = require('./typesOfYears');

describe('isLeapYear', function() {
	it('(year % 4 == 0) and (year % 100 != 0) ==> false', function() {
	  	assert.equal(typesOfYears.isLeapYear(1996), true);
	});

	it('(year % 400 != 0) ==> false', function() {
	  	assert.equal(typesOfYears.isLeapYear(1900), false);
	});

	it('(year % 400 == 0) ==> true', function() {
	  	assert.equal(typesOfYears.isLeapYear(2000), true);
	});

	it('(year % 4 != 0) ==> false', function() {
		assert.equal(typesOfYears.isLeapYear(2001), false);		
	});
});
```

Its awfully easy to write bad tests that describe how the function is implemented,
because I've already written it once by the time I've got there.
Something to be careful about for the future.


