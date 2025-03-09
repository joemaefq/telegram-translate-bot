from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator

API_TOKEN = 'AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo'  # Replace with your bot's API token

# Initialize the translator
translator = Translator()

def start(update: Update, context):
    update.message.reply_text('Hello! I am your translation bot. Send me any message, and I will translate it for you.')

def translate_message(update: Update, context):
    text = update.message.text
    lang = 'en' if update.message.from_user.language_code != 'en' else 'auto'

    # Translate the message to English or vice versa
    translated = translator.translate(text, src=lang, dest='en' if lang != 'en' else 'auto')

    # Send the translated message back
    update.message.reply_text(translated.text)

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
