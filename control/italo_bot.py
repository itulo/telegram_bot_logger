import telebot
from entity.ediscussion import EDiscussion
from database.ddiscussion import DDiscussion

TOKEN = '133209286:AAHGctUjxMIE0I2EoXJdh0y83RRexlcbvik' # @italo_bot

class Italo_bot:
    def __init__(self, channel):
        self.channel = channel
        self.bot = telebot.TeleBot(TOKEN)

    def setup(self):
    	@self.bot.message_handler(func=lambda disc: disc.chat.title == self.channel)
    	def save_message(disc):
    		msg = EDiscussion().create_from_discussion(disc)
    		print msg.__dict__
    		DDiscussion.save(msg)

    def run(self):
    	self.bot.polling()
