---
type: post
title: "What happens if you provide two unnamed slots (in your shadow dom)?"
date: 2019-01-17
---

Inspired by [this post](https://github.com/praveenpuglia/shadow-dom-in-depth) on shadow dom.

Slots are a way to invite light DOM into your [shadow DOM](https://developers.google.com/web/fundamentals/web-components/shadowdom).

```
<!-- shadow dom -->
<custom>
  #shadow-root
    <slot name="come-into-the-shadows"></slot>
</custom>
```

and

```
<!-- light dom --->
<custom>
  <h1 slot="come-into-the-shadows"> The Light </h1>
</custom>
```

results in this flattened tree: 
```
<custom>
  #shadow-root
    <h1 slot="come-into-the-shadows"> The Light </h1>
</custom>
```

If you have duplicate slots, they get ignored,
as the elements from the light-dom go to the first slot they match.

So writing 
```
<!-- shadow dom -->
<custom>
  #shadow-root
    <slot name="come-into-the-shadows"></slot>
    <slot name="come-into-the-shadows"></slot>
</custom>
```

with 
```
<!-- light dom --->
<custom>
  <h1 slot="come-into-the-shadows"> The Light </h1>
</custom>
```

will again result in the flattened tree
```
<custom>
  #shadow-root
    <h1 slot="come-into-the-shadows"> The Light </h1>
</custom>
```
