import telebot, wikipedia, re
# Создаем экземпляр бота
bot = telebot.TeleBot('5248690115:AAG8LQrB0GIQh7MKOF_JUItcDF5qszINRUU')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею направлять людей. Напиши "вуз" и я скину ссылку на сайт твоего ВУЗа')

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