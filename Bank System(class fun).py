class BankAccount:
    def __init__(self,acc_holder,acc_balance = 0):
        self.name = acc_holder
        self.balance = acc_balance
        print(f"\nNew Account Created Successfully for {self.name} with {self.balance} Balance...")
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"\n{amount} was Deposited Successfully")
        else:
            print("\nInvalid Amount!")
            
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"\n{amount} withdrawl succesfully ,Account balance is {self.balance}")
            else:
                print(f'\nInsufficient Balance, Current Balance : {self.balance}')
        else:
            print("\nInvalid Amount to Withdraw!")
            
    def check_balance(self):
        print(f"\nAccount Holder:{self.name} , Account Balance :{self.balance} ")
            
print("\n.............Banking Operation...............")

first_account = BankAccount("Gamer", 1000)

first_account.deposit(500)
first_account.withdraw(300)
first_account.withdraw(2000)
first_account.check_balance()

print("\n--------------------------\n")


sec_account = BankAccount("Suriya")

sec_account.deposit(200)
sec_account.withdraw(50)
sec_account.check_balance()
