class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        try:
            self._balance = float(initial_balance)
        except (TypeError, ValueError):
            raise ValueError("Initial balance must be a number.")

    def deposit(self, amount: float) -> None:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a number.")

        if amt <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amt

    def withdraw(self, amount: float) -> bool:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdraw amount must be a number.")

        if amt <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")

        if amt <= self._balance:
            self._balance -= amt
            return True
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self._balance:.2f}")