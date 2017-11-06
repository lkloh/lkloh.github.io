---
layout: post
title:  "Data Structures Used in Web Apps"
date:   2017-11-05
---

Interviewing.io recently raised a [3 million dollar seed round](https://techcrunch.com/2017/09/27/interviewing-io-hopes-to-close-the-engineer-diversity-gap-with-anonymous-interviews/).
Meaning they now have money to pay for more interviewers,
so that probably explains why their availability for scheduling
interview practices is getting better.
It used to take 3 weeks to schedule anything, now it takes about 2 weeks.


At least I can get off Pramp now,
it was great but I've done all their questions available by now.
Today though, an interviewer on Interviewing.io 
gave me the exact same question I had seen on Pramp in the past. 
Still didn't get it perfect though,
knowing the strategy isn't enough to figure out how to get all the edge cases right.


```
String: 'abbbcca'
Alphabet: ['a', 'b', 'c']
Output: 'bcca'

String: 'aaaaabbbbbbcccccabcaaaaabbbbbbcccc'
Alphabet: ['a', 'b', 'c']
Output: 'abc'

String: 'abbbbbcccccffff'
Alphabet: ['a', 'b', 'c', 'f']
Output: ''
```

## O(len(string)^2) time solution, using lots of space

Pseudocode
```
for strlen = len(alphabet)...len(string)
	for substr of in string, where len(substr) == strlen
		if substr contains all chars in alphabet
			return substr
return ''
```

## O(len(string) + len(alphabet)) solution, using O(len(alphabet)) space

I only came up with this because someone explained it to me
the first time I saw it on Pramp.
I'm not sure how anyone can come up with it without hints in 15 min
if they haven't seen something similar in the past.

It took me at least 2 hours to figure a correctly coded
solution by myself after the interview.

```
def contains_all_alphabets(char_counts):
	for ch in char_counts:
		if char_counts[ch] == 0:
			return False
	return True

def get_shortest_substr(s, alphabet):
	char_counts = {}
	for ch in alphabet:
		char_counts[ch] = 0

	start = 0
	end = 0
	min_start = 0
	min_end = 0
	min_str_len = len(s) + 1
	while start <= end and end < len(s):
		end_ch = s[end]
		char_counts[end_ch] += 1
		if contains_all_alphabets(char_counts):
			# try to do better by incrementing start index
			if end - start + 1 < min_str_len:
				min_str_len = end - start + 1
				min_start = start
				min_end = end

			start_ch = s[start]
			if char_counts[start_ch] >= 2:
				char_counts[start_ch] -= 1
				start += 1
			else:
				end += 1
		else:
			end += 1

	return s[min_start:min_end+1] if min_str_len <= len(s) else ''

print get_shortest_substr('abbbcca', set(['a','b','c']))
print get_shortest_substr('abc', set(['a','b','c']))
print get_shortest_substr('bc', set(['a','b','c']))
```



















