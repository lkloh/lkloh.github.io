---
type: post
title: "Decoupling data structure from the template"
date: 2018-11-13
---

Given

```js
get data() {
  return {
    name: "Alice",
    schools_attended: {
      'A_elementary': 6,
      'B_middle': 2,
      'C_high': 4,
      'D_college': 4,
      'E_graduate': 2,
    };
  }
};
```

and 

```
// template
each num_years_attended, school_name in data.schools_attended
  .school= school_name
  .attendance= num_years_attended
```

it is better not have the template depend on knowing the shape of the data,
(especially several depths in)
and instead rewrite the above as


```js
get data() {
  return {
    name: "Alice",
    schools_attended: {
      'A_elementary': 6,
      'B_middle': 2,
      'C_high': 4,
      'D_college': 4,
      'E_graduate': 2,
    };
  }
};

get schools_attended() {
  return this.data.schools_attended;
}
```

and 

```
// template
each num_years_attended, school_name in schools_attended
  .school= school_name
  .attendance= num_years_attended
```

