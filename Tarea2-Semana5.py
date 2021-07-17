import logging
from typing import Text

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, message
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("Usuario %s Ha iniciado conversacion", user.first_name)
   
    keyboard = [
        [

            InlineKeyboardButton("Consultar la tasa de cambio de el dolar.",
            callback_data='el dolar en HN es 1USD=23HNL. Mas en: g.co/finance/USD-HNL'),
        ],
        [
            InlineKeyboardButton("Consultar la tasa de cambio de el euro.", 
            callback_data='el euro en HN es 1EUR=28HNL. Mas en: g.co/finance/EUR-HNL'),
            
        ],
        [   
            InlineKeyboardButton("Consultar el precio de el oro.", 
            callback_data='el oro en HN es 1KG=1,409,987.60HNL Mas en: goldprice.org/es')
        ],
        [   
            InlineKeyboardButton("Consultar el precio de el café.", 
            callback_data='el café en HN es 1KG=3,37USD. Mas en: cutt.ly/zmJZgsu')
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    user = update.effective_user
    update.message.reply_markdown_v2(
    fr'¡Hola {user.mention_markdown_v2()}\!, ¿Deseas realizar una consulta?',
        
    reply_markup=reply_markup)
    
    


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer("Permitame se esta cargando su peticion")
    query.edit_message_text(text=f"El valor de {query.data}")
    
 

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start para realizar otra consulta")
    
    


def main() -> None:
    updater = Updater("1837995131:AAFYIniZO8FM11P73Zl92ZIor1e9047P63M")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
    