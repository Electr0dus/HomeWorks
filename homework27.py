list_1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def qudra(x):
    return x**2

def is_not(x):
    if x % 2 != 0:
        return x

new_list = map(qudra, list(filter(is_not, list_1)))

print(list(new_list))
