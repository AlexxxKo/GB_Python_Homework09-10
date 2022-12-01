import telebot

bot = telebot.TeleBot('5835523259:AAEsu5zaslzDpQ_-J9rZFEmbAUm0iNIbwBs')

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('C',callback_data='C'),
             telebot.types.InlineKeyboardButton('*',callback_data='*'),
             telebot.types.InlineKeyboardButton('/',callback_data='/'),
             telebot.types.InlineKeyboardButton('+',callback_data='+'),
             )
keyboard.row(telebot.types.InlineKeyboardButton('7',callback_data='7'),
             telebot.types.InlineKeyboardButton('8',callback_data='8'),
             telebot.types.InlineKeyboardButton('9',callback_data='9'),
             telebot.types.InlineKeyboardButton('i',callback_data='i'),
             )
keyboard.row(telebot.types.InlineKeyboardButton('4',callback_data='4'),
             telebot.types.InlineKeyboardButton('5',callback_data='5'),
             telebot.types.InlineKeyboardButton('6',callback_data='6'),
             telebot.types.InlineKeyboardButton('^',callback_data='**'),
             )
keyboard.row(telebot.types.InlineKeyboardButton('1',callback_data='1'),
             telebot.types.InlineKeyboardButton('2',callback_data='2'),
             telebot.types.InlineKeyboardButton('3',callback_data='3'),
             telebot.types.InlineKeyboardButton('-',callback_data='-'),
             )
keyboard.row(telebot.types.InlineKeyboardButton('',callback_data='no'),
             telebot.types.InlineKeyboardButton('0',callback_data='0'),
             telebot.types.InlineKeyboardButton('<=',callback_data='<='),
             telebot.types.InlineKeyboardButton('=',callback_data='='),
             )

@bot.message_handler(commands=['start','calculate'])
def getMassage(massage):
    global value 
    if value == '':
        bot.send_message(massage.from_user.id,'0', reply_markup=keyboard)
    else:
        bot.send_message(massage.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def calback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value =''
    elif data == '^':
        value ='**'
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or (0 !=old_value and value ==''):
        if value =='':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
        
    old_value = value
    if value == 'Ошибка': value = ''

bot.polling(none_stop=False,interval=0)

# def welcome():
#     print('\nПриветствуем Вас в калькуляторе Python!')


# def read_data() -> dict:
#     dct = {
#         'num1': '',
#         'num2': '',
#         'operator': '',
#         'result': '',
#     }

#     first_num = input('\nВведите рациональное или мнимое число: ')

#     operator = False
#     while not operator:
#         try:
#             math_action = input('''\nВыберите нужное действие из приведенных ниже:
#                 + для сложения
#                 - Для вычитания
#                 * Для умножения
#                 / Для деления
#                 ^ Для возведения в квадрат \n''')
#             if math_action == '^' or math_action == '*' or math_action == '/' or math_action == '+' or math_action == '-':
#                 operator = True
#             else:
#                 print('Нужно ввести корректный оператор\n')
#         except ValueError:
#             print('Нужно ввести корректный оператор\n')

#     if math_action != '^':
#         second_num = input('Введите второе число: ')
#         dct['num2'] = second_num
#     else:
#         dct['num2'] = '2'

#     dct['num1'] = first_num
#     dct['operator'] = math_action

#     return dct


# def print_data(dct: dict):
#     print(f"{dct['num1']} {dct['operator']} {dct['num2']} = {dct['result']}\n")


# def is_repeat():
#     repeat = input(
#         'Введите Y для повторения вычислений, или что угодно для выхода из калькулятора ')
#     if repeat.upper() != 'Y':
#         return True
#     else:
#         return False
