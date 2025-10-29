from utils.bank_acconut import BankAccount



if __name__ == "__main__":
    bank_account = BankAccount("Alice")
    bank_account.deposit(1000)
    print(bank_account.get_balance())  # Output: 1000
    bank_account.withdraw(900)
    print(bank_account.get_balance())  # Output: 100
    bank_account.set_interest_rate(0.1)
    bank_account.apply_interest()
    print(bank_account.get_balance())  # Output: 110.0