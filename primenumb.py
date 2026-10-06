n = int(input("Enter a number: "))
count = 0
sum = 0

for i in range(2, n + 1):

    counting = 0

    for j in range(1, i + 1):
        if i % j == 0:
            counting = counting + 1

    if counting == 2:
        print(i, end=" ")
        count = count + 1
        sum = sum + i

print()
print("Total prime numbers:", count)
print("Sum of prime numbers:", sum)