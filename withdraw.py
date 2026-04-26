import utils

def withdraw_money():
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > utils.balance:
        print("Insufficient balance!")
    else:
        utils.balance -= amount
        utils.transactions.append(f"Withdrawn ₹{amount}")
        print("Amount withdrawn successfully!")
