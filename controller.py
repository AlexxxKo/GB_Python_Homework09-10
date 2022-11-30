from view import read_data, print_data, welcome, is_repeat
from mathRational import calculate
from mathComplex import calculate_complex
from log import result_log


def is_complex(dct: dict) -> bool:
    complex_number = False
    if dct['operator'] != '^':
        if str(dct['num1'])[-1] == 'i' or str(dct['num2'])[-1] == 'i':
            complex_number = True
        else:
            complex_number = False
    else:
        if str(dct['num1'])[-1] == 'i':
            complex_number = True
        else:
            complex_number = False
    return complex_number


def calc():
    welcome()
    end = False
    while not end:
        dct = read_data()
        if is_complex(dct):
            dct_result = calculate_complex(dct)
        else:
            dct_result = calculate(dct)
        result_log(dct_result)
        print_data(dct_result)

        end = is_repeat()

    print('До свидания.')
