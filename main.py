import telebot 
from telebot import types
from congig import TOKEN

bot = telebot.TeleBot(TOKEN)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("супы","горячие блюда")
menu.row("десерты", "напитки")


dish = types.ReplyKeyboardMarkup(resize_keyboard= True)
dish.row("блюдо1", "блюдо2", "блюдо3")
dish.row("вернуться в меню")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "wellcom to coffe u annura , у нвс электронное меню", reply_markup=menu)

@bot.message_handler(func=lambda message: True)

def second(message):
    if message.text == "супы":
        bot.send_message (message.chat.id, "выберите суп", reply_markup=dish)
    elif message.text == "горячие блюда":
        bot.send_message(message.chat.id, " выберите блюда", reply_markup=dish)
    elif message.text == "десерты":
        bot.send_message(message.chat.id, "выберите напиток") 
    elif message.text == "напиток":
        bot.send_message(message.chat.id, "выберите напиток", reply_markup=dish)
    elif message.text == "вернутся в меню":
        bot.send_message(message.chat.id, "наше электронное меню")           

    elif message.text in ["блюдо1","блюдо2", "блюдо3"]:
        bot.send_message(message.chat.id, f"вы выбрали {message.text}")

bot.polling(non_stop=True)
