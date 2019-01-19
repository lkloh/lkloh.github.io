---
type: post
title: "Getting the name of an element"
date: 2019-01-19
---

I was trying to get hold of all the custom elements `student-record` in JavaScript.
```
<!-- .jade -->
#display
  student-record(attrs={id="561", name="Alice", gpa="3.42"})
  student-record(attrs={id="147", name="Bob", gpa="3.51"})
  student-record(attrs={id="298", name="Carol", gpa="2.67"})
```
by doing
```js
<!-- .js -->
const studentRecords = this.getElementById(`display`)
  .children.filter(el => el.tagName.toLowerCase() === `student-record`);
```

The unfortunate thing was that by filtering by
```
el.tagName.toLowerCase() === `student-record`
```

encouraged the use of bad syntax by template authors.
They could potentially write

```
<!-- .jade -->
#display
  STUDENT-RECORD(attrs={id="561", name="Alice", gpa="3.42"})
  STUDENT-RECORD(attrs={id="147", name="Bob", gpa="3.51"})
  STUDENT-RECORD(attrs={id="298", name="Carol", gpa="2.67"})
```

and still the .js script would filter by the correct nodes
for student records.

That was when I did some digging and found out that `tagName`
was always [capitalized in HTML](https://stackoverflow.com/questions/27223756/is-element-tagname-always-uppercase).

I wondered if there were other ways to get the name of a node,
and found that there are three ways.

## TagName

Always capitalizes the name of the node for HTML elements.
So it wouldn't have worked.

## NodeName

`nodeNames` of HTML elements are
[always capitalized](https://johnresig.com/blog/nodename-case-sensitivity/),
even when written in lowercase.

`nodeNames` of XML elements are always presented in the
original case, but that didn't help me as I was working with HTML.

## LocalName

`localName` did in fact return the HTML element's name in
the original case, but it was [deprecated](https://developer.mozilla.org/en-US/docs/Web/API/Node/localName) so it didn't help me either

# Conclusion

I ended up just deciding to rely on the linter to stop
template authors from writing something awful like:

```
<!-- .jade -->
#display
  student-RECORD(attrs={id="561", name="Alice", gpa="3.42"})
  StUdEnT-ReCorD(attrs={id="147", name="Bob", gpa="3.51"})
  STUDENT-record(attrs={id="298", name="Carol", gpa="2.67"})
```
