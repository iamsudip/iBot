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

    def join(self, channel='#bcrec'):
        self.ircsock.send("JOIN {channel}\n".format(channel=channel))
        self.ircsock.send("Nickserv IDENTIFY {password}\n".format(password='password'))
        
    def pong(self, server):
        self.ircsock.send("PONG {server}\n".format(server=server))
        return

    def replypm(self, target, buddy=None, flagforpm=False):
        if flagforpm:
            self.ircsock.send("PRIVMSG {target} :Hi! {target}.\n".format(target=target))
            return
        else:
            self.ircsock.send("PRIVMSG {target} :Hi! {buddy}.\n".format(target=target, buddy=buddy))          

def log_it(data):
    pass

bot = iBot()
bot.initiate()
bot.join()

while True:
    ircmsg = bot.ircsock.recv(2048).strip('\n\r')
    splitircmsg = ircmsg.split()
    if "PING" in splitircmsg:
        bot.pong(ircmsg[1])
        continue
    if bot.nick in ircmsg and "PRIVMSG" in ircmsg:
        target = splitircmsg[0].split('!~')[0][1:]
        #print ircmsg
        if not splitircmsg[2].startswith('#'): # Check if message to bot is in channel
            bot.replypm(target, flagforpm=True) # Send pm to target
            continue
        else:
            bot.replypm(splitircmsg[2], buddy=target) # Message buddy in channel
            continue