---
layout: post
title:  "Backbone model should represent current state of date"
date:   2017-11-15
---

When using Backbone,
update the model to reflect what the data should be.
Then bind the view to re-render whenever the model changes.

## No

Use javascript to update the view directly

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

	// use view to update model
	render: function() {
		var meaning = $('input').val();
		this.model.set('meaningOfLife', meaning);
	},

	// update view on change
	updateMeaningOfLife: function(e) {
		var prevMeaning = this.model.set('meaningOfLife');
		$('input').val(prevMeaning + 1);
	},
});

```

## Yes

Update the model first, and hook up the view to re-render when model is updated.

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