#! /usr/bin/env python
# Written by Joshua Jordi

import sys
import socket
import string

HOST='irc.freenode.net'
PORT=6667
NICK='TestPyBot'
IDENT='pybot'
REALNAME='Python Bot'
readbuffer=''

s=socket.socket()
s.connect((HOST,PORT))
s.send(('NICK %s\r\n' % NICK).encode('utf-8'))
s.send(('USER %s %s bla : %s\r\n' % (IDENT, HOST, REALNAME)).encode('utf-8'))
s.send(('JOIN ##isso-mnsu\r\n').encode('utf-8'))

while 1:
    readbuffer=readbuffer+s.recv(1024).decode()
    temp=readbuffer.split('\n')
    readbuffer=temp.pop()

    for line in temp:
        line=line.rstrip()
        line=line.split()

        if (line[0]=='PING'):
            s.send("PONG %s\r\n" % line[1])
#        for word in line:
#            print(word, end=' ')
        print(line)
