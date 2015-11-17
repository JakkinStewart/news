#! /usr/bin/env python3
# Written by Joshua Jordi

import os
#var = 1
#while var == 1:

def news(news):
    os.system("/usr/bin/sh /home/$USER/newsTest/news.sh")
    infile = open(news, "r")

    s = []
    predict = set()
    diction = {}

    count = 0
    for word in infile:
        word = word.rstrip()
        word = word.split()
        s += word
    #    print(word)
    for word in s:
        predict.add(word)
    
    count = 0
    average = 0
    for word in predict:
        diction[word] = s.count(word)

    maximum = 0 
    for word in diction:
        if diction[word] > maximum:
            maximum = diction[word]
#    print(list(diction.keys())[list(diction.values()).index(maximum)])
    return diction
#    print(maximum)

#    print(diction.keys())
#    for key in sorted(diction.keys()):
#        print(key, diction[key])#, sorted(diction.keys()))
#    print(diction)
#        count += 1
#        average += s.count(word)
