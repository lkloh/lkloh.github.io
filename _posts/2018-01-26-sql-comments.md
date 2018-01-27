---
type: post
title: "SQL comments"
date: 2018-01-26
---

SQL allows comments. That means that if you want to write an SQL statement that is very complex, you should add them in.
Their comments look like this:


```
SELECT
  student.id AS id
  student.first_name AS first_name
  student.last_name AS last_name
  car.model AS car_model
  /* Age of car needed to decide on insurance costs */
  car.year AS car_age
FROM
  student
  INNER JOIN car 
  ON student.id = car.owner_id
WHERE
  car_age >= 2016
```

