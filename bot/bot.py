import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from backend.api_client import call_api
from backend.formatter import toman

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

products = call_api(API_KEY,"get_all_product_details")
user_state = {}

async def start(update: Update, context):
    user_state[update.effective_user.id] = 0
    await send_product(update, context)

async def send_product(update, context):
    uid = update.effective_user.id
    idx = user_state.get(uid,0)
    if idx >= len(products):
        await update.message.reply_text("لیست تمام شد")
        return
    p = products[idx]
    text = f"📦 {p['name']}\n💰 {toman(p['sell_price'])}"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("⬅ قبلی", callback_data="prev"),
        InlineKeyboardButton("بعدی ➡", callback_data="next")
    ]])
    await update.message.reply_text(text, reply_markup=keyboard)

async def buttons(update: Update, context):
    q = update.callback_query
    uid = q.from_user.id
    if q.data == "next":
        user_state[uid] += 1
    elif q.data == "prev" and user_state[uid] > 0:
        user_state[uid] -= 1
    await q.answer()
    await q.message.delete()
    await send_product(update, context)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
