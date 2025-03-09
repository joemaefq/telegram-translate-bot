from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from deep_translator import GoogleTranslator
import re

# Replace this with your actual bot token from BotFather
TOKEN = AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo

# Function to check if the text is English
def is_english(text):
    return bool(re.match(r'^[A-Za-z0-9\s\.,!?\'\"]+$', text))

# Function to handle incoming messages
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if is_english(text):
        update.message.reply_text(text)  # No translation needed
    else:
        translated_text = GoogleTranslator(source="auto", target="en").translate(text)
        update.message.reply_text(f"{text}\n\n🔹 *Translation:* {translated_text}", parse_mode="Markdown")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add a handler for text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
