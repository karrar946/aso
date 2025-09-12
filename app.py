import telebot

# ضع التوكن هنا
TOKEN = "8083436685:AAHO7SzPu--ImuSl8BtL2jplLzooJ2V6uxA"

# ضع ال ID الخاص بك هنا إذا تحتاجه
ADMIN_ID = 1800163946  

bot = telebot.TeleBot(TOKEN)

# دالة ترد على أي رسالة أو أمر
@bot.message_handler(func=lambda message: True)
def maintenance_mode(message):
    bot.reply_to(message, "🚧 البوت تحت الصيانة حالياً 🚧")

print("البوت يعمل... (لكن كل شيء يرد بصيانة)")
bot.infinity_polling()
