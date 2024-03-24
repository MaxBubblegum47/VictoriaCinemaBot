import pickle
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

help_text = (
    "Benvenuto! Se vuoi vedere che film sono attualmente al cinema digita /start \n"
    "Se preferisci avere informazioni riguardo le tariffe digita /info \n"
)

def start(update: Update, context: CallbackContext):
    
    messageEvenLoad = []
    messageOddLoad = []
    
    # Load the information from the file
    with open('saveEven.txt', 'rb') as file:
        messageEvenLoad = pickle.load(file)

    with open('saveOdd.txt', 'rb') as file:
        messageOddLoad = pickle.load(file)

    for elem in messageOddLoad:
        update.message.reply_text(elem)
    
    for elem in messageEvenLoad:    
        update.message.reply_text(elem)

def price(update: Update, context: CallbackContext):
    # Price and other information
    price_text = (
        "*BIGLIETTO INTERO*\n"
        "Ingresso Intero: tutto il giorno € 9,00\n"
        "Mercoledi': esclusi festivi e prefestivi € 7,00\n"
        "Pomeridiano: spettacoli prima delle ore 19.00, esclusi sabato, domenica, festivi e prefestivi € 7,00\n\n"
        
        "*BIGLIETTO RIDOTTO*\n"
        "Bambini dai  3 ai 12 anni: tutti i giorni € 7,00\n"
        "Over 65: dal lunedì al venerdì, prefestivi fino alle ore 18:59 € 7,00\n"
        "Militari: tutti i giorni € 7,00\n"
        "Accompagnatori disabili: tutti i giorni € 7,00\n"
        "Invalidi: tutti i giorni € 7,00\n"
        "Giornalisti: tutti i giorni € 7,00\n"
        "Universitari: ogni lunedì, esclusi festivi e prefestivi € 6,00\n"
        "Tessera IO STUDIO: da lunedì a mercoledì, esclusi festivi e prefestivi € 6,00\n\n"

        "*CONVENZIONI*\n"
        "AGIS: lunedì e martedì, esclusi festivi e prefestivi € 7,00\n"
        "Intestatari tessere Coop: ingresso ridotto per possessore e accompagnatore, da lunedì a giovedì tutto il giorno e venerdì per gli spettacoli prima delle 20:59, esclusi festivi e prefestivi € 7,00\n"
        "Intestatari tessere UISP: da lunedì a giovedì, esclusi festivi e prefestivi € 7,00\n\n"

        "*PROIEZIONE IN 3D*\n"
        "Intero 3D: tutto il giorno € 10,50\n"
        "Ridotto 3D: tutto il giorno € 8,50\n"
        "Universitari 3D: ogni lunedì, esclusi festivi e prefestivi € 7,50\n"
        "Tessera IO STUDIO 3D: da lunedì a mercoledì, esclusi festivi e prefestivi € 7,50\n"
        "Tessera Coop 3D: da lunedì a giovedì tutto il giorno e venerdì per gli spettacoli prima delle 20:59, esclusi festivi e prefestivi € 8,50\n"
    )
    
    update.message.reply_markdown(price_text)

def info(update: Update, context: CallbackContext):
    info_text = (
        "Da noi puoi spendere il tuo Bonus Cultura 18APP/ Bonus Docente\n\n"
        "I VOUCHER VANNO SCARICATI CON LA FUNZIONE ESERCIZIO FISICO E NON VENDITA ON LINE\n\n"
        "Per le proiezioni evento non sono valide le cinecard\n"
        "Il biglietto per i film Atmos è maggiorato di 1 €\n\n"

        "Il costo di prenotazione per l'acquisto online è di 0,50 €, le prenotazioni vanno ritirate\n"
        "almeno 30 minuti prima dell'orario di inizio del film.\n"
        "Il locale si riserva la possibilità di spostare i posti acquistati o prenotati a seconda delle necessità.\n\n" 
        
        "Importante! Per i film in uscita il mercoledì il prezzo del biglietto sarà intero.\n"
        "Per le visioni 3D non sono valide le tessere VCard, sono invece valide le tessere VCard 3D. La tariffa pomeridiana non è valida nelle giornate\n"
        "dal 19 dicembre al 10 gennaio compreso. Per gli eventi fuori dalla normale programmazione il prezzo e le convenzioni potrebbero\n"
        "subire delle variazioni indipendenti dalla Direzione.\n\n"

        "Si informa la gentile clientela che i film inizieranno circa 10/15 minuti dopo l'orario indicato.\n"
        "La programmazione potrebbe subire variazioni indipendenti dalla Direzione.\n"
    )

    update.message.reply_markdown(info_text)


def help(update: Update, context: CallbackContext):
    update.message.reply_text(help_text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("'%s' non e' un comando valido. Se vuoi vedere i film disponibili in sala digita /film, se vuoi avere informazioni o prezzi digita rispettivamente: /info oppure /prezzi" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("'%s' non e' un comando valido. Se vuoi vedere i film disponibili in sala digita /film, se vuoi avere informazioni o prezzi digita rispettivamente: /info oppure /prezzi" % update.message.text)  

def main():
    # new main
    application = Application.builder().token('6846511727:AAFcGoxXj6rSqbqSQ_JTzZZdvjTzZDhdEj8').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


    # # old main
    # # Get the dispatcher to register handlers
    # updater = Updater(token=TOKEN, use_context=True)
    # dp = updater.dispatcher

    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("film", start))
    # dp.add_handler(CommandHandler("prezzi", price))
    # dp.add_handler(CommandHandler("price", price))
    # dp.add_handler(CommandHandler("info", info))
    # dp.add_handler(CommandHandler("help", help))

    # # Filters out unknown commands
    # dp.add_handler(MessageHandler(Filters.command, unknown))
  
    # # Filters out unknown messages.
    # dp.add_handler(MessageHandler(Filters.text, unknown_text))

    # updater.start_polling(timeout=30, drop_pending_updates=True)
    # updater.idle()


if __name__ == "__main__":
    main()


