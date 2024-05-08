val = int(input('Введите число от 3 до 20 '))
while val  < 3 or val > 20:
    val = int(input('Введите число от 3 до 20 '))

# list_val.append(1)  # записать первую единицу, которая встречается во всех примерах

# проверить число на кратность

def old_shivr(val):
    list_val = []  # для хранения чисел
    str_val = None
    number1 = 1  # для записи первого слагаемого
    number2 = 1  # для записи второго слагаемого
    while number1 and number2 <= val:
        if val % (number1 + number2) == 0:
            if number1 == number2:
                number2 += 1
                continue
            str_val = str(number1) + str(number2)
            list_val.append(str_val)
        if number2 == val:
            number1 += 1
            number2 = number1 + 1
            continue
        number2 += 1
    return list_val


print(old_shivr(val))
