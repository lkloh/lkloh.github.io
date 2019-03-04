---
type: post
title: "In Django catch exceptions outside of an atomic block"
date: 2019-02-08
---

## Wrong way

```py
from django.db import IntegrityError, transaction

def view(request):
  with transaction.atomic():
    try:
      update_record(request)
    except IntegrityError:
      handle_exception()
```

If `handle_exception` was called inside the atomic block,
Django doesn't know a problem happended when it exited
the `atomic` block as the exception was already handled inside the block.
This can cause [unexpected behavior](https://docs.djangoproject.com/en/2.1/topics/db/transactions/).

## Right way

```py
from django.db import IntegrityError, transaction

def view(request):
  try:
    with transaction.atomic():
      update_record(request)
  except IntegrityError:
    handle_exception()
```

If an exception happens within `update_record`,
then an exception is called and Django exits the atomic block.
Django sees that an `IntegrityError` was called next,
and changes in `update_record` are rolled back.




