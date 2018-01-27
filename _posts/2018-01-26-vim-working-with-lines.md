---
type: post
title: "Working with multiple lines in Vim"
date: 2018-01-26
---

To manipulate lines 66 - 70 in a file, in ESC mode do:

## Commenting and Uncommenting

From [here](https://unix.stackexchange.com/questions/120615/how-to-comment-multiple-lines-at-once):

```
:66,70s/^/#
```

And to uncomment:

```
:66,70s/^#/

## Deleting

```
:66,70d
```

## Copying

```
:66,70y
```

place the cursur where you want to paste and hit `p`.

