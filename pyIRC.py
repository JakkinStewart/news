#! /usr/bin/python3
# Written by Joshua Jordi

# This program is designed to be a simple demonstration of a Python IRC client with SSL capabilities.
# From http://tools.ietf.org/html/rfc1459#section-3.3.2:
# The IRC protocol is a text-based protocol, with the simplest client being any socket program capable of connecting to the server.

# In its current stage, this IRC client fulfills the "simplest client" criteria. In the future, it will be updated to follow IRC client protocol and parse messages from IRC servers more cleanly.

import sys
import socket
import string
import ssl

# Asks user for input.
host = input("Enter IRC server [AnonOps]: ")
port = input("Enter port [6697]: ")
nick = input("Enter nick [PyIRC]: ")
chan = input("Enter channel [#news]: ")
Ssl = input("Do you want to use SSL? [Y/n]: ")

# If an input was left blank, use defaults.
if host == '': HOST='irc.anonops.com'
elif host != '': HOST=host
if port == '': PORT=6697
elif port != '': PORT=int(port)
if nick == '': NICK='PyIRC'
elif nick != '': NICK=nick
if chan == '': CHANNEL='#news'
elif chan != '': CHANNEL=chan
if Ssl == '' or Ssl.lower() == 'y': sslEnable='y'
elif Ssl.lower() == 'n': sslEnable='n'
else: exit("This is an unusual error. Contact JakkinStewart at Github to solve this.")

# Sets identity and realname for the IRC server.
IDENT='pyirc'
REALNAME='Python IRC Client'

# Begins readbuffer.
# Taken from http://archive.oreilly.com/pub/h/1968:
# You need a readbuffer because your might not always be able to read complete IRC commands from the server (due to a saturated Internet connection, operating system limits, etc).
readbuffer=''

# If SSL was enabled, wrap the socket in SSL.
if sslEnable.lower() == 'y': 
    ssL=socket.socket()
    ssL.connect((HOST,PORT))
    s = ssl.wrap_socket(ssL)

# Otherwise, don't wrap anything.
elif sslEnable.lower() == 'n': 
    s=socket.socket()
    s.connect((HOST,PORT))

# Send messages to the server containing the nick, identity, server, and realname. All messages must be encoded in utf-8.
s.send(('NICK %s\r\n' % NICK).encode('utf-8'))
s.send(('USER %s %s bla : %s\r\n' % (IDENT, HOST, REALNAME)).encode('utf-8'))

# Enter an infinite loop.
while 1:
    # Read 1024 bytes from the server and append it to the readbuffer. 
    readbuffer=readbuffer + s.recv(1024).decode()
    temp=readbuffer.split('\n')
    readbuffer=temp.pop()

    for line in temp:
        line=line.rstrip()
        line=line.split()

        print(line)

        if (line[0]=='PING'):
            s.send(("PONG %s\r\n" % line[1]).encode('utf-8'))
        if (line[1]=='MODE'):
            s.send(("JOIN %s\r\n" % CHANNEL).encode('utf-8'))

#        users = []
        message = ''
        user = ''

#        string = line[0]
#        temporary = string.split('!')
#        user = str(temporary[0])[1:]
        temp = ''
        for index, item in enumerate(line):
            if "x03" in item:
                print(item)
                line[index] = item[6:]
#        if str(x[3:])[1:3] == 'x0':
#            message += x[6:] + ' '
#        elif x[0] == ':':
#            message += x[1:-1] + ' '
#        else: message += x + ' '
#        print(message)
        if line[1] == 'PRIVMSG':
            string = line[0]
            temporary = string.split('!')
            user = str(temporary[0])[1:]
            y = line[3:]
            for x in y:
               if str(x[3:])[1:3] == 'x0':
                   message += x[6:] + ' '
               elif x[0] == ':':
                   message += x[1:-1] + ' '
               else: message += x + ' '
#       print(message)

            print(user, '|', message)
#        for word in line:
#             print(word[0], word[3], end=' ')
#        print()
#        print(line)


