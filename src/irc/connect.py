import auth, socket
import irc


def init (host, port, chan, nick, ops):
   con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   data = ""

   con.connect((host, port))
   print("[LOG] Connected!")
   send_nick(nick)

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
                  irc.handlers.send_pong(line[1])

            if len(line) >= 2:
               if line[1] == 'MODE':
                  if joined == False:
                     irc.handlers.send_message("NickServ", "IDENTIFY {0}".format(auth.PASS))
                     irc.handlers.join_channel(chan)
                     joined = True
                     print("[LOG] Joined channel!")

               if line[1] == 'JOIN':
                  sender = irc.handlers.get_sender(line[0])
                  if sender in ops:
                     irc.handlers.auto_op(sender)

               if line[1] == 'PRIVMSG':
                  sender = irc.handlers.get_sender(line[0])
                  message = irc.handlers.get_message(line)
                  print("[MSG] " + sender + ": " + message)
                  if sender in ops:
                     irc.commands.parse_message_op(message)
                  irc.commands.parse_message(message)

      except socket.error:
         print("[ERR] Socket died")
         raise

      except socket.timeout:
         print("[ERR] Socket timeout")