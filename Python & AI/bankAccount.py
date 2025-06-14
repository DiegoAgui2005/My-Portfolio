class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self, amount):
            if self.is_active:
                self.balance += amount
                print(f"Depósito de {amount}. Saldo actual {self.balance} ")
            else:
                print("Cuenta inactiva")    
                    
    def withdraw(self, amount):
            if self.is_active:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Retiro de {amount}. Saldo actual {self.balance}")
                        
    def deactivate(self):
            self.is_active = False
            print(f"Cuenta inactiva")
                
    def activate(self):
            self.is_active = True
            print(f"Cuenta activa")
            
            
account1 = BankAccount("Diego",1000)
account2 = BankAccount("Juan",10000)
            
    # Calling methods
account1.deposit(500)
account2.deposit(100)
account1.deactivate()
account1.deposit(1000)      
account1.activate()
account1.deposit(1000)      