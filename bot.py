import config
import bgg_api_reader
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    InlineQueryHandler,
)
from telegram.constants import ParseMode


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I'm BGG Telegram Bot. What game are you looking for?",
    )


# for handling inline search i.e. @botusername <query>
async def inline_query(
    update: Update, context: ContextTypes.DEFAULT_TYPE, answerCallbackQuery=None
) -> None:
    query = update.inline_query.query

    if query == "":
        return

    list_of_games = bgg_api_reader.get_list_of_board_games(query)

    results = []
    for game in list_of_games:
        print(f"User's query: {query}")
        print(game.name)
        results.append(
            InlineQueryResultArticle(
                id=game.name,
                title=f"{game.name} ({game.year_published})",
                input_message_content=InputTextMessageContent(
                    f"<b>{game.name} ({game.year_published})</b>",
                    parse_mode=ParseMode.HTML,
                ),
            )
        )

    await update.inline_query.answer(results)


def main() -> None:
    application = ApplicationBuilder().token(config.bot_token).build()

    #  Handling Bot commands
    start_handler = CommandHandler(["hello", "start"], start)
    application.add_handler(start_handler)

    # Handling searching board games (inline bot)
    application.add_handler(InlineQueryHandler(inline_query))

    # Method for initializing and starting the app
    application.run_polling()


if __name__ == "__main__":
    main()
