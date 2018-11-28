---
type: post
title: "Controlling from the parent or child"
date: 2018-11-22
---

What's a better way to decide whether to show a component?

This might work
```
// jade file
.parent
  .student #{name}
  .records(class={isHidden: isActive})
    .address ${address}
    .gpa ${gpa}
    ul.enrolled_classes
      for class in classes
        li.class 
          .name #{class.name}
          .professor ${class.instructor}
```
with a style file that does
```
// styl file
.isHidden
  display none
```

but really one should be doing

```
// jade file
.parent
  .student #{name}
  if isActive
    .records
      .address ${address}
      .gpa ${gpa}
      ul.enrolled_classes
        for class in classes
          li.class 
            .name #{class.name}
            .professor ${class.instructor}
```

so you only render the elements in `records` if absolutely necessary.
This saves on load time, and potentially also any missing data errors
if you try to pull some data that doesn't exist.


