class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        print(f"Your account balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount:.2f} to {recipient}")
            print(f"Transferred ${amount:.2f} to {recipient}")
        else:
            print("Invalid amount for transfer or insufficient funds in your account.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    account1 = ATM()
    account2 = ATM()

    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            account1.display_balance()
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            account1.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            account1.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter the transfer amount: $"))
            account1.transfer(amount, account2)
        elif choice == '5':
            account1.show_transaction_history()
        elif choice == '6':
            print("Thank you for using our ATM. Have a good day ahead!")
            break
        else:
            print("Invalid option selected. Please select a valid option.")

if __name__ == "__main__":
    main()
