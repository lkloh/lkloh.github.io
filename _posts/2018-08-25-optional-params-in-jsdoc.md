---
type: post
title: "Optional params in JSDoc"
date: 2018-08-25
---

In order to specify the default value for an optional attribute in JSDoc,
you could write `[property_name=default_property_value]`.

Like this, for example:

```js
/**
 * Updates state
 * @params {Object} config - dictionary of attributes to update
 * @params {number} id - unique identifier for the session
 * @params {boolean} [is_dropdown=true] - true if dropdown list, false otherwise
 * @params {boolean} [filterable=false] - true if you can filter results in the search box, false otherwise
 */
function update_state(config) {
  this.helper.update_state(config);
}
```

