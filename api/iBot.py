import socket
import sys
import time

class iBot:
    def __init__(self):
        self.server = 'irc.freenode.net'
        self.nick = 'iBot'
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def initiate(self, password=""):
        try:
            self.ircsock.connect((self.server, 6667))
        except Exception, e:
            log_it(e)
            raise 
        self.ircsock.send("USER {username} {hostname} {servername} :{realname}\n".format(username=self.nick, hostname=self.nick, servername=self.nick, realname=self.nick))
        self.ircsock.send("NICK {nick}\n".format(nick=self.nick))
        self.ircsock.send("Nickserv IDENTIFY {password}\n".format(password=password))
        return

    def join(self, channel):
        self.ircsock.send("JOIN #{channel}\n".format(channel=channel))
        return

    def pong(self, server):
        self.ircsock.send("PONG {server}\n".format(server=server))
        return

    def replypm(self, target, buddy=None, flagforpm=False):
        if flagforpm:
            self.ircsock.send("PRIVMSG {target} :Hi! {target}.\n".format(target=target))
            return
        else:
            self.ircsock.send("PRIVMSG {target} :Hi! {buddy}.\n".format(target=target, buddy=buddy))
            return      


class iLogger(file_pointer):
    pass
