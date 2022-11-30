def calculate(dct: dict) -> dict:
    if dct['operator'] == '+':
        dct['result'] = is_float(float(dct['num1']) + float(dct['num2']))
    elif dct['operator'] == '-':
        dct['result'] = is_float(float(dct['num1']) - float(dct['num2']))
    elif dct['operator'] == '*':
        dct['result'] = is_float(float(dct['num1']) * float(dct['num2']))
    elif dct['operator'] == '/':
        if (float(dct['num2']) == 0):
            dct['result'] = 'На нуль делить нельзя'
        else:
            dct['result'] = is_float(float(dct['num1']) / float(dct['num2']))
    elif dct['operator'] == '^':
        dct['result'] = is_float(float(dct['num1']) * float(dct['num1']))
    return dct


def is_float(num: float) -> str:
    if num % 1 == 0:
        return str(int(num))
    else:
        return str(num)
