---
layout: post
title:  "Operator Precedence"
date:   2017-11-27
---

Here's how [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence) works in JavaScript. Long, long list of rules, too long to keep in my head. Lots of people suggest putting parentheses around them to avoid confusion, but this looks bad too:

```
return ((a && (!b)) || (((c.length >= 2) && (!d)) || _.isEmpty(e)))
```

Same rule: no more than three levels of parentheses anywhere.
And try to eliminate some parentheses, they don't necessarily make stuff look neater either.
```
var comboA = a && !b;
var comboB = c.length >= 2 && !d
return comboA || comboB || _.isEmpty(e)
```