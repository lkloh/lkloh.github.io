---
layout: post
title:  "Real Technical Interview Question: Detecting a toepliz matrix"
date:   2017-07-02 01:57:45 -0700
categories: technical interview, toeplitz matrix
---

Two separate interviewers tried to give me this question
at a very well known company in Mountain View.
I answered it the first time round, 
and told the second that I had already seen this question. 

{% highlight ruby %}
Find out whether a matrix is a Toeplitz Matrix.
{% endhighlight %}

A [Toeplitz matrix](https://en.wikipedia.org/wiki/Toeplitz_matrix) 
has the same integers on all of its diagonals.
It can be of any dimension, not necessarily square.
For example, 

{% highlight ruby %}
1, 8, 7, 5
2, 1, 8, 7
3, 2, 1, 8
{% endhighlight %}

is a Toeplitz matrix, but 

{% highlight ruby %}
1, 8, 7, 5
2, 1, 9, 7
3, 2, 1, 8
{% endhighlight %}

is not a Toeplitz matrix.

To solve this, note that given any two rows in the matrix,
displacing 


































