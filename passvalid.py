password = input("ENTER THE PASSWORD HERE :")
uppercase = 0
lowercase = 0
digit = 0
for ch in password:
    if ch.isalpha():
        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1
    elif ch.isdigit():
        digit = digit + 1
if len(password) >= 8 and uppercase > 0 and lowercase > 0 and digit > 0:
    print("Valid password")
else:
    print("Invalid password")