---
type: post
title: "Beware of caching when deploying"
date: 2018-01-27
---

I was trying to add a new field to a class.
Something like this:

```py
# Old class
class Student:
  def __init__(self, first_name, last_name, birthday, citizenship):
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = birthday
    self.citizenship = citizenship

  def is_eligible_for_financial_aid(self):
    return self.birthday.year >= 1997

  def serialize(self):
    return {
      'first_name': self.first_name,
      'last_name': self.last_name,
      'birthday': self.birthday,
   }
```

Rules for financial aid got stricter due to budget cuts:

```py
# New class
class Student:
  def __init__(self, first_name, last_name, birthday, citizenship):
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = birthday
    self.citizenship = citizenship

  def is_eligible_for_financial_aid(self):
    return self.birthday.year >= 1997 and self.citizenship === 'USA'

  def serialize(self):
    return {
      'first_name': self.first_name,
      'last_name': self.last_name,
      'birthday': self.birthday,
      'citizenship': self.citizenship,
   }
```

Then I tried to deploy the new code, which included something like this

```py
LENGTH_OF_TIME_TO_CACHE = 3600

def obtain_students_getting_financial_aid(student_ids):
  students = [] 
  for id in student_ids:
      if cache.contains(id):
         students += [cache(id)]
      else:
         students += [query_for_student(id)
    
  return [s for s in students if s.is_eligible_for_finanial_aid()]
```

Naturally, this caused all sorts of failures, since the students in the cache kept getting returned,
so the deploy had to be rolled back.
Instead, the solution was to re-deploy without making use of the new field on
citizenship.


```py
# New class
class Student:
  def __init__(self, first_name, last_name, birthday, citizenship):
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = birthday
    self.citizenship = citizenship

  def is_eligible_for_financial_aid(self): # Use old version
    return self.birthday.year >= 1997 # and self.citizenship === 'USA'

  def serialize(self):
    return {
      'first_name': self.first_name,
      'last_name': self.last_name,
      'birthday': self.birthday,
      'citizenship': self.citizenship,
   }


## Script using the updated Student class
LENGTH_OF_TIME_TO_CACHE = 3600

def obtain_students_getting_financial_aid(student_ids):
  students = [] 
  for id in student_ids:
      if cache.contains(id):
         students += [cache(id)]
      else:
         students += [query_for_student(id)
    
  return [s for s in students if s.is_eligible_for_finanial_aid()]
```

Then wait for an hour for the cache to be repopulated, 
then deploy the new code with the additional conditional to check for citizenship.

Beware of what you have in the cached if you're changing the schema of some data structures in any way.

