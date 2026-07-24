class BankAccount:
    def __init__(self):
        
        self.balance = 0
        self.status = "Closed"
    def get_balance(self):
        if self.status == "Open":
            return self.balance
        else:
            raise ValueError("account not open")
        

    def open(self):
        if self.status == "Closed":
            self.status = "Open"
        else:
            raise ValueError("account already open")
        
    def deposit(self, amount):
        if self.status != "Open":
            raise ValueError("account not open")
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if self.status != "Open":
            raise ValueError("account not open")
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("amount must be less than balance")
        self.balance = self.balance - amount

    def close(self):
        if self.status == "Open":
            self.status = "Closed"
            self.balance = 0
        else:
            raise ValueError("account not open")
