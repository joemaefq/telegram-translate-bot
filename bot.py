import logging
from googletrans import Translator  # Using googletrans for translation
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Initialize Google Translate client using googletrans
translator = Translator()

# Telegram Bot Token (replace with your own token)
TELEGRAM_TOKEN = AAGLzg5J9Z9OeoFpfCkK0-Vgsra10tR4EZo

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle incoming messages
def translate_message(text, target_language='en'):
    result = translator.translate(text, dest=target_language)
    return result.text  # Return translated text

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Send me any message, and I'll translate it for you!")

# Function to handle the messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text  # Original text
    language_code = 'en' if update.message.from_user.language_code != 'en' else 'auto'  # Check if translation is needed
    
    # Translate to English or back to user's language
    translated_text = translate_message(text, target_language=language_code)
    
    # Send back the translated message
    await update.message.reply_text(translated_text)

def main():
    """Start the bot."""
    # Create the Application object (which replaced the Updater class)
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Add message handler (for handling text messages)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
