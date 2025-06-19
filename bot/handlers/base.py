from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"Пользователь {user.full_name} ({user.username} / {user.id}) вызвал /start")
    await update.message.reply_text(f"Привет, {user.first_name}! Я бот. Напиши /help чтобы узнать команды.")

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"Пользователь {user.full_name} ({user.username} / {user.id}) вызвал /help")
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — Запустить бота\n"
        "/help — Помощь\n"
        "/profile — Посмотреть профиль"
    )
