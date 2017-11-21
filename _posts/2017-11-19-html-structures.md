---
layout: post
title:  "HTML structures"
date:   2017-11-19
---

I was writing a pug file that looked somewhat like this:
Shows info for college and student loan debt only for users that actually went to college.

```
- var attendedCollege
.content_styles 
  .row
    .input.name
    .input.birthday // Hi!
  if attendedCollege
    .row
      .input.college
      .input.graduation_year
      .input.gpa
if attendedCollege // Repeated if stmt!
  .divider
  .content_styles
    .row
      .input.student_debt_amount
      .input.montly_loan_amount
    .row
      .input.apply_for_loan_forgiveness
```

Because I wanted to consolidate things, I changed it to

```
- var attendedCollege
.content_styles
  .user_name
    .row
      .input.name
      .input.birthday
  if attendedCollege // Only once!
    .row.college_row
      .input.college
      .input.graduation_year
      .input.gpa
    .divider
    .content_styles
      .row
        .input.student_debt_amount
        .input.montly_loan_amount
      .row
        .input.apply_for_loan_forgiveness
```
Problem was that it messed up the CSS styles in `.content_styles`, so I did this:

```
- var attendedCollege
.content_styles
  .user_name
    .row
      .input.name
      .input.birthday
  if attendedCollege // Only once!
    .content_styles.row.college_row
      .input.college
      .input.graduation_year
      .input.gpa
    .divider
    .content_styles
      .row
        .input.student_debt_amount
        .input.montly_loan_amount
      .row
        .input.apply_for_loan_forgiveness
```

But that compromised the CSS structure. I ended up switching it back to 

```
- var attendedCollege
.content_styles
  .row
    .input.name
    .input.birthday
  if attendedCollege // Hi!
    .row
      .input.college
      .input.graduation_year
      .input.gpa
if attendedCollege // Repeated if stmt!
  .divider
  .content_styles
    .row
      .input.student_debt_amount
      .input.montly_loan_amount
    .row
      .input.apply_for_loan_forgiveness
```

Because you should not let the conditionals compromise the HTML structure, even for clarity.

Oh, and don't do this:
```
.content_styles
  .row
    .input.name
    .input.birthday
  - var attendedCollege // Beware of indentation
  if attendedCollege 
    .row
      .input.college
      .input.graduation_year
      .input.gpa
if attendedCollege // It's used in the outer indentation!
  .divider
  .content_styles
    .row
      .input.student_debt_amount
      .input.montly_loan_amount
    .row
      .input.apply_for_loan_forgiveness
```




