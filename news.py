#! /usr/bin/env python3
# Written by Joshua Jordi

import newsin

outFile = open("news.txt", "w")

writeIn = newsin.news("cnn.txt")

for word in writeIn:
    print(word, writeIn[word])
#outFile.write(writIn)
