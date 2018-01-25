---
type: post
title: "Do cheap annotations work for natural language processing"
date: 2018-01-22
---

Summarized from
```
Snow, Rion, et al. "Cheap and fast---but is it good?: evaluating non-expert annotations for natural language tasks." Proceedings of the conference on empirical methods in natural language processing. Association for Computational Linguistics, 2008.
```

## Why they investigated

* Natural language processing needs human linguistic annotations on datasets for research development
* Using experts to do the annotations is costly
* Using non-expects over the Web to do annotations is cheap
* This paper wants to investigate whether using non-experts
  will be as effective as using experts - it did

## Tasks chosen for measurements

* Affective text recognition: 
  Given a list of headlines, rate from 0-100 for the emotions
  anger, disgust, fear, joy, sadness, surprise,
  and rate from -100 - 100 the positive or negative emotional content of the headline.
  ~4 non-expert annotations to achive the same quality as 1 expert annotation.

* Word similarity:
  Numeric judgements of word similary on a scale of 1-10,
  aggregating the work of 10 non-experts gives the same accuracy of 1 expert.
  
* Recognizing textual entailment:
  Inferring statements form another.
  Example, which of "Crude oil prices slump" or "The government decided
  to raise oil prices last week" implies "Oil prices drop"?
  Averaging performance of 10 non-experts gives the same accuracy of 1 expert.

* Event temporal ordering:
  "The airplane blew up, then we saw two fireballs coming down from the sky".
  Decided whether "the airplane blew up" or "two fireballs" coming down from
  the sky came before or after each other.
  Averaging performance of 10 non-experts gives the same accuracy of 1 expert.
  They did have to simplify this task a bit for non-expert aggregation to 
  reach an acceptable correlation with the experts' judgement.

* Word sense disambiguation:
  "John Doe was appointed president and chief operating officer" - 
  was John Doe appointed as
  (1) Leader of a corporation, such as Google, Inc
  (2) Head of a country
  (3) Header of the United States, the world's only superpower?
  Performing simple majority voting over the non-expert annotations
  yielded a high accuracy rate, almost 100% in agreement with the expert
  annotations.


  

Chosen as the authors thought they were learnable for non-experts,
and had gold-standards from experts to compare against.

About USD $25 was spend on paying non-experts to label for the purpose of the research.




