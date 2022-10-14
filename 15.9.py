import telebot
from telebot import types

bot = telebot.TeleBot("2110529010:AAH0tkIHL74pQbphax1XPt-D7avkEc2knL0")


@bot.message_handler(commands=['Рассчитать'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рассчитать объём')
    item2 = types.KeyboardButton('Рассчитать площадь')

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Что вы хотите рассчитать?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рассчитать объём':
            bot.send_message(message.chat.id, 'Введите объём')

        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Отлично, как сам?')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')


def process(message):
    try:
        global user_num1

        user_num1 = int(message.text)
bot.polling(none_stop=True)