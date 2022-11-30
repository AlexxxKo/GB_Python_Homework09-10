def welcome():
    print('\nПриветствуем Вас в калькуляторе Python!')


def read_data() -> dict:
    dct = {
        'num1': '',
        'num2': '',
        'operator': '',
        'result': '',
    }

    first_num = input('\nВведите рациональное или мнимое число: ')

    operator = False
    while not operator:
        try:
            math_action = input('''\nВыберите нужное действие из приведенных ниже:
                + для сложения
                - Для вычитания
                * Для умножения
                / Для деления
                ^ Для возведения в квадрат \n''')
            if math_action == '^' or math_action == '*' or math_action == '/' or math_action == '+' or math_action == '-':
                operator = True
            else:
                print('Нужно ввести корректный оператор\n')
        except ValueError:
            print('Нужно ввести корректный оператор\n')

    if math_action != '^':
        second_num = input('Введите второе число: ')
        dct['num2'] = second_num
    else:
        dct['num2'] = '2'

    dct['num1'] = first_num
    dct['operator'] = math_action

    return dct


def print_data(dct: dict):
    print(f"{dct['num1']} {dct['operator']} {dct['num2']} = {dct['result']}\n")


def is_repeat():
    repeat = input(
        'Введите Y для повторения вычислений, или что угодно для выхода из калькулятора ')
    if repeat.upper() != 'Y':
        return True
    else:
        return False
