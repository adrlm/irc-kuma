import auth, socket
from irc import commands, handlers


def init (host, port, chan, nick, ops):
   con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   data = ""

   con.connect((host, port))
   print("[LOG] Connected!")
   handlers.send_nick(nick)

   data = ""
   joined = False

   while True:
      try:
         data = data + con.recv(4096).decode('utf8')
         data_split = re.split(r"[~\r\n]+", data)
         data = data_split.pop()

         for line in data_split:
            line = str.rstrip(line)
            line = str.split(line)

            if len(line) >= 1:
               if line[0] == 'PING':
                  handlers.send_pong(line[1])

            if len(line) >= 2:
               if line[1] == 'MODE':
                  if joined == False:
                     handlers.send_message("NickServ", "IDENTIFY {0}".format(auth.PASS))
                     handlers.join_channel(chan)
                     joined = True
                     print("[LOG] Joined channel!")

               if line[1] == 'JOIN':
                  sender = handlers.get_sender(line[0])
                  if sender in ops:
                     handlers.auto_op(sender)

               if line[1] == 'PRIVMSG':
                  sender = handlers.get_sender(line[0])
                  message = handlers.get_message(line)
                  print("[MSG] " + sender + ": " + message)
                  if sender in ops:
                     commands.parse_message_op(message)
                  commands.parse_message(message)

      except socket.error:
         print("[ERR] Socket died")
         raise

      except socket.timeout:
         print("[ERR] Socket timeout")