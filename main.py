import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("TOKEN")

def first_memo(update: Update, context: CallbackContext):
    update.message.reply_text("📘 مذكرة أولى ثانوي:\n[ضع الرابط هنا]")

def first_explain(update: Update, context: CallbackContext):
    update.message.reply_text("🎧 شرح أولى ثانوي:\n[ضع الرابط هنا]")

def second_memo(update: Update, context: CallbackContext):
    update.message.reply_text("📘 مذكرة تانية ثانوي:\n[ضع الرابط هنا]")

def second_explain(update: Update, context: CallbackContext):
    update.message.reply_text("🎧 شرح تانية ثانوي:\n[ضع الرابط هنا]")

def third_memo(update: Update, context: CallbackContext):
    update.message.reply_text("📘 مذكرة تالتة ثانوي:\n[ضع الرابط هنا]")

def third_explain(update: Update, context: CallbackContext):
    update.message.reply_text("🎧 شرح تالتة ثانوي:\n[ضع الرابط هنا]")

def menu(update: Update, context: CallbackContext):
    keyboard = [["أولى ثانوي", "تانية ثانوي", "تالتة ثانوي"]]
    update.message.reply_text("اختار السنة:", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))

def handle_text(update: Update, context: CallbackContext):
    text = update.message.text
    mapping = {
        "أولى ثانوي": (first_memo, first_explain),
        "تانية ثانوي": (second_memo, second_explain),
        "تالتة ثانوي": (third_memo, third_explain),
    }
    if text in mapping:
        funcs = mapping[text]
        context.user_data["funcs"] = funcs
        keyboard = [["📘 مذكرة", "🎧 شرح"]]
        update.message.reply_text(f"اختر نوع المحتوى للسنة {text}:", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    elif text in ["📘 مذكرة", "🎧 شرح"]:
        funcs = context.user_data.get("funcs")
        if funcs:
            funcs[0](update, context) if text=="📘 مذكرة" else funcs[1](update, context)
    else:
        menu(update, context)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("first_memo", first_memo))
    dp.add_handler(CommandHandler("first_explain", first_explain))
    dp.add_handler(CommandHandler("second_memo", second_memo))
    dp.add_handler(CommandHandler("second_explain", second_explain))
    dp.add_handler(CommandHandler("third_memo", third_memo))
    dp.add_handler(CommandHandler("third_explain", third_explain))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
