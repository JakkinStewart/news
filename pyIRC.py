#! /usr/bin/python3
# Written by Joshua Jordi

# This program is designed to be a simple demonstration of a Python IRC client with SSL capabilities.
# From http://tools.ietf.org/html/rfc1459#section-3.3.2:
# The IRC protocol is a text-based protocol, with the simplest client being any socket program capable of connecting to the server.

# In its current stage, this IRC client fulfills the "simplest client" criteria. In the future, it will be updated to follow IRC client protocol and parse messages from IRC servers more cleanly.

import socket
import ssl

# Asks user for input.
host = input("Enter IRC server [Freenode]: ")
port = input("Enter port [6697]: ")
nick = input("Enter nick [PythonIRCBot]: ")
chan = input("Enter channel [#temp]: ")
Ssl = input("Do you want to use SSL? [Y/n]: ")
logging = input("Do you want to enable logging? [Y/n]: ")
if logging.lower() == 'y':
    log = input("Where do you want save the log file? (Default is in currect directory.) ")
elif logging == '':
    log = './'


# If an input was left blank, use defaults.
if host == '': HOST='irc.freenode.net'
elif host != '': HOST=host
if port == '': PORT=6697
elif port != '': PORT=int(port)
if nick == '': NICK='PythonIRCBot'
elif nick != '': NICK=nick
if chan == '': CHANNEL='#temp'
elif chan != '': CHANNEL=chan
if Ssl == '' or Ssl.lower() == 'y': sslEnable='y'
elif Ssl.lower() == 'n': sslEnable='n'
if logging.lower() == '': logFile = open('%s.log' % CHANNEL, 'a')
elif logging.lower() == 'y':
    logFile = open(log + '%s.log' % CHANNEL, 'a')
elif logging.lower() == 'n':
    pass
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
    try:
    # Read 1024 bytes from the server and append it to the readbuffer.
        readbuffer=readbuffer + s.recv(1024).decode()
        temp=readbuffer.split('\n')
        readbuffer=temp.pop()
    
        for line in temp:
            line=line.rstrip()
            line=line.split()

            if (line[0]=='PING'):
                s.send(("PONG %s\r\n" % line[1]).encode('utf-8'))
            if (line[1]=='MODE'):
                s.send(("JOIN %s\r\n" % CHANNEL).encode('utf-8'))

            message = ''
            user = ''

            if line[1] == 'PRIVMSG':
                string = line[0]
                temporary = string.split('!')
                user = str(temporary[0])[1:]
                y = line[3:]
                for x in y:
                    if x[0] == ':':
                        message += x[1:] + ' '
                    else: message += x + ' '
                print(user, '|', message)
                ircChat = user + ' | ' + message +'\n'
                logFile.write(ircChat)
                logFile.flush()
    except KeyboardInterrupt:
        logFile.write('\nClosed\n')
        logFile.flush()
        print()
        exit('Closing')
