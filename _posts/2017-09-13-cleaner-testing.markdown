---
layout: post
title:  "Cleaner Testing"
date:   2017-09-13 11:05:37 -0700
---

When there is a large suite of tests,
one should reuse the setup code

```python
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        self.company_people = {
        	'CEO': 'alice',
			'COO': 'bob',
			'Manager': 'charlie',
			'Receptionist': 'dave',
        }
        write_to_database(company_people)

    def test_transform_names_to_capitalized(self):
    	expected_company_people = {
        	'CEO': 'Alice',
			'COO': 'Bob',
			'Manager': 'Charlie',
			'Receptionist': 'Dave',
        }
    	assert transform_names_to_capitalized(self.company_people) == expected_company_people

   	def test_update_cleaner(self):
   		new_company_people = {
        	'CEO': 'Alice',
			'COO': 'Bob',
			'Manager': 'Charlie',
			'Receptionist': 'Dave',
			'Cleaner': 'Eve',
        }
        expected_company_people = {
        	'CEO': 'Alice',
			'COO': 'Bob',
			'Manager': 'Charlie',
			'Receptionist': 'Dave',
			'Cleaner': 'Flora',
        }
        assert update_cleaner('Flora') = expected_company_people
```

In this case, `test_add_cleaner` isn't the best way to do things,
because it is copying a large test value again,
that already appears in the set up.

Instead it would be better to refactor it to:

```python
def test_update_cleaner(self):
	self.company_people.update({'Cleaner': 'Eve'})
	assert self.company_people.get('Cleaner') == 'Eve' 
    assert add_cleaner('Flora').get('Cleaner') == 'Flora'
```

The above function makes it clear that the cleaner
before and after `update_cleaner` was called is different.
This saves on amount of code, and also makes it easier to understand what the test
is trying to verify.


