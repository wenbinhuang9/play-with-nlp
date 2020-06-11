#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:23:34 2020

@author: ben
"""

import  nltk


# A is a B, A can be a person or a regular noun
sample = "He is the president of United States. Before this, he was a successful business man"

grammar = "chunk: {<PRP><VB.?>+<DT>?<JJ.?>*<NN.*>}"

sents = nltk.sent_tokenize(sample)

print(sents)
for i in sents:
    pos = nltk.pos_tag(nltk.word_tokenize(i))
    parser = nltk.RegexpParser(grammar)
    chunks = parser.parse(pos)
    #chunks.draw()


text='''Donald John Trump (born June 14, 1946) is the 45th and
current President of the United States. Before entering politics,
he was a businessman and television personality.'''

grammar = 'chunk: {<PRP><VB.?><DT>?<NN.*>+}'

pos = nltk.pos_tag(nltk.sent_tokenize(text))

parser = nltk.RegexpParser(grammar)

chunked = parser.parse(pos)

## todo it seems here has a bug
for i in chunked.subtrees():
    print(i)

text='''Bush was born on July 6, 1946, in New Haven,
Connecticut. After graduating from Yale University in 1968
and Harvard Business School in 1975, he worked in the oil industry.
Bush married Laura Welch in 1977 and unsuccessfully ran for the U.S.
House of Representatives shortly thereafter.
He later co-owned the Texas Rangers baseball team before defeating Ann
Richards in the 1994 Texas gubernatorial election.
Bush was elected President of the United States in 2000
when he defeated Democratic incumbent Vice President Al Gore
after a close and controversial win that involved a stopped recount
in Florida. He became the fourth person to be elected president
while receiving fewer popular votes than his opponent.[3]
Bush is a member of a prominent political family and is the
eldest son of Barbara and George H. W. Bush, the 41st President
of the United States. He is only the second president to assume
the nation's highest office after his father, following the
footsteps of John Adams and his son, John Quincy Adams.[4]
His brother, Jeb Bush, a former Governor of Florida, was a
candidate for the Republican presidential nomination in the
2016 presidential election. His paternal grandfather,
Prescott Bush, was a United States Senator from Connecticut.'''

Organization = []
person = []
GPE = []

pos = nltk.pos_tag(nltk.sent_tokenize(text))
ne_chunk = nltk.ne_chunk(pos)

print(ne_chunk)

