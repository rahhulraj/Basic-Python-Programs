inputstring = input("ENTER THE WORD :")
newstring = ""
for i in range(len(inputstring)):
    found = 0

    for j in range(i):
        if inputstring[i] == inputstring[j]:
            found = 1

    if found == 0:
        newstring = newstring + inputstring[i]

print(newstring)