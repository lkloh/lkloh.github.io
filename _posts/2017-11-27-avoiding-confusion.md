---
layout: post
title:  "Avoiding confusion"
date:   2017-11-27
---

I had a bit of backbone code for a form that looked like this:

```
 ---------------------
|                     |
|  first name: _____  |
|  last name:  _____  |
|  birthday:   _____  |
|                     |
|     ----------      |
|    | CONTINUE |     |
|     ----------      |
|                     |
 ---------------------
```

and I wanted to avoid repeating myself.
Not too much code here.
```
var view = Backbone.View.extend({

	template: htmlTemplate,

	events: {
		'blur .firstname, .lastname, .birthday': 'validateForm',
        'click .continue_button': 'validateForm',
    },

	initialize: function() {
		this.model = new myModel();
        this.model.on_change(this.render.bind(this));
	},

	render: function() {
		// render view
	},

	validateForm: function() {
		this.model.set('firstname', this.$el.find('.firstname').val());
		this.model.set('lastname', this.$el.find('.lastname').val());
		this.model.set('birthday', this.$el.find('.birthday').val());
		this.model.validateModel();
	},
});
```

Problem was that I was saving all the input values to the backbone model
when the user hit the `submit` button,
and that was really unnecessary, as they were already saved by the `blur` event.

## Right way

```
var view = Backbone.View.extend({

	template: htmlTemplate,

	events: {
		'blur .firstname' : 'handleFirstname',
		'blur .lastname' : 'handleLastname',
		'blur .birthday': 'handleBirthday',
        'click .continue_button': 'validateForm',
    },

	initialize: function() {
		this.model = new myModel();
        this.model.on_change(this.render.bind(this));
	},

	render: function() {
		// render view
	},

	handleFirstname: function() {
		this.model.set('firstname', this.$el.find('.firstname').val());
		this.validateForm();
	},

	handleLastname: function() {
		this.model.set('lastname', this.$el.find('.lastname').val());
		this.validateForm();
	},

	handleBirthday: function() {
		this.model.set('birthday', this.$el.find('.birthday').val());
		this.validateForm();
	},

	validateForm: function() {
		this.model.validateModel();
	},
});
```


