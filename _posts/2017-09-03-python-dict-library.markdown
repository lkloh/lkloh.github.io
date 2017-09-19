---
layout: post
title:  "Accessing dictionary values in Python"
date:   2017-09-03 10:37:34 -0700
---

The last post was about dictionaries in Javascript.
This one will be about dictionaries in Python.

Given a dictionary that of form:

```python
alice_user_profile = {
	'first_name': 'Alice',
	'last_name': 'Anderson',
	'age': 42,
	'gender': 'female',
	'owns_a_house: True,
}
```

You have to access dictionary values using bracket notation: 
`user_profile['first_name'] = 'Alice`.
Dot notation is not enabled for dictionaries, so
`user_profile.first_name` throws an error.

If we wanted to write a function that only does something if an attribute is present:
for example, if these profiles are all possible: 

```python
alice_user_profile = {
	'first_name': 'Alice',
	'last_name': 'Anderson',
	'age': 42,
	'gender': 'female',
	'owns_a_house: True,
}

bob_user_profile = {
	'first_name': 'Bob',
	'last_name': 'Brown',
	'age': 21,
	'gender': 'male',
}

charlie_user_profile = {
	'first_name': 'Charlie',
	'last_name': 'Chaplin',
	'age': 35,
	'gender': 'male',
	'owns_a_house: False,
}
```

and we only want to send an advertisement for homeowner's insurance to people
who own a house, we could do something like this

```python
def send_advertisement_to_select_people(user_profile):
	if ('college' in user_profile) and user_profile['college']:
		send_homeowner_ad(user_profile)
```

but it would be more concise to do this:


```python
def send_advertisement_to_select_people(user_profile):
	if user_profile.get('owns_a_house'):
		send_homeowner_ad(user_profile)
```

since the `.get` function will return `True` if the user owns a house,
and `False` if he does not, or the attribute `owns_a_house` is not set.

Good reason to [read the docs](https://www.tutorialspoint.com/python/python_dictionary.htm) 
more carefully.




