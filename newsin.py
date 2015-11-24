#! /usr/bin/env python
# Written by Joshua Jordi

import os
def main():
#    news = input("Enter the text file location: ")
#    keywords = input("Enter the keyword file location: ")
    news = 'news/cnn.txt'
#    cnn = 'news/cnn.txt'
    
    keywords = open('keywords.txt', 'r')
    keyword = keywords.read()
    keyword = keyword.strip()
    keyword = keyword.split('\n')

#    print(theNews(newsList(news), keyword))
    categories(keyword)

def newsList(newsIn):
    # Runs news.sh
    os.system("/usr/bin/sh /home/$USER/newsTest/news.sh")
    # Opens whichever news text file exists. In this case, its cnn.txt
    infile = open(newsIn, "r")

    # Creates an empty list for later use.
    s = []

    # Creates list of each line. Makes browsing the news easier.
    for word in infile:
        word = word.rstrip()
        word = word.split()
        s.append(word)
    return s

def newsSet(newsIn):
    # Creates a set of each word.
    s = newsList(newsIn)
    predict = set()    
    for sentences in s:
        for word in sentences:
            predict.add(word)
    return predict

# 
def theNews(newsList, keywords):

    keyword = keywords #open(keywords, 'r')

#    line = keyword.read()
#    line = line.strip()
#    line = line.split('\n')

    for word in newsList:
        for words in keyword:
            if words in word:
                return word

def categories(keywords):
    print(keywords)

main()

# Below this line are relics from earlier versions of the program. They are not designed to work, just give me code examples if I wish to incorporate them later on.

#def newsDict(newsList, newsSet):
#    list1 = newsList
#    preDict = newsSet
#
#    diction = {}
#    for word in preDict:
#        diction[word] = list1.count(word)
#        print(word, list1.count(word))

#def newsDict():
#    s = newsList("news/cnn.txt")
#    s = list(s)
#    predict = newsSet()
#    diction = {}
#    for word in predict:
#        pass
#        diction[word] = word
    
#    average = 0
#    print(s)
#    for word in predict:
#        print(s.count(word))
#        diction[word] = s.count(word)
#    print(diction)
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

