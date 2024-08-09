import telebot 
from telebot import types
from adress import TOKEN

bot = telebot.TeleBot(TOKEN)

mygroup = types.ReplyKeyboardMarkup(resize_keyboard=True)
mygroup.row("our group", "about group")
choosegr = types.ReplyKeyboardMarkup(resize_keyboard= True)
choosegr.row("our group", "about group")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "wellcom to itc", reply_markup= choosegr)
@bot.message_handler(func=lambda message: True)

def second(message):
    if message.text == "our group":
        bot.send_message(message.chat.id, " good group" ,reply_markup=choosegr)
    elif message.text ==  "about group":
        bot.send_message(message.chat.id, "Annur, Arkadii mentor, lamar, Shirin", reply_markup=choosegr)
    elif message.text == "вернутся в меню":
        bot.send_message(message.chat.id, "наше электронное меню")
    elif message.text in ["our group", "about group"]:
        bot.send_message(message.chat.id, f"this is our group")

bot.polling(non_stop=True)
