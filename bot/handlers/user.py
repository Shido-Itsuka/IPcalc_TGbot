from telegram import Update
from telegram.ext import ContextTypes

async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Профиль:\nИмя: {user.full_name}\nID: {user.id}"
    )
