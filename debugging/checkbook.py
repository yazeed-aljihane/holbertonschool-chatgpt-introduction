#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        if action == 'exit':
            break
        elif action == 'balance':
            cb.get_balance()
        elif action in ['deposit', 'withdraw']:
            try:
                # محاولة تحويل المدخل إلى رقم
                amount = float(input(f"Enter the amount to {action}: $"))
                
                # التأكد من أن المبلغ ليس سالباً
                if amount < 0:
                    print("Error: Amount cannot be negative.")
                    continue
                
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
                    
            except ValueError:
                # التعامل مع المدخلات غير الرقمية
                print("Invalid input. Please enter a numeric value (e.g., 10.50).")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
