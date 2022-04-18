from curses.ascii import isdigit
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from distutils.command import clean
from os import sep, times_result
import requests
import re
import config # for storing bot token
from bs4 import BeautifulSoup


class Film:
    def __init__(self, poster, time_slots, reservation):
        self.poster = poster # all data about the movie
        self.time_slots = time_slots # day and time of movie 
        self.reservation = reservation # link for reservate a seat

TOKEN_BOT = config.bot_token #inser your token here
updater = Updater(TOKEN_BOT, use_context=True)
    
def start(update: Update, context: CallbackContext):
    
    url = "https://www.victoriacinema.it/victoria_cinema/index.php"
    body = requests.get(url)
    body_text = body.content
    soup = BeautifulSoup(body_text, 'lxml')

    update.message.reply_text("Ecco i film di oggi:")
    divsOdd = soup.find_all("div", class_="filmContainer oddFilm")
    messageOdd = ""
    #oddFilm loop
    for div in divsOdd:
        idfilm = div.find_all("div",  class_="scheda")
        idfilm = re.findall(r"\D(\d{5})\D", str(idfilm))
        poster = ""
        time_slots = []
        reservation = ""

        divs3 = div.find_all("div", class_="datiFilm")
        #Film data
        for div1 in divs3:

            reservation = "https://www.victoriacinema.it/generic/scheda.php?id=" + str(idfilm).strip("['']") + "&idcine=1760&idwt=5103#inside"
            for clean_strip in list (div1.stripped_strings):
                poster += " " + clean_strip
                
        #getting the day and the time for each film in the theater
        divs2 = div.find_all("ul", class_="orari")
        for div2 in divs2:
            for clean_strip in list(div2.stripped_strings):
                time_slots.append(clean_strip)

        f = Film(poster, time_slots, reservation)  
        messageOdd = f.poster + "\nProiezioni:\n" + "".join(str("\n" + elem + ":\n") if elem.isalpha() else str(elem + "   ") for elem in f.time_slots )+ "\nLink Prenotazione:\n" + f.reservation +"\n\n\n"
        update.message.reply_text(messageOdd)
        
        

    divsEven = soup.find_all("div", class_="filmContainer evenFilm")
    messageEven = ""
    #evenFilm loop
    for div in divsEven:
        idfilm = div.find_all("div",  class_="scheda")
        idfilm = re.findall(r"\D(\d{5})\D", str(idfilm))
        poster = ""
        time_slots = []
        reservation = ""

        divs3 = div.find_all("div", class_="datiFilm")
        #Film data
        for div1 in divs3:

            reservation = "https://www.victoriacinema.it/generic/scheda.php?id=" + str(idfilm).strip("['']") + "&idcine=1760&idwt=5103#inside"
            for clean_strip in list (div1.stripped_strings):
                poster += " " + clean_strip
                
        #getting the day and the time for each film in the theater
        divs2 = div.find_all("ul", class_="orari")
        for div2 in divs2:
            for clean_strip in list(div2.stripped_strings):
                time_slots.append(clean_strip)
        
        f = Film(poster, time_slots, reservation)
        messageOdd = f.poster + "\nProiezioni:\n" + "".join(str("\n" + elem + ":\n") if elem.isalpha() else str(elem + "   ") for elem in f.time_slots )+ "\nLink Prenotazione:\n" + f.reservation +"\n\n\n"
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