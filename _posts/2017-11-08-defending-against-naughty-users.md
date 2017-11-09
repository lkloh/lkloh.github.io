---
layout: post
title:  "Defending against naughty users"
date:   2017-11-08
---

I was trying to write an input field for a form that
can only take in integers within a certain range,
to submit to the backend.
The backend does its own validation,
but ideally the front-end does as much as possible to 
get the user to input acceptable values.

Here's all the things a casual user could to to screw things up in a simple 
text input field that is supposed to only accept numbers between 0-5:
* Scroll to a negative field
* Type in negative numbers
* Copy and paste negative numbers into the input box

The form below mostly defends against accidental mistakes.

```
<!DOCTYPE html>
<html>

<head>
<title> 
	Defense against naughty users
</title>
</head>

<body>
	<h1> Only integers between 0 - 5 are allowed </h1>

	<h2> You can enter anything you like! </h2>
	<input placeholder="Enter a number between 0 and 5">

	<h2> You can only scroll between 0 - 5, but can type negative numbers in </h2>
	<input type="number" placeholder="Enter a number between 0 and 5" , min=0, max=5>

	<h2> No typing negative numbers! </h2>
	<input type="number" placeholder="Enter a number between 0 and 5" , min=0, max=5, onkeypress="return event.charCode >= 48">

	<h2> No copying and pasting </h2>
	<input type="number" placeholder="Enter a number between 0 and 5" , min=0, max=5, onkeypress="return event.charCode >= 48", onpaste="return false;">


</body>

</html>
```

A user determined to screw things up could probably
submit a require to the form programmatically,
but I'm not going to defend against that in the front-end.









