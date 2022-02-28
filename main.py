import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5248690115:AAG8LQrB0GIQh7MKOF_JUItcDF5qszINRUU')
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Как тебя зовут?", "/help", "/lobby")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['lobby'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/start", "/help", "ВУЗ","Как тебя зовут?","Пока")
    bot.send_message(message.chat.id, 'Выбери функцию, которой хочешь воспользоваться', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею направлять людей. Напиши "вуз" или кликни на кнопку я скину ссылку на сайт твоего ВУЗа')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "вуз":
        bot.send_message(message.chat.id, 'Тебе сюда – https://mtuci.ru/')
    if message.text.lower() == 'как тебя зовут?':
        bot.send_message(message.chat.id, 'Оливия!')
    if message.text.lower() == 'как у тебя дела?':
        bot.send_message(message.chat.id, 'Отлично! У тебя?')
    if message.text.lower() == 'тоже':
        bot.send_message(message.chat.id, '')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
bot.polling(none_stop=True, interval=0)