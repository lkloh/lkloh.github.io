---
layout: post
title:  "Pure functions"
date:   2017-09-10 11:05:37 -0700
---

[Pure functions](https://www.sitepoint.com/functional-programming-pure-functions/)
have a return value determined only by its input values,
and not other states.

For example:
```python
def capitalize_dict__pure(dict_of_strings):
	return {key: val.capitalize() for key, val in dict_of_strings.items() if key != 'CEO' else val}
``` 
is a pure function as the return value depends only on the dictionary passed in.

But
```python
def capitalize_dict__impure(dict_to_modify):
	for key in dict_to_modify:
		if key != 'CEO':
			dict_to_modify[key] = val.capitalize()
``` 
modifies one of the return value `dict_to_modify`,
and thus changes some data outside the function,
so is not pure.

It is good practice to use pure functions where possible,
as it is easier to test and maintain them.
One does not have to worry about side effects.

It is obvious how to test the first function:
```python
def test_empty_dict_returns_empty():
	assert capitalize_dict__pure({}) == {}

def test_ceo_is_not_changed():
	company_people = {
		'CEO': 'alice',
		'COO': 'bob',
		'Manager': 'charlie'
	}
	assert capitalize_dict__pure(company_people) != company_people
	expected_company_people = {
		'CEO': 'alice',
		'COO': 'Bob',
		'Manager': 'Charlie'
	}
	assert capitalize_dict__pure(company_people) == expected_company_people
```


But the second function could exhibit different behavior depending on the functions that call it.
For example, if we have this function that we want to test instead, because it is hard
to test `capitalize_dict__impure` when it could change,
we may instead test the functions that call it:

```python
def get_ceo_name(company_people):
	capitalize_dict__impure(dict_to_modify)
	company_people['CEO'] = 'Alison'
	return company_people['CEO']

def get_ceo_name_formatted(company_people):
	return capitalize_dict__impure(company_people)['CEO']
```

Then we need separate tests for both the parent functions of `capitalize_dict__impure`.

```python
def get_ceo_name():
	company_people = {
		'CEO': 'alice',
		'COO': 'bob',
		'Manager': 'charlie'
	}
	assert get_ceo_name(company_people) == 'Alice' // fails

def get_ceo_name_formatted():
	company_people = {
		'CEO': 'alice',
		'COO': 'bob',
		'Manager': 'charlie'
	}
	assert get_ceo_name(company_people) == 'Alice' // correct
```

And it is easier to get unexpected behavior that requires
more digging to fix.





