---
type: post
title: "The importance of consistency in APIs"
date: 2018-05-19
---

## Consistent way - best practice

```py
def get_student_details(self, id):
  return {
    'first_name': self.get_first_name(id),
    'last_name': self.get_last_name(id),
    'email': self.get_email(id),
    'middle_name': self.get_middle_name(id),
  }
```

## Not ideal

```py
def get_student_details(self, id):
  result = {
    'first_name': self.get_first_name(id),
    'last_name': self.get_last_name(id),
    'email': self.get_email(id),
  }
  if self.under_house_arrest(id):
    result['middle_name'] = self.get_middle_name(id)
  return result
```

Even if you only need the middle name in certain situations,
it is best for consistency to return the middle name in all circumstances,
even if you have to change ~200 unit tests after the refactor.


