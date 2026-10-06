choice = int(input("ATM Menu\n1. Deposit\n2. Withdraw\n3. Balance\nEnter your choice: "))

match choice:
    case 1:
        print("Deposit selected")
    case 2:
        print("Withdraw selected")
    case 3:
        print("Balance selected")
    case _:
        print("Invalid choice")