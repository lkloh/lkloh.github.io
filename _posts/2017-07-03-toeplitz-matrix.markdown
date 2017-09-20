---
layout: post
title:  "Detecting a toepliz matrix"
date:   2017-07-03 01:57:45 -0700
---

Two separate interviewers tried to give me this same question.
I answered it correctly at the phone screen, 
and told the interviewer at the onsite that I had already seen this question. 

```python
Find out whether a matrix is a Toeplitz Matrix.
```

A [Toeplitz matrix](https://en.wikipedia.org/wiki/Toeplitz_matrix) 
has the same integers on all of its diagonals.
It can be of any dimension, not necessarily square.
For example, 

```python
1, 8, 7, 5
2, 1, 8, 7
3, 2, 1, 8
```

is a Toeplitz matrix, but 

```python
1, 8, 7, 5
2, 1, 9, 7
3, 2, 1, 8
```

is not a Toeplitz matrix.

Let's gain an insight by looking at the example of a Toeplitz matrix above.
Notice that when displacing the rows, we get a pattern: 

```python
      1, 8, 7, 5
   2, 1, 8, 7
3, 2, 1, 8
```

It seems that for any row `i` and row `i+1` in a Toeplitz matrix with `n` rows and `m` columns
shifting row `i` by one position would result in
elements `0, 1, ..., m-2` of row `i` being the same
as elements `1, ..., m-1` of row `i+1`.

However, in the non-Toeplitz matrix, this is not the case.
```python
      1, 8, 7, 5
   2, 1, 9, 7
3, 2, 1, 8
```

Thus we want something like:
```python
def is_toeplitz_matrix(matrix):
  [nrows, ncols] = matrix.shape
  if nrows < 2 or ncols < 2:
    return True
  for row in range(nrows - 1):
    if not centers_align(matrix, row, row + 1, ncols):
      return False
    return True
```

where `centers_align` checks whether two adjacent rows could be rows of a Toeplitz matrix.

To check if two adjacent rows are rows of a Toeplitz matrix:
{% highlight ruby %}
def centers_align(matrix, row, next_row, ncols):
  return np.array_equal(matrix[row, 0:(ncols - 1)], matrix[next_row, 1:ncols])
{% endhighlight %}

Putting them together, we get the solution.
We have to examine almost all the numbers in each row, so this is an `O(nm)` solution in time.
Depending on implementation, the space could be constant if you
passed the rows of the matrix to `centers_align` by reference. 

See the full solution in python with test cases [here](https://github.com/lkloh/technical-interview-questions/blob/master/detecting_toepitz_matrix.py). 

That's only a few lines of code.
I was asked to describe how to scale the solution,
assuming a very large matrix. 

I said that we could break up the matrix into several contiguous blocks,
then check each block on a different machine.
If any of the blocks was not a Toeplitz, then the matrix is not a Toeplitz matrix.
If each block was also a Toeplitz matrix,
then we could check if putting them together would make a toeplitz matrix. 
then merge them together.
Assuming we broke the matrix into `b` blocks,
that is `n / b` matrices to check on each machine,
so `O(nm / b)` time to check the blocks separately.
To merge them, we have to merge `n / b` blocks,
so its `O(nm / b)` time to merge.
So you could check this in `O(nm / b)` time
and get time savings depending on what `b` is. 

