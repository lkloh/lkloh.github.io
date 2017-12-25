---
layout: post
title:  "Why ES6 and Backbone don't mix"
date:   2017-12-21
---

ES6 is the latest version of JavaScript, with lots of new features that help shorten the amount of boilerplate needed to do anything. So why shouldn't we [upgrade](https://benmccormick.org/2015/04/07/es6-classes-and-backbone-js/) legacy Backbone code written in ES5 to ES6?

For example, from this ES5 code
```js
// taken from the Backbone website
var DocumentRow = Backbone.View.extend({

  tagName: "li",

  className: "document-row",

  events: {
    "click .icon":          "open",
    "click .button.edit":   "openEditDialog",
    "click .button.delete": "destroy"
  },

  initialize: function() {
    this.listenTo(this.model, "change", this.render);
  },

  render: function() {
    //...
  }

});
```

to ES6

```js
// taken from the Backbone website
class DocumentRow extends Backbone.View {

  tagName: "li", // property added to class, not an instance of the class

  className: "document-row", // property added to class, not an instance of the class

  events: {
    "click .icon":          "open",
    "click .button.edit":   "openEditDialog",
    "click .button.delete": "destroy"
  },

  initialize: function() {
    this.listenTo(this.model, "change", this.render);
  },

  render: function() {
    //...
  }
};

var dr = new DocumentRow();
```

Reason is that at ES6 classes only allow adding properties to functions, not the class instance.

Otherwise if properties could be added to the class, 
they would be share by all instance of the class.
If the property added is a mutable state like an array,
that would cause real problems.

There are workarounds, but all even uglier than just writing `Backbone.View.extend({ })`
instead of `<classname> extends Backbone.View`.


