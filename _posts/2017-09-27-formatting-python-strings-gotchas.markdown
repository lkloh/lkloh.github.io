---
layout: post
title:  "Gotchas when formatting Python Strings"
date:   2017-09-27
---

Given a name stored as a unicode variable, `name = u'John Doe`,
and a desired to print a welcome message, there are three ways to do it right now:

```py
username = u'John Doe'
welcome_message_1 = 'Hello, %s' % username
welcome_message_2 = 'Hello, ' + username
welcome_message_3 = 'Hello, {name}'.format(name=username)
```

Which should you choose?

Python 3 will require you to use `.format()`,
but there are some gotchas.
First of all,
all of the welcome messages will give you `Hello, John Doe` as expected.
But the difference is that we have
`welcome_message_1 = u'Hello, John Doe' = welcome_message_2`
so the entire message is converted unicode as the `username` is in unicode.

However, `welcome_message_3 = 'Hello, John Doe'` is still a string.
This can cause issues in certain functions if they are expecting unicode 
but you're passing in a string.
I just spent almost an entire day debugging this because I wanted
to be clever and optimize for the future of Python.



