import threading
import queue
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.customers = []

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer = Customer(customer_number, self)
            self.customers.append(customer)
            customer.start()
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        table_assigned = False
        while not table_assigned:
            for table in self.tables:
                with table.lock:
                    if not table.is_busy:
                        print(f'Посетитель номер {customer.number} сел за стол {table.number}.')
                        table.is_busy = True
                        table_assigned = True
                        break
            if table_assigned:
                time.sleep(5)
                print(f'Посетитель номер {customer.number} покушал и ушёл.')
                with table.lock:
                    table.is_busy = False
            else:
                print(f'Посетитель номер {customer.number} ожидает свободный стол.')
                time.sleep(1)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

for customer in cafe.customers:
    customer.join()

print("Все клиенты обслужены, программа завершена.")