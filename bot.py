import telebot
from dotenv import load_dotenv
import os

from mathComplex import split_number
from log import result_log

load_dotenv()
secret_token = os.getenv('TOKEN')
bot = telebot.TeleBot(secret_token)

value = ''
old_value = ''
is_complex = False
dct = {
    'num1': '',
    'num2': '',
    'operator': '',
    'result': ''
}

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('x2', callback_data='**'),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton('i', callback_data='i'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start', 'calculater'])
def getMessage(message):
    bot.send_message(message.from_user.id,
                     '\nПриветствуем Вас в тестовом калькуляторе трёх Александров!')
    bot.send_message(message.from_user.id,
                     '\nКалькулятор принимает 2 числа и нужную операцию. Числа могут быть и комплексными.')
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value, is_complex, dct
    is_end = False
    data = query.data

    if data == '/' or data == '*' or data == '+' or data == '-':
        if not dct['operator']:
            dct['operator'] = data
            value += data
        else:
            is_end = True
            try:
                if is_complex:
                    dct['num1'] = value
                    dct['result'] = split_number(dct)
                    value = dct['result']
                else:
                    value = str(eval(value))
            except:
                value = 'Ошибка!'
    else:
        if data == 'i':
            if value[-1] != 'i':
                value += data
                is_complex = True
        elif data == 'C':
            value = ''
            dct = {
                'num1': '',
                'num2': '',
                'operator': '',
                'result': ''
            }
            is_complex = False
        elif data == '<=':
            if value != '':
                if value[-1] == '/' or value[-1] == '*' or value[-1] == '+' or value[-1] == '-':
                    dct['operator'] = ''
                elif value[-1] == 'i' and value[:-1].find('i') == -1:
                    is_complex = False
                value = value[:len(value)-1]
        elif data == '**':
            is_end = True
            if is_complex:
                dct['num1'] = value
                dct['result'] = split_number(dct, True)
                dct['num1'] = value + '^2'
                value = dct['result']
            else:
                dct['num1'] = value + '^2'
                value = f'{value}*{value}'
                value = str(eval(value))
                dct['result'] = value
        elif data == '=':
            is_end = True
            try:
                val = value
                dct['num1'] = value
                if is_complex:
                    dct['result'] = split_number(dct)
                    value = dct['result']
                else:
                    value = str(eval(value))
                    dct['result'] = value
                dct['num1'] = val
            except:
                value = 'Ошибка!'
        else:
            value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value

    old_value = value

    if value == 'Ошибка!':
        value = ''
    if is_end:
        result_log(dct)
        value = ''
        dct = {
            'num1': '',
            'num2': '',
            'operator': '',
            'result': ''
        }
        is_complex = False
    is_end = False


if __name__ == '__main__':
    bot.polling(none_stop=False, interval=0)
