import logging
from googletrans import Translator
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the translator
translator = Translator()

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a message, and I will translate it below.')

# Function to handle messages and translate them
def translate(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    translated = translator.translate(text, dest='en')  # You can change 'en' to your target language
    
    translated_text = translated.text
    
    # Send back the original message followed by the translation
    update.message.reply_text(f"Original: {text}\n\nTranslation: {translated_text}")

def main():
    # Use your bot token here
    TOKEN = AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo

    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
