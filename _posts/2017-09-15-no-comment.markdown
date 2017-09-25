---
layout: post
title:  "No comment"
date:   2017-09-15
---

Comments are supposed to be good.
At least, that what my [introductory computer science class's](http://web.stanford.edu/class/cs106a/)
lecturer said repeatedly.
In fact, we were docked points for bad style when we have no comments.

So naturally I freaked out and commented every. single. function. I wrote,
usually after I had finished the entire program,
so that I wouldn't lose points.

Eventually I learnt to only write comments to 
explain what some code was doing in a function.
In the following example taken from [here](https://github.com/django/django), 
I would probably have written something like

```python
def body(self):
    if not hasattr(self, '_body'):
        # Ensure request has not been read yet
        if self._read_started:
            raise RawPostDataException("You cannot access body after reading from request's data stream")

        # Limit the maximum request data size that will be handled in-memory.
        if (settings.DATA_UPLOAD_MAX_MEMORY_SIZE is not None and
                int(self.META.get('CONTENT_LENGTH') or 0) > settings.DATA_UPLOAD_MAX_MEMORY_SIZE):
            raise RequestDataTooBig('Request body exceeded settings.DATA_UPLOAD_MAX_MEMORY_SIZE.')

        # Obtain body
        try:
            self._body = self.read()
        except IOError as e:
            raise UnreadablePostError(*e.args) from e
        self._stream = BytesIO(self._body)
    return self._body
```

But that's still no good, too much of implementation details,
and implementations change fairly often.
Either you'll remember to change the comments after fixing the implementations,
or most likely you'll forget it, and the comment will become wrong after a while.
I've done that more than once.
And obviously a wrong comment is worst than no comment because it just confuses
other people who read it.

Instead, its better to refactor the code until its self-explanatory.
No need to update comments, and the code base is kept as lean as possible.

Something like:
```python
def body(self):
    if not hasattr(self, '_body'):
        if self._read_started:
            raise RawPostDataException("You cannot access body after reading from request's data stream")
        if (settings.DATA_UPLOAD_MAX_MEMORY_SIZE is not None and
                int(self.META.get('CONTENT_LENGTH') or 0) > settings.DATA_UPLOAD_MAX_MEMORY_SIZE):
            raise RequestDataTooBig('Request body exceeded settings.DATA_UPLOAD_MAX_MEMORY_SIZE.')
        try:
            self._body = self.read()
        except IOError as e:
            raise UnreadablePostError(*e.args) from e
        self._stream = BytesIO(self._body)
    return self._body
```

Obviously add comments if a particular implementation is really obscure,
and there's no easy way to make it more obvious. 
Or if several other contributors demand you to add it in because they think its obsure.
But in general it's best to err on the side of avoiding comments.

Now if only when in college,
I didn't spend 2 hours after getting my code to compile, 
writing extra comments on code I was never going to reuse,
I would have gotten more sleep.

