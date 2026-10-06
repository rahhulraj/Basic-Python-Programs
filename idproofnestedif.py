age=int(input("ENTER THE AGE :"))
idp=input("ID PROOF YES OR NO :")
if age>=18:
    if idp=='yes':
        print("ELIGIBLE FOR DRIVING LICENSE")
    else:
        print("YOU NEED ID PROOF")
else:
    print("YOU ARE NOT ELIGIBLE")
