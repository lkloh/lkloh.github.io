---
layout: post
title:  "Data Structures Used in Web Apps"
date:   2017-11-04
---

Today I had a session with Interviewing.io.
Here's what we talked about.

## Describe what happens when you click a button on a webpage

Too generic, hard to know what happens unless you know the use case.

There's a client, your browser, and a server serving up the webpage.
Since we're in Web 2.0, your browser probably has all the javascript
for generating the next webpage to be rendered on demand already,
so the server never event gets a new request.
What the browser does is to see if the new page has been cached,
and serve that up.
Otherwise generated the new page and load it.

Here's what I didn't say, but should have. Thanks 
[Stack Overflow](https://stackoverflow.com/questions/2092527/what-happens-when-you-type-in-a-url-in-browser).
If this is an old-fashioned Web 1.0 page,
or a form to be submitted:
Browser asks OS for client IP address.
OS looks for the IP address using DNS lookip and returns the IP address to browser.
Browser opens TCP connection to server.
Browser sends HTTP request through TCP connection with info in the form.
Browser gets HTTP response (with the new page to be loaded after form is submitted)
and checks for success/failure, then closes connection.
Cache response, decode it and render the new webpage.

## Data Structures to learn in college CS class/ for technical interviews

* Array
* Dictionary
* (Hash) Set
* Linked List
* Tree
* Binary Search Tree
* Self-Balancing Tree
* Heap

## Data Structures actually used in full-stack development

90% of the time
* Array 

10% of the time
* Dictionary
* Tree

## Reason for how few are used in practice when doing development
* They are all abstracted away by implementations written
	by people with more (decades more) experience


## Here's a coding question about trees

```
Find all unique trees with n nodes.
```


Obviously a recursive solution would be required.


Here are the unique trees you want:
'''
     o
    / 
find_unique_tree(n-1)

     o
      \
  find_unique_tree(n-1)

      o
     / \
    o  find_unique_tree(n-2)

                       o
                      / \
 find_unique_tree(n-2)   o

'''


And here's the code,
which uses a hash set to store the trees,
`*` to represent nodes in the tree,
and also records the structure of the tree.

'''
def find_unique_tree(n):
	if n == 0:
		return []
	elif n == 1:
		return ['*']
	else:
		all_unique_trees = set
		tree_minus_one_set = find_unique_tree(n-1)
		for subtree in tree_minus_one_set:
			all_unique_trees += ['L(' + subtree + ')*']
			all_unique_trees += ['*L(' + subtree + ')']
		tree_minus_two_set = find_unique_tree(n-2)
		for subtree in tree_minus_two_set:
			all_unique_trees += ['**L(' + subtree + ')']
			all_unique_trees += ['L(' + subtree + ')**']
		return all_unique_trees

print find_unique_tree(0) # []
print find_unique_tree(1) # ['*'']
print find_unique_tree(2) # ['L(*)*', '*L(*)']
print find_unique_tree(3) # ['L(L(*)*)*', '*L(L(*)*)', 'L(*L(*))*', '*L(*L(*))', '**L(*)', 'L(*)**']
print find_unique_tree(4) # ['L(L(L(*)*)*)*', '*L(L(L(*)*)*)', 'L(*L(L(*)*))*', '*L(*L(L(*)*))', 'L(L(*L(*))*)*', '*L(L(*L(*))*)', 'L(*L(*L(*)))*', '*L(*L(*L(*)))', 'L(**L(*))*', '*L(**L(*))', 'L(L(*)**)*', '*L(L(*)**)', '**L(L(*)*)', 'L(L(*)*)**', '**L(*L(*))', 'L(*L(*))**']
'''



Could probably use some dynamic programming to avoid computing everything again,
but I only had 30 minute to think of everything.
The hardest part was thinking of a good representation of the tree 
using an immutable string,
so that I wasn't repeating everything I already found.



