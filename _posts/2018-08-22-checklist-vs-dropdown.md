---
type: post
title: "Checklist vs Dropdown"
date: 2018-08-22
---

I was writing some code to process items selected in dropdown,
which can have at most one item to process.

```js
function process() {
  const selected_val = this.dropdown.get_selected();
  let selelected_item = {};
  this.all_items.forEach(item => {
    if (item.val === selected_val) {
      selected_item = {...item, {has_wings: false, is_animal: true});
    }
  });
  return selected_item;
}
```

but in hindsight, since only one item could be selected, it would be more instructive to use
`find` instead of `forEach` to clarify that only one item would ever be returned;
```js
function process() {
  const selected_val = this.dropdown.get_selected();
  const selected_item = this.all_items.find(item => {
    if (item.val === selected_val) {
      return item;
    }
  });
  if (selected_item) {
    return {...selected_item, {has_wings: false, is_animal: true}};
  }
}
```


