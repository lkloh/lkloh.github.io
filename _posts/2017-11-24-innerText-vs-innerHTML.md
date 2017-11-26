---
layout: post
title:  "innerText vs innerHTML"
date:   2017-11-24
---

Given this bit of html,
```
<div id='myDiv'>
Hello World!
</div>
```
The webpage looks like this:
```
Hello World!
```

## innerHTML

```js
$('#myDiv').html('<a href="https://www.ted.com/talks">TED Talks</a>');
```

Transforms it to a webpage that looks like this
```
TED Talks
---------
```
and the works "Ted Talks" is a hyperlink to the TED Talks website,
as you probably wanted.

## innerText

```js
$('#myDiv').text('<a href="https://www.ted.com/talks">TED Talks</a>');
```

Transforms it to a webpage that looks like this
```
<a href="https://www.ted.com/talks">TED Talks</a>
```

See the demo [here](https://github.com/lkloh/javascriptPlayground/blob/master/htmlFun/test.html).




