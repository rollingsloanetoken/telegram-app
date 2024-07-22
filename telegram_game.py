import logging
from telegram import InlineQueryResultGame, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, InlineQueryHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

BOT_TOKEN = "6539738422:AAF8hDkjm86uOAZzbaT9zifMdWs7mSvXzCU"
GAME_SHORT_NAME = "DogeFlyer"
GAME_URL = "https://rollingsloanetoken.github.io/telegram-app/"

async def start(update: Update, context):
    logger.info("Start command received")
    keyboard = [[InlineKeyboardButton("Play DogeFlyer", url=GAME_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to DogeFlyer! Click the button below to play:", reply_markup=reply_markup)

async def inline_query(update: Update, context):
    logger.info(f"Inline query received: {update.inline_query.query}")
    game_result = InlineQueryResultGame(
        id="0",
        game_short_name=GAME_SHORT_NAME
    )
    logger.info(f"Answering inline query with game: {GAME_SHORT_NAME}")
    await update.inline_query.answer([game_result], cache_time=1)

async def callback_query(update: Update, context):
    query = update.callback_query
    logger.info(f"Callback query received: {query.game_short_name}")
    await query.answer(url=GAME_URL)
    logger.info(f"Answered callback query with game URL: {GAME_URL}")

def main():
    logger.info("Starting bot...")
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(CallbackQueryHandler(callback_query))

    logger.info("Bot started, polling for updates...")
    application.run_polling()

if __name__ == '__main__':
    main()