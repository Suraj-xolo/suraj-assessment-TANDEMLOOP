numbers = [1,2,8,9,12,46,76,82,15,20,30]

find_value = {}

for i in range(1, 10):   # from 1 to 9
    count = 0
    for n in numbers:
        if n % i == 0:
            count += 1
    find_value[i] = count

print(find_value)