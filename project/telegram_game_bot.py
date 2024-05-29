import telebot  # библиотека для бота (требует скачивания)
from telebot import types  # модуль для создания кнопок
from random import randrange

# токен бота
bot = telebot.TeleBot('6089059682:AAGRmoyozTWX3JURX_YZkYBMclENoWmHdVI')
number = randrange(1, 100, 1)

# запуск бота, start - это команда
# возможно добавление команд с тем же функционалом при
# добавлении команды в список


@bot.message_handler(commands=['start'])
def start(message):
    text_hello = 'Приветствую вас в Game_bot! Введите команду /list чтобы увидеть список игр'
    # создание кнопки для быстрых команд
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('/list')
    btn2 = types.KeyboardButton('/number')
    # вывод кнопок быстрых команд
    markup.row(btn)
    markup.row(btn2)
    # вывод текста, можно добавить смайлик,
    bot.send_message(message.chat.id, text_hello, reply_markup=markup)


# скрипт для обработки команды /site
@bot.message_handler(commands=['list'])
def list_gams(message):
    game_list = 'Список игр на данный момент\nУгадай число'
    bot.send_message(message.chat.id, game_list)


@bot.message_handler(commands=['number'])
def number(message):
    start = 'Начать игру'
    bot.send_message(message.chat.id, start)


# скрипт для обработки текста
@bot.message_handler()
def info(message):
    bot.reply_to(message, 'Такую команду я не знаю, поэтому просто повторю за вами')
    bot.send_message(message.chat.id, message.text)


# команда для того, чтобы проект работал, пока его не отключат
bot.infinity_polling()
