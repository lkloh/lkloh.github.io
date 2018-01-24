---
type: post
title: "Django classmethods"
date: 2018-01-24
---

Summarized from [here](https://stackoverflow.com/questions/2213309/django-model-class-methods-for-predefined-values).

Given a Django class like this:
```
class Animal(models.Model):
  name = models.CharField(maxlength=255)
  age = models.IntegerField()
```

and some animals in the database like this:
```
----------
name: "Cow"
age: 5
----------
name: "Sheep"
age: 1
----------
name: "Chicken"
age: 1
----------
name: "Dog"
age: 15
----------
name: "Cat"
age: 6
----------
```

To find the methods to obtain the number of animals <= 5 years old
and > 5 years old, do NOT do this:

```py
class Animal(models.Model):
  name = models.CharField(maxlength=255)
  age = models.IntegerField()

  @classmethod
  def below_five(cls):
    return len([animal.age <= 5 for animal in Animal.objects.all()])

  @classmethod
  def above_five(cls):
    return len([animal.age > 5 for animal in Animal.objects.all()])
```

But instead the Django way to do things is to seperate the way a single Animal
is defined, versus how a table of animals are defined.

```
class Animal(models.Model):
  '''Works for a particular Animal'''
  name = models.CharField(maxlength=255)
  age = models.IntegerField()

  objects = AnimalManager()


class AnimalManager(models.Manager):
  '''Works for a table of animal'''
  def below_five(self):
    return len([animal.age <= 5 for animal in self.all()])

  def above_five(self):
    return len([animal.age > 5 for animal in self.all()])
```

