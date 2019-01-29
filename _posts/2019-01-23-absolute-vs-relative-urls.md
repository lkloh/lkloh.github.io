---
type: post
title: "Absolute vs Relative URLs"
date: 2019-01-23
---

Summarized from [here](https://html.com/anchors-links/#Specify_a_Hyperlink_Target_href).

## Absolute URL

From the `http://example.com/items/my-item/` page:
```
<a href="http://example.com/items/my-item">Absolute</a> link.
```

## Relative URL

Useful in the development process as the staging server's
domain name is usually different from the production domain name,
so developers can test more easily on both.
Also useful in case the site's domain name ever changing when a rebranding happens.

From the `http://example.com/items/your-item/` page,
to point to the URL: `http://example.com/items/my-item/`:

```
<a href="/items/my-item">Relative</a> link.
```
causes the browser to look at the lowest level of the file directory
for the file `items`, then `my-item` inside.

while
```
<a href="../my-item">Relative</a> link.
```
looks in the parent folder of the `your-item` directory
for the `my-item` directory.
