import config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I'm BGG Telegram Bot. What game are you looking for?",
    )


async def search_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # todo: add logic for searching board games using BGG API
    print(update.message.text)
    await update.message.reply_text(text=f"Here are results for {update.message.text}")


if __name__ == "__main__":
    application = ApplicationBuilder().token(config.bot_token).build()

    #  Handling bot commands
    start_handler = CommandHandler(["hello", "start"], start)
    search_handler = CommandHandler("search", search_game)

    application.add_handler(start_handler)
    application.add_handler(search_handler)

    # Method for initializing and starting the app
    application.run_polling()
