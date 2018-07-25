---
type: post
title: "Injecting HTML verbatim into pug (template) files"
date: 2018-07-22
---

To inject HTML into a pug (template) file:

## Wrong way

```
html
  head Hello World!
  body
    - var inject_text = `<span class="inject_me">Inject me please!</span>`
    div.inject_here
      div= inject_text
    div End of body
```

This will give you a rendered page looking like this:
```
Hello World!
<span class="inject_me">Inject me please!</span>
End of body
```
which is probably no what you want.

Instead do


## Right way

```
html
  head Hello World!
  body
    - var inject_text = `<span class="inject_me">Inject me please!</span>`
    div.inject_here
      div= !{inject_text}
    div End of body
```

This will give you a rendered page looking like this:
```
Hello World!
Inject me please!
End of body
```

As desired.

In general you shouldn't be injecting HTML from variables into a template file,
or generating HTML in javascript and then sticking it into a template file,
as that is _not_ where one might expect HTML to be placed.




