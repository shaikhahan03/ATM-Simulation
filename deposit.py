import utils

def deposit_money():
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        utils.balance += amount
        utils.transactions.append(f"Deposited ₹{amount}")
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")
