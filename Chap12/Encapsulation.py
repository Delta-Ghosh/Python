class BankAccount:
    def __init__(self, balance):
        # Private attribute (encapsulated)
        self.__balance = balance
    
    # Deposit method (setter)
    def deposit(self):
        amount = int(input("Enter your deposit amount: "))
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method (setter)
    def withdraw(self):
        amount = int(input("Enter your withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")

    # Getter (to read balance safely)
    def get_balance(self):
        return self.__balance

account = BankAccount(100000)

# Show initial balance
print("Your starting bank balance is:", account.get_balance())

# Perform transactions
account.deposit()
account.withdraw()
print("Final Balance:", account.get_balance())

# ❌ Direct access won't work now
# print(account.__balance)   # AttributeError
