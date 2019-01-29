---
type: post
title: "Hyperlinks"
date: 2019-01-22
---

Summarized from [here](https://html.com/anchors-links/#Specify_a_Hyperlink_Target_href).

## Anchor element

The `a` tag
```
This is an <a>anchor tag</a> linking to nothing
```

## The "href" anchor attribute

Short for `hypertext reference`.
Use to specify where the anchor element links to.

### "href" can link to a webpage

```
This links to <a href="https://www.google.com/">Google</a>.
```

### "href" can link to any element on a webpage with an id
```
<div id="block">
  Hello world!
</div>

<span>I can link to the <a href="#block">block</a>.</span>
```

### "href" can run a script
```
<a href="javascript:alert('Hello World!')"></a>
```

### "href" can link to a non HTTP resource
```
Get <a href="mailto:lkloh2410@gmail.com">in touch</a> with me!
```

## The "target" attribute

```
Go to <a href="https://www.google.com/" target="_blank">Google</a>
in a new browser tab.
```

## The "download" attribute

```
A link can be used to tell the browser to 
<a href="http://example.com/file.txt" download="my_file_name">download</a> a file.
```

When the download is done, the file downloaded is called `my_file_name.txt`.







