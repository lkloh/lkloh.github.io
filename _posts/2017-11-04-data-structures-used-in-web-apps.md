---
layout: post
title:  "Data Structures Used in Web Apps"
date:   2017-11-04
---

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


## Here's a question about trees

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
		all_unique_trees = []
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
but I only had 30 minute to think of everything on Interviewing.io.
The hardest part was thinking of a good representation of the tree 
using an immutable string,
so that I wasn't repeating everything I already found.



