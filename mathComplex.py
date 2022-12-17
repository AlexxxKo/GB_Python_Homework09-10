def split_number(dct: dict, is_square: bool = False) -> dict:
    if dct['operator']:
        numbers = dct['num1'].split(dct['operator'])
        dct['num1'] = numbers[0]
        dct['num2'] = numbers[1]

        if is_square:
            dct = calculate_complex(dct)
            num_complex = []
            if dct['result'][0] == '-':
                num_complex = dct['result'][1:].split('-')
                if len(num_complex) == 1:
                    num_complex = num_complex[0].split('+')
                num_complex[0] = '-' + num_complex[0]
            else:
                num_complex = dct['result'].split('-')
                if len(num_complex) == 1:
                    num_complex = num_complex[0].split('+')
            double = 2 * float(num_complex[0]) * float(num_complex[1][:-1])
            par = ''
            if double < 0:
                par = '-'
            else:
                par = '+'

            dct['result'] = str(pow(float(num_complex[0]), 2) -
                                pow(float(num_complex[1][:-1]), 2)) + par + str(abs(double)) + 'i'
            return dct['result']
        else:
            return calculate_complex(dct)['result']
    else:
        return square_complex(dct['num1'])


def calculate_complex(dct: dict):
    num1 = dct['num1']
    is_num1_complex = False
    is_num2_complex = False
    num2 = dct['num2']

    if dct['num1'][-1] == 'i':
        is_num1_complex = True

    if dct['num2'][-1] == 'i':
        is_num2_complex = True

    if dct['operator'] == '+':
        dct['result'] = sum_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '-':
        dct['result'] = sub_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '*':
        dct['result'] = mult_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '/':
        dct['result'] = div_complex(
            is_num1_complex, is_num2_complex, num1, num2)

    return dct


def sum_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    if is_num1_complex and is_num2_complex:
        number = float(num1[:-1]) + float(num2[:-1])
        if number != 0:
            if number % 1 == 0:
                result = str(int(number)) + 'i'
            else:
                result = str(number) + 'i'
        else:
            result = '0'
    elif is_num1_complex:
        number = float(num1[:-1])
        if number % 1 == 0:
            number = int(number)
        if float(num2) % 1 == 0:
            num2 = int(num2)

        if num2 != 0:
            if number > 0:
                result = '{}+{}i'.format(num2, number)
            elif number < 0:
                result = '{}-{}i'.format(num2, abs(number))
            else:
                result = str(num2)
        else:
            if number != 0:
                result = f'{number}i'
            else:
                result = '0'
    else:
        number = float(num2[:-1])
        if number % 1 == 0:
            number = int(number)
        if float(num1) % 1 == 0:
            num1 = int(num1)

        if num1 != 0:
            if number > 0:
                result = '{}+{}i'.format(num1, number)
            elif number < 0:
                result = '{}-{}i'.format(num1, abs(number))
            else:
                result = str(num1)
        else:
            if number != 0:
                result = f'{number}i'
            else:
                result = '0'

    return result


def sub_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    if is_num1_complex and is_num2_complex:
        number = float(num1[:-1]) - float(num2[:-1])
        if number != 0:
            if number % 1 == 0:
                result = str(int(number)) + 'i'
            else:
                result = str(number) + 'i'
        else:
            result = '0'
    elif is_num1_complex:
        number = float(num1[:-1])
        if number % 1 == 0:
            number = int(number)
        if float(num2) % 1 == 0:
            num2 = int(num2)

        if num2 != 0:
            if number > 0:
                result = '{}+{}i'.format(num2 * (-1), number)
            elif number < 0:
                result = '{}-{}i'.format(num2 * (-1), abs(number))
            else:
                result = str(num2 * (-1))
        else:
            if number != 0:
                result = f'{number}i'
            else:
                result = '0'
    else:
        number = float(num2[:-1])
        if number % 1 == 0:
            number = int(number)
        if float(num1) % 1 == 0:
            num1 = int(num1)

        if num1 != 0:
            if number > 0:
                result = '{}-{}i'.format(num1, number)
            elif number < 0:
                result = '{}+{}i'.format(num1, abs(number))
            else:
                result = str(num1)
        else:
            if number != 0:
                result = f'{number * (-1)}i'
            else:
                result = '0'

    return result


def mult_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''

    if is_num1_complex and is_num2_complex:
        number = float(num1[:-1]) * float(num2[:-1])
        if number != 0:
            if number % 1 == 0:
                number = int(number)
            result = str(number * (-1))
        else:
            result = '0'
    else:
        if is_num1_complex:
            number = float(num1[:-1]) * float(num2)
        else:
            number = float(num1) * float(num2[:-1])

        if number != 0:
            if number % 1 == 0:
                number = int(number)
            result = f'{number}i'
        else:
            result = '0'

    return result


def div_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    if is_num1_complex:
        num1 = float(num1[:-1])
    if is_num2_complex:
        num2 = float(num2[:-1])

    if float(num2) != 0:
        number = float(num1) / float(num2)
        if number != 0:
            if number % 1 == 0:
                number = int(number)

            if is_num1_complex and is_num2_complex:
                result = str(number)
            elif is_num1_complex:
                result = f'{number}i'
            else:
                result = f'{number * (-1)}i'
        else:
            result = '0'
    else:
        result = 'На нуль делить нельзя'

    return result


def square_complex(num: str) -> str:
    result = ''
    number = float(num[:-1])
    number = number * number * (-1)
    if number % 1 == 0:
        result = str(int(number))
    else:
        result = str(number)

    return result
