import threading


class BankAccount(threading.Thread):
    all_cash = 1000

    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = lock

    def deposit(self, cash):
        with self.lock:
            self.all_cash += cash
        print(f'Deposited {cash}, new balance {self.all_cash}', flush=True)

    def withdraw(self, cash_remove):
        with self.lock:
            self.all_cash -= cash_remove
        print(f'Withdrew {cash_remove}, new balance is {self.all_cash}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = threading.Lock()

myDeposit = BankAccount(lock)

deposit_thread = threading.Thread(target=deposit_task, args=(myDeposit, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(myDeposit, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
