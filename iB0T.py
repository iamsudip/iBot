import socket

class iBot:
    def __init__(self):
        self.server = 'irc.freenode.net'
        self.nick = 'iBot'
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def initiate(self):
        try:
            self.ircsock.connect((self.server, 6667))
        except Exception, e:
            log_it(e)
            raise 
        self.ircsock.send("USER {username} {hostname} {servername} :{realname}\n".format(username=self.nick, hostname=self.nick, servername=self.nick, realname=self.nick))
        self.ircsock.send("NICK {nick}\n".format(nick=self.nick))

    def join(self, channel='#iamsudip'):
        self.ircsock.send("JOIN {channel}".format(channel=channel))

    def pong(self):
        self.ircsock.send("PONG :{message}\n".format(message='Saying something? Drop me private message.'))
        return

def log_it(data):
    pass

bot = iBot()
bot.initiate()
bot.join()

while True:
    ircmsg = bot.ircsock.recv(2048).strip('\n\r')
    if ircmsg.find("PING :") != -1:
        bot.pong()

