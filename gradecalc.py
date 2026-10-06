english=int(input("enter the English Mark out of 50:"))
python=int(input("enter the python Mark out of 50:"))
java=int(input("enter the java Mark out of 50:"))
cpro=int(input("enter the cpro Mark out of 50:"))
logic=int(input("enter the logic Mark out of 50:"))
total=english+python+java+cpro+logic
avrgmark=total/5
if avrgmark>=40:
    print("A grade")
elif avrgmark>=30:
    print("B grade")
elif avrgmark>=20:
    print("C grade")
elif avrgmark>=10:
    print("D grade")
else:
    print("FAIL")

