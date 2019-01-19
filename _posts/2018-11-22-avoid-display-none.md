---
type: post
title: "Avoid using display:none to hide your element"
date: 2018-11-22
---

Not rendering it at all is usually a better idea,
as it saves on load time and computation errors due to 
potentially missing or null data.

## Using display:none

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

## Not rendering it

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

Less elements to load (only loads a student records if the student is actively studying), and also you get to avoid dealing with errors due to missing data for an inactive student.


