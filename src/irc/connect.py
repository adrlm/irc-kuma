import auth, socket


def init ():
   con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   data = ""

   con.connect((HOST, PORT))
   print("[LOG] Connected!")
   send_nick(NICK)

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
                  send_pong(line[1])

            if len(line) >= 2:
               if line[1] == 'MODE':
                  if joined == False:
                     send_message("NickServ", "IDENTIFY {0}".format(auth.PASS))
                     join_channel(CHAN)
                     joined = True
                     print("[LOG] Joined channel!")

               if line[1] == 'JOIN':
                  sender = get_sender(line[0])
                  if sender in OPS:
                     auto_op(sender)

               if line[1] == 'PRIVMSG':
                  sender = get_sender(line[0])
                  message = get_message(line)
                  print("[MSG] " + sender + ": " + message)
                  if sender in OPS:
                     parse_message_op(message)
                  parse_message(message)

      except socket.error:
         print("[ERR] Socket died")
         raise

      except socket.timeout:
         print("[ERR] Socket timeout")