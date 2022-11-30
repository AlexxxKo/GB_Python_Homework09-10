from datetime import datetime


def result_log(dct: dict):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('calculator.log', 'a', encoding='utf-8') as file:
        file.write('{} --> {} {} {} = {}\n'
                   .format(time, dct['num1'], dct['operator'], dct['num2'], dct['result']))
