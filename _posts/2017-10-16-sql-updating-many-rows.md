---
layout: post
title:  "Updating multiple rows on multiple conditions in SQL"
date:   2017-10-16
---

If you want to update multiple rows in SQL, 
the way to do it depends on the type of SQL you are using.

Given this schema:
```
CREATE TABLE employees 
(
	firstname text PRIMARY KEY,
	lastname text,
	salary int,
	bonus int
)
```

and employees paid this much:
```
('John', 'Doe', 100, 15)
('Jane', 'Roe', 110, 5)
('Alice', 'Anderson', 80, 20)
('Bob', 'Brown', 70, 30)
```

To give some of them a pay raise:

## MySQL:

```
INSERT INTO employees (firstname, salary, bonus)
VALUES
	('John', 120, 20)
	('Alice', 100, 15)
	('Bob', 85, 40)
ON DUPLICATE KEY UPDATE
 	cod_user=VALUES(cod_user), date=VALUES(date)
```

## SQlite:

```
REPLACE INTO employees (firstname, lastname, salary, bonus)
VALUES 
	('John', 'Doe', 120, 20)
	('Alice', 'Anderson', 100, 15)
	('Bob', 85, 40)
```


See a working example [here](https://github.com/lkloh/sql-playground).






