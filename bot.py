from translate import Translator
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Initialize Translator
def get_translator(target_lang):
    return Translator(to_lang=target_lang)

# Define the translation function
def translate_text(text: str, target_lang: str) -> str:
    try:
        translator = get_translator(target_lang)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f"Error in translation: {e}"

# Define a function to handle messages
def handle_message(update: Update, context: CallbackContext) -> None:
    original_text = update.message.text
    target_lang = 'en'  # Default target language
    # Set target language based on the user's locale or your preference
    target_lang = 'en'  # Change this according to your use case (e.g., 'es', 'fr')

    translated_text = translate_text(original_text, target_lang)

    # Send translated message under the original message
    update.message.reply_text(f"{original_text}\n\nTranslated: {translated_text}")

# Define a start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your translation bot. Send any message to translate.")

def main():
    # Replace 'YOUR-BOT-TOKEN' with your bot's API token
    updater = Updater("8153206681:AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.Filters.text & ~filters.Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a stop signal (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
