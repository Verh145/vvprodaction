import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6783422819:AAH0zyJwbu9z1QNFpZ13X68remRQpPprorc')
markup1 = types.InlineKeyboardMarkup()
markup2 = types.InlineKeyboardMarkup()
markup1.add(types.InlineKeyboardButton('Предложка', callback_data='delete'))
markup1.add(types.InlineKeyboardButton('Угадать промокод', callback_data='promo'))


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Спасибо, лошара!')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://vvproduction.ru/')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'<b>Здорова</b>, <em>пидр!</em> ({message.from_user.first_name})',
                     parse_mode='html', reply_markup=markup1)


@bot.message_handler()
def info(message):
    if 'физика' in message.text.lower():
        bot.send_message(message.chat.id, 'Ты Зоя?')
    elif '52' in message.text.lower():
        bot.reply_to(message, 'Это втаой')
    if 'впопиум' in message.text.lower():
        markup2.add(types.InlineKeyboardButton('Перейти в приватный канал', url='https://t.me/+LaTyjaeSWMgzYTQy'))
        bot.send_message(message.chat.id, 'А ты рил шаришь...', reply_markup=markup2)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Предложка')
    btn2 = types.KeyboardButton('Угадать промокод')
    markup.row(btn1, btn2)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Предложка':
        bot.send_message(message.chat.id, 'Кидай фото, чмо ебанное')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'promo':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
