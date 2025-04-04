import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from openai import OpenAI




# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

# Hàm này sẽ được gọi khi người dùng gửi lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Xin chào, tôi có thể giúp gì được cho bạn?")

# Hàm này sẽ được gọi khi người dùng gửi tin nhắn bất kỳ
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=user_message)

# Khởi tao ứng dụng OpenAI client
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Lịch sử chat (list gồm nhiều tin nhắn, mỗi tin nhắn là 1 list [user_message, bot_message])
chat_history = []
 
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_history

    # Chuyển lịch sử chat thành định dạng mà OpenAI yêu cầu
    messages = []
    for user_message, bot_message in chat_history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": bot_message})
    
    # Thêm tin nhắn mới vào lịch sử
    user_message = update.message.text
    messages.append({"role": "user", "content": user_message})

    chat_completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
    )

    bot_message = chat_completion.choices[0].message.content
    chat_history.append([user_message, bot_message])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_message)


# Khởi tạo ứng dụng Telegram bot
application = ApplicationBuilder().token(BOT_TOKEN).build()

start_handler = CommandHandler("start", start)
application.add_handler(start_handler)

# echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
# application.add_handler(echo_handler)

chat_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat)
application.add_handler(chat_handler)

# Chạy bot cho đến khi bạn nhấn Ctrl-C
print("Bot is running...")
application.run_polling()