# Main Bot Script for Ringgit Fighter
import time
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging for debugging purposes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start Command: Starts the game
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Game started! Ready to play Ringgit Fighter!')

# Help Command: Provide information about the bot
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Use /start to start the game, /help for instructions.')

# Game Command: Command to start a new round of the game
def game(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('A new round of Ringgit Fighter has started!')

# Error handling
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Get the bot token from the environment
    with open('.env', 'r') as file:
        TELEGRAM_TOKEN = file.readline().strip().split('=')[1]

    updater = Updater(TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("game", game))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
