class BankAccount():
    def __init__(
            self,
            account_number: int,
            holder_name: str,
            balance: float
    ):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Balance: {self.balance}")


def manage_actions(
        accounts: dict,
        option: str
):
    if option == "5":
        print("Goodbye!")
        exit()
    elif option == "1":
        print("Create Account")
        name = input("Enter your name:").strip()
        new_account = BankAccount(len(accounts)+1, name, 0.0)
        accounts[new_account.account_number] = new_account
        print(f"Your Account Number is: {new_account.account_number}")

        initial_account_number += 1
    elif option == "2":
        account_number = int(input("Enter account number:"))
        amount = float(input("Enter amount to deposit:"))
        if account_number in accounts:
            accounts[account_number].deposit(amount)
        else:
            print(f"Cannot find account: {account_number}")
    elif option == "3":
        account_number = int(input("Enter account number:"))
        amount = float(input("Enter amount to withdraw:"))
        if account_number in accounts:
            accounts[account_number].withdraw(amount)
        else:
            print(f"Cannot find account: {account_number}")
    elif option == "4":
        account_number = int(input("Enter account number:"))
        if account_number in accounts:
            accounts[account_number].display_balance()
        else:
            print(f"Cannot find account: {account_number}")


def main():
    print("""
Welcome to the Bank Account Management System!

1. Create a new account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit"""
    )

    accounts = {}

    option = input("Choose and option: ").strip()
    while True:
        manage_actions(accounts, option)
        option = input("Choose and option: ").strip()


if __name__ == "__main__":
    main()