# =============================================
# CLASE PADRE: BankAccount (Cuenta Bancaria)
# =============================================

class BankAccount:
    def __init__(self, balance=0):
        #Constructor: initialize the balance of the account
        #If no balance is provided, it initializes at 0
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the account"""
        if amount > 0: # validate that the amount is positive   
            self.balance += amount # add the balance
            print(f"✅ Deposito exitoso: +${amount}. Balance actual: ${self.balance}")
        else:
            print(f'❌ Error: El monto debe de ser positivo')

    def withdraw(self, amount):
        """Method to withdraw money from the account"""
        if amount > 0 and self.balance >= amount: # validate that the amount is positive and the balance is greater or equal to the amount
            self.balance -= amount # subtract the balance
            print(f"✅ Retiro exitoso: -${amount}. Balance actual: ${self.balance}" )
        else:
            print(f"❌ Error: El monto debe de ser positivo y el balance debe ser mayor o igual al monto")
# =============================================
# CLASE HIJA: SavingsAccount (Cuenta de Ahorros)
# ============================================= 

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        # constructor: inherit balance and add the minimum balance
        super().__init__(balance) # call the parent class constructor
        self.min_balance = min_balance # minimum balance(new exclusive attribute)

    def withdraw(self, amount):
        """Method to withdraw with minimum balance validation"""
        if self.balance - amount >= self.min_balance: # validate that the balance is greater or equal to the minimum balance
            super().withdraw(amount) # call the parent class withdraw method
        else:
            #error message if the balance is less than the minimum balance
            print(f"❌ Error: No puedes retirar ${amount}. "
                f"El saldo minimo dede ser de (${self.min_balance}). "
                f"Balance actual: ${self.balance}") 

# =============================================
# DEMOSTRACIÓN PRÁCTICA
# =============================================
if __name__ == "__main__":
    print("🏦 Bienvenido al sistema de cuentas bancarias 💰")
    banck_accaunt = BankAccount(1000) # create a normal account with $1000 balance
    banck_accaunt.deposit(500)        # deposit $500
    banck_accaunt.withdraw(200)       # withdraw $200
    banck_accaunt.withdraw(2000)      # try to withdraw $2000 (not possible)

    print("\n🔍 Estado de las cuentas:")
    savings_account = SavingsAccount(balance=1000, min_balance=200)# minimum balance $200
    savings_account.deposit(300) # deposit $300
    savings_account.withdraw(1000) # withdraw $1000 (valid, remaining $300)
    savings_account.withdraw(150) # try to withdraw $150(invalid, remaining $150 < $200)