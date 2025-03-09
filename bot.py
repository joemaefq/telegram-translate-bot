import os
import logging
from google.cloud import translate_v2 as translate
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Initialize Google Translate Client
translate_client = translate.Client()

# Telegram Bot Token (replace with your own token)
TELEGRAM_TOKEN = AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle incoming messages
def translate_message(text, target_language='en'):
    result = translate_client.translate(text, target_lang=target_language)
    return result['translatedText']

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Send me any message, and I'll translate it for you!")

# Function to handle the messages
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text  # Original text
    language_code = 'en' if update.message.from_user.language_code != 'en' else 'auto'  # Check if translation is needed
    
    # Translate to English or back to user's language
    translated_text = translate_message(text, target_language=language_code)
    
    # Send back the translated message
    update.message.reply_text(translated_text)

def main():
    """Start the bot."""
    updater = Updater(TELEGRAM_TOKEN)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
