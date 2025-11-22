a = int(input())

num = 1

for i in range(a):
    print(num, end="")
    num += 2

    # print comma only if it's NOT the last number
    if i != a - 1:
        print(", ", end="")