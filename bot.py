import config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hello! I'm BGG Telegram Bot. What game are you looking for?")

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.bot_token).build()

    #  Handling /start command
    start_handler = CommandHandler(['hello', 'start'], start)
    application.add_handler(start_handler)

    # Method for initializing and starting the app
    application.run_polling()
