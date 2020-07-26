#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:29:19 2020

@author: ben
"""


import nltk
from nltk.corpus import names
import re
import random 



maleList=[name for name in names.words('male.txt')] # build the training/testing set in a format (input, class)
femaleList=[name for name in names.words('female.txt')]


bothList = [ name for name in maleList if name in femaleList]

print(bothList)

print(len(maleList), len(femaleList), len(bothList))

maleOnlyList = [name for name in maleList if name not in bothList]
femaleOnlyList = [name for name in femaleList if name not in bothList ]

print(len(maleOnlyList), len(femaleOnlyList))

maleOnlyTupleList = [(name, "male") for name in maleOnlyList]
femaleOnlyTupleList = [(name, "female") for name in femaleOnlyList]
bothTupleList = [(name, "both") for name in bothList]



        
def feature(name):    
    d = {}
 
    d["first_letter"] = name[0]
    d["last_letter"] = name[-1]

    for i, j in zip(name[:-1], name[1:]):
        if i == j :
            d["consecutive"] = True  
            break
        else:
            d["consecutive"] = False 
    
    return d


dataList = maleOnlyTupleList + femaleOnlyTupleList + bothTupleList


random.shuffle(dataList )

print(len(dataList ))
featureList = [(feature(name), label) for name, label in dataList ]

trainLen = int(len(dataList) * 0.9)


train = featureList[:trainLen]

test = featureList[trainLen:]


classifier = nltk.NaiveBayesClassifier.train(train)

# classify some names
# the classify function takes features as argument
result = nltk.classify.accuracy(classifier, test)

print(result)




