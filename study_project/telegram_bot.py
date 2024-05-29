import telebot  # библиотека для бота (требует скачивания)
from telebot import types  # модуль для создания кнопок
import webbrowser  # библиотека для открытия веб страниц (встроенная)

# токен бота
bot = telebot.TeleBot('6854897795:AAGQcnyqih6RDAJB_QoywZMCGMzLCsseKd8')

# запуск бота, start - это команда
# (в коде добавление / - не требуется, в телеграмме требуется),
# возможно добавление команд с тем же функционалом при
# добавлении команды в список


@bot.message_handler(commands=['start'])
def start(message):
    text_hello = 'Приветствую вас в Game_bot! Введите команду /site чтобы начать игру'
    # создание кнопки для быстрых команд
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('/site')
    # вывод кнопок быстрых команд
    markup.row(btn)
    # вывод текста, можно добавить смайлик,
    # скопировав его из Telegram
    bot.send_message(message.chat.id, text_hello, reply_markup=markup)


# скрипт для обработки команды /site
@bot.message_handler(commands=['site'])
def site(message):
    # команда для открытия сайта
    webbrowser.open('https://www.youtube.com/shorts/THEXl1yJu4s')  # адрес сайта


# скрипт для обработки текста
@bot.message_handler()
def info(message):
    # шуточная функция повторение (вместо простой ошибки)
    bot.reply_to(message, 'Такую команду я не знаю, поэтому просто повторю за вами')
    bot.send_message(message.chat.id, message.text)


# команда для того, чтобы проект работал, пока его не отключат
bot.infinity_polling()
