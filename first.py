# ek bankaccount class banao jisme deposit, withdraw ho ,aur agar balance se zyda withdraw karne toh insufficientbalance ka naam ka custom error throw kare
class InsufficientBalanceError(Exception):
    def __init__(self, message="Account me balance nahi hai!"):
        self.message = message
        super().__init__(self.message)
# BankAccount Class
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(self.balance, "rupees deposit ho gaye hain.")
            print(f"New Balance: ₹{self.balance}")
        else:
            print("Deposit amount 1000 se zyada hona chahiye!")
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Error: Aap ₹{amount} nikalna chahte hain, par aapka balance sirf ₹{self.balance} hai!")
        elif amount <= 0:
            print("Withdraw amount 0 se zyada hona chahiye!")
        else:
            self.balance -= amount
            print(f"₹{amount} successfully nikale gaye.")
            print(f"Bacha hua Balance: ₹{self.balance}")

a=BankAccount("Gaurav")
a.deposit(15000)
a.withdraw(15000)
try:    
    a.withdraw(1000)  # This will raise InsufficientBalanceError
except InsufficientBalanceError as e:
    print(e)