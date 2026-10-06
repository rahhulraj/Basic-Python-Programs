org_pin = "1234"
balance = 100000

pin = input("Enter your PIN: ")

if pin == org_pin:
    amount = float(input("Enter withdrawal amount: "))
    
    if amount <= balance:
        print("Withdrawal successful.")
        print("Remaining balance:", balance - amount)
    else:
        print("Insufficient balance.")
else:
    print("Incorrect PIN.")