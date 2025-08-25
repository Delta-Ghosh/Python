class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        ammount = int(input("Enter Your deposit ammount:"))
        if (ammount <= 0):
            print("Deposite minimum 1rs.")
        elif (ammount > 0):
            self.balance += ammount
            print(f"Deposited: {ammount}, New balance: {self.balance}")

    def withdraw(self):
        ammount = int(input("Enter your withdrawl ammount: "))
        if (ammount <= 0):
            print("withdrawl ammount must be positive.")
        elif (ammount > self.balance):
            print ("Insufficient funds!")

        else:
            self.balance -= ammount
            print(f"Withdrawled : {ammount}, New balance: {self.balance}")

    def get_balance(self):
        return self.balance
    
Account = BankAccount(100000)

print ("Your Balance is: ", Account.get_balance())
Account.deposit()
Account.withdraw()

print ("Final Balance:", Account.get_balance())