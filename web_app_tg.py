from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
BOT_TOKEN = "YOUR_BOT_TOKEN"

# URL вашего веб-приложения
WEB_APP_URL = "https://example.com"  # Замените на ваш URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет сообщение с кнопкой для открытия веб-приложения"""
    keyboard = [
        [InlineKeyboardButton("Открыть веб-приложение", web_app=WEB_APP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Привет! Нажми на кнопку ниже, чтобы открыть веб-приложение:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатие кнопки"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы открыли веб-приложение!")

def main():
    """Запускает бота"""
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()