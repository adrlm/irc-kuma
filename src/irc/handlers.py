# IRC commands
class Handlers (self, con):

   def __init__ (self, con):
      self.con = con

   def _pong (msg):
      con.send(bytes('PONG %s\r\n' % msg, 'utf8'))

   def _message (chan, msg):
      con.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'utf8'))

   def _mode (chan, mode, user):
      con.send(bytes('MODE %s %s: %s\r\n' % (chan, mode, user), 'utf8'))

   def _nick (nick):
      con.send(bytes('USER %s %s %s %s\n' % (nick, nick, nick, nick), 'utf8'))
      con.send(bytes('NICK %s\n' % nick, 'utf8'))

   def _pass (password):
      con.send(bytes('PASS %s\r\n' % password, 'utf8'))

   def _channel (chan):
      con.send(bytes('JOIN %s\r\n' % chan, 'utf8'))

   def _channel (chan):
      con.send(bytes('PART %s\r\n' % chan, 'utf8'))


# IRC chat functions
def get_sender (msg):
   result = ""
   for char in msg:
      if char == "!":
         break
      if char != ":":
         result += char
   return result

def get_message (msg):
   result = ""
   i = 3
   length = len(msg)
   while i < length:
      result += msg[i] + " "
      i += 1
   result = result.lstrip(':')
   return result


# Automod function.
def auto_op (username):
   send_mode(CHAN, "+o", username)