---
layout: post
title:  "JQuery: ev.stopPropagation()"
date:   2017-09-17
---

You're supposed to write
```js
$('button').click(ev => {
	ev.stopPropagation();
	doSomething();
});
```

instead of the more concise
```js
$('button').click(ev => {
	doSomething();
});
```

That's because if we have the html as 
```
<div id='outer'>
	<button ></button>
</div>
```

and the jQuery script as
```js
$('button').click(() => {
	alert('button');
});

$('div').click(() => {
	alert('div');
});
```

Then when the button is clicked, the click action is also bubbled up to its parent div,
so two alerts, "button" and "div" would be fired.

To avoid this problem, the jQuery script should be

```js
$('button').click(ev => {
	ev.stopPropagation();
	alert('button');
});

$('div').click(ev => {
	ev.stopPropagation();
	alert('div');
});
```

w3schools has the best illustration of this 
[here](https://www.w3schools.com/jquery/event_stoppropagation.asp).












