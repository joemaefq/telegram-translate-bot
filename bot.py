import os
from googletrans import Translator
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set the language based on the system's country setting (you can replace with custom logic)
import locale
user_locale = locale.getdefaultlocale()[0]

# Initialize Translator
translator = Translator()

# Define your translation function
def translate_text(text: str, target_lang: str) -> str:
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Error in translation: {e}"

# Define a function to handle messages
def handle_message(update: Update, context: CallbackContext) -> None:
    original_text = update.message.text
    target_lang = 'en'  # Default target language
    # Here we can detect the user's language or derive it from locale
    if user_locale != 'en_US':
        target_lang = user_locale.split('_')[0]

    translated_text = translate_text(original_text, target_lang)
    
    # Send translated message under the original message
    update.message.reply_text(f"{original_text}\n\nTranslated: {translated_text}")

# Define a start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your translation bot. Send any message to translate.")

def main():
    # Replace '8153206681:AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo' with your bot's API token
    updater = Updater('YOUR-BOT-TOKEN')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a stop signal (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
