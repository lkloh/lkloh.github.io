---
type: post
title: "Typing Unicode"
date: 2018-03-25
---

Some ways to type in Unicode, see [here](https://www.w3schools.com/charsets/ref_utf_misc_symbols.asp) for more.

## Github

Decimal
* Star, `&#9733;`: &#9733;
* Telephone, `&#9742;`: &#9743;
* Hearts, `&#9829;`: &#9829;

## Python2

Hex
```py
print u'Check \u2611 for "yes" and \u2612 for no'
```

prints out: Check &#2611; for "yes" and &#2612; for no

## Python 3

Hex
```py
print('Check \u2611 for "yes" and \u2612 for no')
```

prints out: Check &#2611; for "yes" and &#2612; for no

## HTML

Any would do

```
<p> Spades: &spades;</p> <!-- HTML entity -->
<p> Spades: &#9824;</p>  <!-- Decimal -->
<p> Spades: &#x2600;<p>  <!-- Hexadecimal -->
```


