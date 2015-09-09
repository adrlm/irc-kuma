from irc import handlers
from markov import gen as mk


def send_markov (chat_name):
   out = mk.gen_markov(chat_name)
   handlers.send_message(CHAN, out)
   print("[OUT] " + out)

commands = {
   '.markov':  send_markov
}

def parse_message(msg):
   if len(msg) == 1:
      msg = msg.split(' ')
      if msg[0] in commands:
         commands[msg[0]]()
   elif len(msg) >= 2:
      msg = msg.split(' ')
      if msg[0] in commands:
         commands[msg[0]](msg[1])

commands_op = {
   '.refresh': mk.refresh
}

def parse_message_op(msg):
   if len(msg) == 1:
      msg = msg.split(' ')
      if msg[0] in commands_op:
         commands_op[msg[0]]()
   elif len(msg) >= 2:
      msg = msg.split(' ')
      if msg[0] in commands_op:
         commands_op[msg[0]](msg[1])