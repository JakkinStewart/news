#! /usr/bin/env python3
# Written by Joshua Jordi

import os
#var = 1
#while var == 1:
def main():
    # Runs news module
    news('news/cnn.txt')
    # Opens outFile for writing
    outFile = open("news/news.txt", "w")
    
def news(news):
    # Runs news.sh
    os.system("/usr/bin/sh /home/$USER/newsTest/news.sh")
    # Opens whichever news text file exists. In this case, its cnn.txt
    infile = open(news, "r")

    # Creates empty sets, lists, and dictionarys for later use.
    s = []
    predict = set()
    diction = {}

    # Creates list of each line. Makes browsing the news easier.
    for word in infile:
        word = word.rstrip()
        word = word.split()
        s += word
        print(word)
#    for word in s:
#        predict.add(word)
#    
#    average = 0
#    for word in predict:
#        diction[word] = s.count(word)
#
#    maximum = 0 
#    for word in diction:
#        if diction[word] > maximum:
#            maximum = diction[word]
##    print(list(diction.keys())[list(diction.values()).index(maximum)])
#    return diction


##    print(maximum)
#
##    print(diction.keys())
##    for key in sorted(diction.keys()):
##        print(key, diction[key])#, sorted(diction.keys()))
##    print(diction)
##        count += 1
##        average += s.count(word)
main()
