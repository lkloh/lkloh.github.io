---
type: post
title: "Shadow Boundaries"
date: 2018-02-16
---

Given


	<!DOCTYPE html>
	<html>
	<head>
	<script>
	window.onload = function() {
	  var root = document.getElementById('welcome_msg').createShadowRoot();
	  root.textContent = 'Hi Shadow';
	};
	</script>
	</head>

	<body>
	<div id='welcome_msg'>Welcome to my world</div>
	</body>
	</html>






