import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_part = sys.argv[1]
    command, *params = command_part.split(':')
    command = command.lower().strip()

    amount = None
    if params and params[0] != "":
        try:
            amount = float(params[0])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")

        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")

        elif command == "display":
            account.display_balance()

        else:
            print("Invalid command.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()