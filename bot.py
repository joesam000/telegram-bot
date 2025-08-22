import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from sheets_helper import get_sheet
from gpt_helper import ask_chatgpt

SHEET_NAME = "Panduan Cust Support  - LUXEGAMING"
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("Hello 👋 Ask me anything from the support sheet!")

async def handle_message(update, context):
    question = update.message.text
    
    # Get sheet data
    sheet = get_sheet(SHEET_NAME)
    rows = sheet.get_all_records()
    
    # Limit rows for efficiency (or filter specific column)
    data = rows[:15]
    
    # Ask GPT
    answer = ask_chatgpt(question, data)
    await update.message.reply_text(answer)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
