---
layout: post
title:  "Temporary features"
date:   2017-12-13
---

When developing temporary features - eg stuff for a beta release, 
here are things to keep in mind:

## Do

Make it a component of its own if possible.
Try to avoid integration with the main codebase,
so it is easy to remove.
Even if you have to copy some code from other parts 
- its ok! Copy what you need over to the temporary component.

Remember to remove it.

## Don't

Obsess over the code being perfectly intuitive to read. It's temporary.


