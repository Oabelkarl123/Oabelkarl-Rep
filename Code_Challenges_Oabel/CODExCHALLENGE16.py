class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        #mag desit ng pera
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₱{amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        #mag withdraw ng pera sa account
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₱{amount:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        #current balance.
        return self.balance

    def print_balance(self):
        #Prints the balance in the account.
        print(f"{self.name}'s Current Balance: ₱{self.balance:.2f}")

def breakdown_denomination(amount):
    #Breaks down the amount into Filipino denominations.
    denominations = {
        1000: '₱1000',
        500: '₱500',
        200: '₱200',
        100: '₱100',
        50: '₱50',
        20: '₱20',
        10: '₱10',
        5: '₱5',
        1: '₱1'
    }

    print("Denomination Breakdown:")
    for value, label in denominations.items():
        count = amount // value
        if count > 0:
            print(f"{label}: {count}")
        amount %= value

def main():
    print("Welcome to the bank")

#user entering account
    name = input("Enter  your name: ")
    initial_deposit = int(input("Enter your initial deposit (₱): "))
    account = BankAccount(name, initial_deposit)
    account.print_balance()

    while True: 
        print("\nMenu: ")
        print("1. Deposit")
        print("2. withdraw")
        print("3. Chech balance")
        print("4. BreakDown Denomination")
        print("5. Termination")

        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            deposit_amount = float(input("Enter deposit amount (₱): "))
            account.deposit(deposit_amount)
        elif choice == '2':
            withdraw_amount = float(input("Enter withdrawal amount (₱): "))
            account.withdraw(withdraw_amount)
        elif choice == '3':
            account.print_balance()
        elif choice == '4':
            amount_to_breakdown = float(input("Enter amount to breakdown (₱): "))
            breakdown_denomination(amount_to_breakdown)
        elif choice == '5':
            print("Terminating the program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
