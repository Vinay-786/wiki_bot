from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot_core import *
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("API_KEY")

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(CommandHandler('custom', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()
