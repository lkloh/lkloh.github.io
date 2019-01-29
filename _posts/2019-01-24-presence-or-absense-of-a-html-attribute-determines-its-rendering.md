---
type: post
title: "Presense or absense of a HTML attribute determines its rendering"
date: 2019-01-24
---

The are several ways to disable a button.

That
```
<button disabled>Click me</button>
<button disabled="disabled">Click me</button>
```
would work seems hardly surprising, but how about this?
Why do they both work?
```
<button disabled=true>Click me</button>
<button disabled=false>Click me</button>
```

Most major browsers check for the presense of the `disabled` attribute alone
to decide whether the button should be disabled or not.
The value of the attribute itself is irrelevant.

See more [here](https://stackoverflow.com/questions/6961526/what-is-the-correct-value-for-the-disabled-attribute).

