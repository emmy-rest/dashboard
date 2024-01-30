class ATM:
    def __init__(self):
        # Initialize accounts dictionary (Account Number: [PIN, Balance, Transaction History])
        self.accounts = {
            '1234567890': ['1234', 1000.0, []],
            '9876543210': ['5678', 500.0, []],
        }
        self.current_account = None

    def authenticate_user(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number][0] == pin:
            self.current_account = account_number
            return True
        return False

    def check_balance(self):
        return self.accounts[self.current_account][1]

    def deposit(self, amount):
        self.accounts[self.current_account][1] += amount
        self.accounts[self.current_account][2].append(f'Deposit: +${amount}')

    def withdraw(self, amount):
        if self.accounts[self.current_account][1] >= amount:
            self.accounts[self.current_account][1] -= amount
            self.accounts[self.current_account][2].append(f'Withdrawal: -${amount}')
            return True
        return False

    def display_transaction_history(self):
        return self.accounts[self.current_account][2]

    def logout(self):
        self.current_account = None


def main():
    atm = ATM()

    while True:
        print("\n==== ATM Simulator ====")
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if atm.authenticate_user(account_number, pin):
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transaction History")
                print("5. Logout")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    balance = atm.check_balance()
                    print(f"Your balance: ${balance}")
                elif choice == '2':
                    amount = float(input("Enter deposit amount: $"))
                    atm.deposit(amount)
                    print("Deposit successful.")
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: $"))
                    if atm.withdraw(amount):
                        print("Withdrawal successful.")
                    else:
                        print("Insufficient funds.")
                elif choice == '4':
                    history = atm.display_transaction_history()
                    print("\nTransaction History:")
                    for transaction in history:
                        print(transaction)
                elif choice == '5':
                    atm.logout()
                    print("Logged out. Thank you for using the ATM.")
                    break
                else:
                    print("Invalid choice. Please entere a number between 1 and 5.")

        else:
            print("Authentication failed. Please check your account number and PIN.")


if __name__ == "__main__":
    main()
