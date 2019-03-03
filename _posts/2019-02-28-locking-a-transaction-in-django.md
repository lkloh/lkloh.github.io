---
type: post
title: "Locking a series of steps to avoid race conditions in Django"
date: 2019-02-28
---

I was trying to write a backend function to update attributes of a student record:
```
# models.py
from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=60)
  gpa = models.IntegerField(default=0)

  @classmethod
  def update(student_id, name, address, gpa):
    records = Student.objects.filter(id=student_id)
    if records.count() == 0:
      raise Exception('No record for student with student id %d exists' % student_id)

    student = records.first()
    if name is not None:
      student.update(name=name)
    elif address is not None:
      student.update(address=address)
    elif gpa is not None:
      student.update(gpa=gpa)
    else:
      raise Exception('Need to update one of name, addres, or gpa')
```

and

```
# view.py

def update_student(request, student_id):
  records = Student.objects.filter(id=student_id)
  if records.count() > 0:
    student = records.first()
  if 'name' in request.POST:
    Student.update(
      student_id,
      request.POST['name'],
      address=student.address,
      gpa=student.gpa)
  elif 'address' in request.POST:
    Student.update(
      student_id,
      student.name,
      address=request.POST['address'],
      gpa=student.gpa)
  elif 'gpa' in request.POST:
    Student.update(
      student_id,
      student.name,
      address=student.address,
      gpa=request.POST['gpa'])
  else:
    return HttpResponseBadRequest('Invalid params: must be one of first_name, addres, or gpa')
  
  return JsonResponse({'success': True})
```

To avoid having the student records change due to to people updating the
records of a student at the same time, I had to lock things.
```
# view.py
from django.db import transaction

def update_student(request, student_id):
  # Lock the row containing the records of the student with student_id until end of transaction
  # All other transcations cannot acquire the lock for student_id until this transaction is done
  # SQL statement: SELECT student.id=student_id ... FOR UPDATE 
  with transaction.atomic():  
    records = Student.objects.filter(id=student_id)
    if records.count() > 0:
      student = records.first()
    if 'name' in request.POST:
      Student.update(
        student_id,
        request.POST['name'],
        address=student.address,
        gpa=student.gpa)
    elif 'address' in request.POST:
      Student.update(
        student_id,
        student.name,
        address=request.POST['address'],
        gpa=student.gpa)
    elif 'gpa' in request.POST:
      Student.update(
        student_id,
        student.name,
        address=student.address,
        gpa=request.POST['gpa'])
    else:
      return HttpResponseBadRequest('Invalid params: must be one of first_name, addres, or gpa')
    
    return JsonResponse({'success': True})
```

Read more [here](https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-for-update).

