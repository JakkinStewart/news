#! /usr/bin/env python
# Written by Joshua Jordi

import sys
import socket
import string
import ssl
from time import sleep

HOST='irc.anonops.com'
PORT=6697
NICK='TestPyBot'
IDENT='pybot'
REALNAME='Python Bot'
readbuffer=''

sslsocket=socket.socket()
sslsocket.connect((HOST,PORT))
s = ssl.wrap_socket(sslsocket)
s.send(('NICK %s\r\n' % NICK).encode('utf-8'))
s.send(('USER %s %s bla : %s\r\n' % (IDENT, HOST, REALNAME)).encode('utf-8'))
#s.send(('QUOTE PONG oxiDWBqeAK\r\n').encode('utf-8'))
#sleep(5)
#s.send(('JOIN #news\n').encode('utf-8'))

while 1:
    readbuffer=readbuffer+s.recv(1024).decode()
    temp=readbuffer.split('\n')
    readbuffer=temp.pop()

    for line in temp:
        line=line.rstrip()
        line=line.split()

        if (line[0]=='PING'):
            s.send(("PONG %s\r\n" % line[1]).encode('utf-8'))
        if (line[1]=='MODE'):
            s.send(("JOIN #news\r\n").encode('utf-8'))
        for word in line:
            print(word, end=' ')
        print()
#        print(line)
