---
type: post
title: "Grep for instance of a class to update them after modifying the class itself"
date: 2018-04-04
---

There was a class that did something like this:
```py
class VisualElementsForPage:
  def __init__(self, height, width, background_color='black', color='white', font_size):
    self.height = height
    self.width = width
    self.background_color = 'white'
    self.color = color
    self.font_size = font_size

  def update_color(self, new_color):
    self.color = new_color
  
  def update_background_color(self, new_background_color):
    self.background_color = background_color
```

I updated the class to do something like:
```py
class VisualElementsForPage:
  def __init__(self, height, width, background_color='black', color='black', font_size):
    self.height = height
    self.width = width
    self.background_color = 'white'
    self.color = color
    self.font_size = font_size

  def update_color(self, new_color):
    self.color = new_color
  
  def update_background_color(self, new_background_color):
    self.background_color = background_color
```

and then updated one instance of the class to be
```py
VisualElementsForPage(10, 20, 12, color='green')
```

There was another instance of the class I forgot to update, so it continue to be
```py
VisualElementsForPage(10, 20, 12)
```
and now it showed a black font on a black background.

See the problem?

What I really should have done after updating `VisualElementsForPage` was to do a 
`git grep VisualElementsForPage` in the entire repository look for everywhere 
an instance of that class existed an update _all__the instances.

Lesson learnt, hopefully.



