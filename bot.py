import sys
from control.italo_bot import Italo_bot

def usage():
	print "Please provide a channel"

def run_bot(channel):
	bot = Italo_bot(channel)
	bot.setup()
	bot.run()

if len(sys.argv) == 1:
	usage()
else:
	run_bot(sys.argv[1])