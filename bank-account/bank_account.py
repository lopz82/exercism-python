from threading import Lock


class BankAccount:
    def __init__(self):
        self._balance = None
        self.lock = Lock()
        self.opened = False

    def _validate_is_not_closed(self):
        if not self.opened:
            raise ValueError("Cannot operate in a closed account")

    def _validate_amount(self, amount: int):
        if amount <= 0:
            raise ValueError("Cannot deposit a negative or zero amount")

    def get_balance(self):
        with self.lock:
            self._validate_is_not_closed()
            return self._balance

    def open(self):
        with self.lock:
            if self.opened:
                raise ValueError("Account already open")
            self.opened = True
            self._balance = 0

    def deposit(self, amount: int):
        with self.lock:
            self._validate_is_not_closed()
            self._validate_amount(amount)
            self._balance += amount

    def withdraw(self, amount: int):
        with self.lock:
            self._validate_is_not_closed()
            if amount > self._balance:
                raise ValueError("Not enough cash")
            self._validate_amount(amount)
            self._balance -= amount

    def close(self):
        with self.lock:
            self._validate_is_not_closed()
            self.opened = False
