from curses.ascii import isdigit
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
import re
import config # for storing bot token
from bs4 import BeautifulSoup

from Victoria_Cinema import Film



TOKEN_BOT = config.bot_token #inser your token here
updater = Updater(TOKEN_BOT, use_context=True)
    
def start(update: Update, context: CallbackContext):
    # stampa solamente il primo film  
    messageOdd = Film.Odd_Movie()
    update.message.reply_text(messageOdd)
            
    # stampa solamente il primo film
    messageEven = Film.Even_Movie()
    update.message.reply_text(messageEven)
    

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()


