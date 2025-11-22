a = int(input("Enter a number: "))

# for odd a → print a odd numbers
# for even a → print a-1 odd numbers
if a % 2 == 0:
    count = a - 1
else:
    count = a

num = 1

for i in range(count):
    if i == count - 1:
        print(num)
    else:
        print(num, end=", ")
    num += 2