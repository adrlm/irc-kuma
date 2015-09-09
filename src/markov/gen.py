import helpers, irc, markov

irc = irc.handlers


# Characters that define what lines to ignore for the output
WEECHAT = ['>>', '<<', '--', '-->', '<--', '@Satsuki']
IGNORE = ['.luser', 'Raw', '!user', '.s']

# Counter of how many words are in a message to be averaged later
chat_average = {}

def clean_file (file_):
   global chat_average
   word_count = []
   avg_words = 0

   """
   This will create a file of just user submitted messages.

   Weechat logs in the following format:

   YYYY-MM-DD HH:MM:SS USERNAME	MESSAGE
   YYYY-MM-DD HH:MM:SS << USERNAME (ADDRESS) has quit (REASON)
   """
   chat_name = file_.split('/')[-1].split('.')[2]
   irc.send_message(CHAN, "Just one second while refresh the logs.")
   print('[LOG] Creating clean output file for {0}.'.format(chat_name))

   file_i = open(file_, encoding="utf8").read().splitlines()
   file_o = open('clean_log_{0}'.format(chat_name), 'w', encoding="utf8")

   for line in file_i:
      try:
         msg = line.split('	') # Splits to [time / name / message] etc
         words = msg[2].split()  # Splits the message into words
         try:
            if msg[1] not in WEECHAT:
               if len(msg[2].split('::')) == 1:
                  if words[0] not in IGNORE:
                     if words[0].split(':')[0] not in ['http', 'https']:
                        word_count.append(len(words))
                        words.append('\n')
                        file_o.write(' '.join(words))
         except:
            pass
      except:
         pass
   chat_average[chat_name] = avg(word_count)
   file_o.close()


def refresh (chat_name):
   global chat_average

   clean_file('../../.weechat/logs/irc.animebytes.{0}.weechatlog'.format(chat_name))
   print('[LOG] Chat log file for {0} refreshed.'.format(chat_name))


def gen_markov (chat_name):
   global chat_average

   while True:
      try:
         file_ = open('clean_log_{0}'.format(chat_name), encoding="utf8")
         mk = markov.Markov(file_)
         return mk.generate_markov_text(chat_average[chat_name] + random.randint(0, int(chat_average[chat_name]/2)))
         break
      except FileNotFoundError:
         return "Sorry, either that log does not exist or you forgot to enter a parameter."
      except:
         refresh(chat_name)
   file_.close()