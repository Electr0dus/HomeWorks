# Фабрики функций
def ret_math(expr):
    if expr == '+':
        def math_func(x, y):
            return x + y
    elif expr == '-':
        def math_func(x, y):
            return x - y
    elif expr == '*':
        def math_func(x, y):
            return x * y
    else:
        raise Exception('Нет такого математического выражения!')
    return math_func
print('Задача 1: Фабрика функций')

summ = ret_math(expr='+')
minus = ret_math(expr='-')
mult = ret_math(expr='*')
# div = ret_math(expr='/')

print(summ(x=2, y=6))
print(minus(x=2, y=6))
print(mult(x=2, y=6))


# Лямбла-Функции
def var_2(x):
    return x ** 2


func = lambda x: x ** 2
print('Задача 2 лямбда')
print(func(10))
print(var_2(11))


# Вызываемые объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print(f'Стороны: {self.a}, {self.b}')
        return f'Площадь прямоугольника равна {self.a * self.b}'


S_ = Rect(5, 7)
print('Задача 3: Вызываемые объекты')
print(S_())
