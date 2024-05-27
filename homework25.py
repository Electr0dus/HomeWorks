def add_everything_up(a, b):
    try:
        c = a + b
    except TypeError:

        return f'{str(a)}{str(b)}'
    else:
        return a + b


print(add_everything_up(12, 'b'))
print(add_everything_up('строка', 23))
print(add_everything_up(12, 32.4))