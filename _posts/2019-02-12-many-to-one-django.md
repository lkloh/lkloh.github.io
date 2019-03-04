---
type: post
title: "Many-to-one django"
date: 2019-02-12
---

Summarized from [here](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/)

Given a model of a people manager who manages multiple employees
```py
from django.db import models

class Manager(model.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
```

and an employee model, in which each employee only has one manager:
```py
from django.db import models

class Employee(model.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
```

you can get all the employees that a manager manages like this:
```py
john = Manager.objects.create(name='John', email='john@company.com')

alice = Employee.objects.create(name='Alice', email='alice@company.com')
bob = Employee.objects.create(name='Bob', email='bob@company.com')
charlie = Employee.objects.create(name='Charlie', email='charlie@company.com')

employee_emails = [employee.email for employee in john.employee_set.all()]
```





