import logging
from telegram import InlineQueryResultGame, Update
from telegram.ext import Application, CommandHandler, InlineQueryHandler, CallbackQueryHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token and game short name
BOT_TOKEN = "6539738422:AAF8hDkjm86uOAZzbaT9zifMdWs7mSvXzCU"
GAME_SHORT_NAME = "DogeFlyer"

async def start(update: Update, context):
    logger.info("Start command received")
    await update.message.reply_text("Welcome to DogeFlyer! Use inline mode to share the game.")

async def inline_query(update: Update, context):
    logger.info("Inline query received")
    result = [InlineQueryResultGame(
        id="0",
        game_short_name=GAME_SHORT_NAME
    )]
    await update.inline_query.answer(result)

async def callback_query(update: Update, context):
    logger.info("Callback query received")
    await update.callback_query.answer(url="https://rollingsloanetoken.github.io/telegram-app/")

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