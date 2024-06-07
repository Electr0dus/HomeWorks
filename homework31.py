def is_prime(func):
    def wrapper(a, b, c):
        flag = 0
        result = func(a, b, c)
        for i in range(2, result):
            if result % i == 0:
                flag = 0
                break
        else:
            flag = 1
        if flag:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 1, 8))
