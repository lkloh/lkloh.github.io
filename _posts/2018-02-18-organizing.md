---
type: post
title: "Organizing Backbone"
date: 2018-02-18
---

Given a form like this:
```
 ---------------
|  -----------  |
| | Say Hello | |
|  -----------  |
|  -----------  |
| | Say No    | |
|  -----------  |
|  -----------  |
| | Say ?     | |
|  -----------  |
 ---------------
```

And a Backbone script like this, with the goal of printing "Hello' when clicking on the first and third buttons,
and "no" when clicking on the second button,
```js
var saySomething = Backbone.View.extend({
  template: myTemplate,
  
  events: {
    'click .firstButton': 'sayHello',
    'click .secondButton': 'sayNo',
  },

  className: 'containingDiv',

  initialize() {
    this.$el.find(`.thirdButton`).on('click', this.sayHello.bind(this));
  },

  sayNo: function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('No');
  },

  sayHello: function(e) {
    if (e.target.class.includes('firstButton') || e.originalEvent.detail.action === 'hello') {
      e.preventDefault();
      e.stopPropagation();
      console.log('Hello');
    }
  },
});
```
Would work, but because we should only get into "sayHello" function when we are absolutely sure 
of saying hello, we should rewrite this as:

```js
var saySomething = Backbone.View.extend({
  template: myTemplate,
  
  events: {
    'click .firstButton': 'sayHello',
    'click .secondButton': 'sayNo',
  },

  className: 'containingDiv',

  initialize() {
    this.$el.find('.thirdButton').on('change', function(e) {
      if (e.originalEvent.detail.action === 'hello') {
        this.sayHello(e);
      }
    }.bind(this));
  },

  sayNo: function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('No');
  },

  sayHello: function(e) {
    if (e.target.class.includes('firstButton') || e.target.action === 'hello') {
      e.preventDefault();
      e.stopPropagation();
      console.log('Hello');
    }
  },
});
```

