year=int(input("ENTER THE YEAR:"))
if year%4==0 or year%400==0:
    print(year,"IS LEAP YEAR")
else:
    print(year,"IS NOT LEAP YEAR")