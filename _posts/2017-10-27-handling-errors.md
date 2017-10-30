---
layout: post
title:  "Handling errors"
date:   2017-10-27
---

Recently I wrote a function that only a developer with 
access to the private repo would use.
No external customers would ever know that function exists.
```py
class Employee:
    def __init__(self, firstname, lastname, salary, bonus=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.bonus = bonus

    def print_employee(self):
        print 'Employee %s %s has a salary of $%d and bonus of $%d' % (self.firstname, self.lastname, self.id, self.salary, self.bonus)


_employees = [
    Employee('Alice', 'Anderson', 120, bonus=5),
    Employee('Bob', 'Brown', 95, bonus=20),
    Employee('Charlie', 'Chaplin', 95, bonus=20),
];

def get_existing_ids(id_list):
  return list(filter(lambda id: id in xrange(len(_employees)), id_list))

def update_employees_salary_by_5(id_list):
  
  for id in id_list:

    
```



## External functions

Handling them carefully, with strong defenses.
Do your best effort.

## Internal functions

Anything goes wrong: fail fast and noisly right there.
Otherwise you risk someone screwing up part of your system without realising it.
This could be long and painful to recover from.