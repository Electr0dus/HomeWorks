import time
import threading


def get_variables_1_to_10():
    for i in range(1, 10 + 1):
        print(i, flush=True)
        time.sleep(1)


def get_lettrs_a_to_j():
    list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in list_letters:
        print(i, flush=True)
        time.sleep(1)


t1 = threading.Thread(target=get_variables_1_to_10)
t2 = threading.Thread(target=get_lettrs_a_to_j)

t1.start()
t2.start()
t2.join()
