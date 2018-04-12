---
type: post
title: "Python comments and docstrings"
date: 2018-04-11
---

## Docstrings

Are use for modules and functions, for instance

```py
def update_user_gender(self, user_id, new_gender):
  '''
  Updates the user's gender and number of people with that gender.
  '''
  if self.users[user_id].gender != new_gender:
    self.users[user_id].gender = new_gender
    self.census[new_gender] += 1
```

## Comments

Are for commenting within a function, for instance

```py
def test_update_user_gender(self):
  # set up test environment
  user = make_fake_user(gender='Male')
  census = {'Male': 0, 'Female': 0)
  self.assertEqual(user.gender, 'Male')
  self.assertEqual(census['Male'], 1)
  self.assertEqual(census['Female'], 0)

  # update gender
  update_user_gender(user.id, 'Female')

  # Ensure counts changed
  self.assertEqual(user.gender, 'Female')
  self.assertEqual(census['Male'], 0)
  self.assertEqual(census['Female'], 1)
```


