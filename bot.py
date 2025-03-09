import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the translator
translator = Translator()

API_TOKEN = '8153206681:AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo'  # Replace with your bot's API token

def start(update: Update, context):
    update.message.reply_text('Hello! I will automatically translate all messages to English.')

def translate_message(update: Update, context):
    original_message = update.message.text
    user_language = update.message.from_user.language_code

    # Only translate if it's not already in English
    if user_language != 'en':
        # Translate to English
        translated = translator.translate(original_message, src=user_language, dest='en')
        # Send translated message below the original
        update.message.reply_text(f"Original: {original_message}\n\nTranslated (to English): {translated.text}")
    else:
        # If it's already in English, translate back to the original language (or any other language)
        translated = translator.translate(original_message, src='en', dest=user_language)
        update.message.reply_text(f"Original: {original_message}\n\nTranslated (to {user_language}): {translated.text}")

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
