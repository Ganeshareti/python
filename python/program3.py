class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully.")
        else:
            print("Insufficient funds.")

    def view_balance(self):
        print(f"Current balance for {self.name}: {self.balance}")


def main():
    print("Welcome to the Bank!")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.view_balance()
        elif choice == "4":
            print("Thank you for using our service. Goodbye!")
            break
        else:
           
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
