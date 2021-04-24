import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json


# Load Telegram bot token from config.json (which should be added to .gitignore)
with open('config.json') as f:
    token = json.load(f)['token']

# Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create updater
updater = Updater(token=token)
dispatcher = updater.dispatcher

# Functions to do send messages
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This bot has been started (using the command /start)") 
def echo(update, context):
    # User's message obtained via update.message.text
    user_message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=user_message)
    
# Add command handler to start the app with '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Add command handler to echo normal messages
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Start the bot
updater.start_polling()

# To stop the bot
# updater.stop()