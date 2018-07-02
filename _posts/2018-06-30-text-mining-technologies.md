---
type: post
title: "Text mining technologies"
date: 2018-06-30
---

## Information extraction

Starting point to analyze unstructured text.

### Goal

Identify key phrases and relationships in text

### How its done

Look for predefined sequences in text (pattern matching).
to infer the relationships between identified people/places/time
to provide meaningful information.

Predict information missed by the extraction using discovered rules.



## Topic tracking

Alerts on certain keywords.

### How it works

* Keep user profiles
* Based on documents a user views, predict other documents of interest to the user

### Limitations

If you sent up a Google alert for "text mining",
you may get new stories on mining for diamonds,
and only a few on text mining.

Can be improved by monitoring click through rate.

### Keyword extraction

Keywords are useful to summarize news articles.
To do this, a candidate keyword list from categories of articles (politics/business/entertainment/etc)
are extracted, compared across domains,
then the keyword list is extracted.

### Lexical chaining

Group lexically related terms into lexical chains.
Useful in tracking articles related to a particular news event.



## Summarization

Used to figure out whether a long article is worth the time it takes to read it.

### Goals

Reduce length of a document but keep the main points and overall meaning.

### Challenges

Teaching software to analyze semantics.

### Sentence extraction

Extracts important sentences from a document.

Does so by statistically weighing the sentences.
For example, it extracts sentences following the phrase "in conclusion".

### Automatic summarization

1. Preprocessing: Original text --> structued text representation.
  * Reduce dimensionality by eliminating common words such as "the" and "a".
  * Case folding: covert all characters to upper/lower case
  * Stemming: Similar words (e.g. plurals) are considered similar - done using a vector model
2. Processing: Structured text representation --> summary structure
3. Generation: Summary structure --> final summary



## Categorization

Identify main themes of a document by placing it into a set of predefined topics "categories".

Document is treated as a "bag of words" and words from a particular category are counted.
Supervised learning algorithms are commonly used for categorization.


## Clustering

Used to group similar documents, but on the fly instead of into predefined categories.
A document can be grouped into multiple subtopics, so this does not lose entire
categories of information like Categorization does.

## Text clustering

1. Remove stop words such as "the" and "a".
2. Stemming: Group similar words such as "work", "worker", "worked", "works", "working".
3. Filtering: Use domain vocabulary to filter words and reduce dimensionality.


## Concept Linkage

Connect related documents by identifying commonly-shared concepts.
Uses for browsing information (not searching).
Useful in biomedical research to identify links between diseases and treatments
from a large body of previously done research.


## Information visualization

Put large textual sources together in a map with browsing and search capabilities.
Useful to narrow down many documents on different topics and explore the related ones.


## Question answering

Finding the best answer to a given question.


## Association rule mining

Discover relationships among a large set of variables in a data set.
Used in business decisions (e.g. which items customers often purchase together).
Study the relationships and implications among topics that characterise a corpus.































