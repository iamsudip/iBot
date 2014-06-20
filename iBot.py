#!/usr/bin/env python

import atexit
import sys
import api.iBot
import api.iBot_functions

def iColor(text, color='default'):
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'default': '39',
        'gray': '90',
        'white': '97', 
    }
    try:
        sys.stdout.write("\033[{color}m{text}\033[0m\n".format(color=colors[color], text=text))
    except IndexError:
        sys.stdout.write(text)
    else:
        sys.stdout.write(text)

def iExit():
    iColor("[*] iBot initializing exit process.", 'red')
    try:
        del bot
    except NameError:
        pass
    iColor("Done!", "green")
    sys.exit(0)

def iController():
    """
    Controls the colors of the text depending upon the activity
    """
    pass

if __name__ == '__main__':
    bot = iBot()
    bot.initiate(sys.argv[1])
    atexit.register(iExit)
    
    for channel in sys.argv[2:]:
        bot.join(channel)

    while True:
        ircmsg = bot.ircsock.recv(2048).strip('\n\r')
        splitircmsg = ircmsg.split()
        if "PING" in splitircmsg:
            bot.pong(ircmsg[1])
            continue
        if bot.nick in ircmsg and "PRIVMSG" in ircmsg:
            target = splitircmsg[0].split('!~')[0][1:]
            print ircmsg
            if not splitircmsg[2].startswith('#'): # Check if message to bot is in channel
                bot.replypm(target, flagforpm=True) # Send pm to target
                continue
            else:
                bot.replypm(splitircmsg[2], buddy=target) # Message buddy in channel
                continue
        if "PRIVMSG" in ircmsg:
            if ircmsg.split(":")[2].startswith('s/'):
                print "ssssss"
