import logging
from googletrans import Translator
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram.ext import CallbackContext

# Enable logging to monitor the bot's activity
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Translator object
translator = Translator()

# Define the translation function
def translate_text(text: str, dest_lang='en'):
    # Translate the text into the destination language (English by default)
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

# Handle incoming messages and translate them
async def translate_message(update: Update, context: CallbackContext) -> None:
    # Get the message text
    original_message = update.message.text
    
    # Translate the message
    translated_message = translate_text(original_message)
    
    # Append the translation in the same message
    translated_text = f"\n\n[Translated]: {translated_message}"
    
    # Edit the original message to append the translation
    await update.message.reply_text(f"{original_message}{translated_text}")

# Start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("I will translate all your messages. Send a message and I will translate it.")

# Main function to run the bot
async def main() -> None:
    """Start the bot."""
    # Create the Application and use your bot's token here
    application = Application.builder().token("8153206681:AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo").build()

    # Register the handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

    # Run the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
