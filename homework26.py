class NotInt(Exception):
    def __init__(self, val):
        self.val = val


class NotList(Exception):
    def __init__(self, list_):
        self.list_ = list_


def PrinterValue(val):
    if isinstance(val, int):
        return val
    else:
        raise NotInt(f'Это не целое число {val}')


def PrinterList(list_):
    if isinstance(list_, list):
        return list_
    else:
        raise NotList(f'Это не список {list_}')


try:
    PrinterValue(12)
    PrinterList(10)
except NotInt as exc:
    print(f'Ошибка {exc}')
except NotList as exc:
    print(f'Ошибка {exc}')
finally:
    print('Программа завершена!')