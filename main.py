import deposit
import withdraw
import balance
import statement

while True:
    print("\n--- ATM Simulation ---")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        balance.show_balance()
    elif choice == "2":
        deposit.deposit_money()
    elif choice == "3":
        withdraw.withdraw_money()
    elif choice == "4":
        statement.show_statement()
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice!")
