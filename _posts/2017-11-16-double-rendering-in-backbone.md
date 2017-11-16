---
layout: post
title:  "Multiple rendering in Backbone"
date:   2017-11-16
---

Be careful about how often a view in Backbone gets rendered,
if you update the view every time the model gets altered!
That could lead to many re-renderings and slow down the application
if you're not careful!

Given the model below, with an input that can be altered by clicking a button"

```
// html template
<input type="number" default=0></input>
```

This backbone code forces the entire view to re-render everytime someone
updates the number in the input.
Could slow things down by a lot. 


```js
var myModel = Backbone.Model.extend({
	initialize: function() {
		this.set('meaningOfLife', 0);
	},
});

var view = Backbone.View.extend({

	template: htmlTemplate,

	events: {
        'click button': 'updateMeaningOfLife',
    },


	initialize: function() {
		this.model = new myModel();
        this.model.on_change(this.render.bind(this));
	},

	// re-render view if model is changed
	render: function() {
		var realMeaningOfLife = 42;
		$('input').val(meaningOfLife);
	},

	// update model on change
	updateMeaningOfLife: function(e) {
		var prevMeaning = this.model.set('meaningOfLife');
		this.model.get('meaningOfLife', prevMeaning + 1);
	},
});
```


