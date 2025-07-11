from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import handlers as h
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Произошла ошибка: %s", context.error)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_error_handler(error_handler)
    app.add_handler(CommandHandler("start", h.start_handler))
    app.add_handler(CommandHandler("help", h.help_handler))
    app.add_handler(CommandHandler("profile", h.profile_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
