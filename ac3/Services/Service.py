def calc(operation, number_1, number_2):
    if operation == '+':
        return number_1 + number_2

    elif operation == '-':
        return number_1 - number_2

    elif operation == '*':
        return number_1 * number_2

    elif operation == '/':
        return number_1 / number_2
    else:
        return 'Operador invalido, digite um operador valido para continuar'
