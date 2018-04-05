---
type: post
title: "Different types of software tests"
date: 2018-03-29
---

Summarized from [here](https://www.atlassian.com/continuous-delivery/different-types-of-software-testing).

## Unit tests

Test individual methods and functions of classes or components.
Can be run quickly be a continuous integration server.

```py
# Example function
def double_number(num):
  return 2 * num

# Example test
def test_double_number(self):
  self.assertEqual(0, double_number(0))
  self.assertEqual(-2, double_number(-1))
  self.assertEqual(2, double_number(1))
```

## Integration tests

Verify that different modules or services used by an application work together properly.

Example: Make sure the web app saves user's data to the database 
in the correct format.

Expensive to run as multiple parts of the application must be up.

## Functional test

Verify the output of an action only,
do not check intermediate states.
  Used to ensure business requirements are going to be met.

Example: Given that an underage child tries to sign up for a shopping website
which requires users to be at least 18 years old,
confirm the website denies the child's request.

Different from integration tests: 
An integration test may just verify the user's information
can be successfully saved to the database.

## End-to-end tests

Simulate a user using the application.
May verify a user can log in,
pay with a credit card,
receive email from an online campaign, etc.

Expensive to run,
troublesome to maintain as the webapp keeps evolving.

## Acceptance tests

Verify a system satisfies business requirements
by simulating a user.

## Performance tests

Ensure a system can handle unexpected load
(e.g. a magazine with a small number of regular readers
is about to publish an article about Kim Kardashian 
breaking the internet).

## Smoke tests

Tests that check basic functionality of an application.
Must run quickly.
Goal is the assume you that basic features of an application
are still working alright. 
Useful to run before more expensive tests.
If the smoke test fails => throw an error immediately, do not run expensive end-to-end tests.












