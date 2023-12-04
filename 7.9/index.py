# 7.9.1
num = 1

while num <= 10:
    print(num)
    num += 1


# 7.9.2
num = 100

while num >= 1:
    print(num)
    num -= 1


# 7.9.3
num = 1

while num <= 10:
    if num % 2 == 1:
        print(num)

    num += 1


# 7.9.4
num = 100
counter = 0

while True:
    if num < 10:
        break

    num /= 2
    counter += 1

print(counter)  # -> 4
print(num)  # -> 6.25


# 7.9.5
num = 10
divisors = []
possible_divisor = 1

while possible_divisor <= num:
    if num % possible_divisor == 0:
        divisors.append(possible_divisor)

    possible_divisor += 1

print(divisors)  # -> [1, 2, 5, 10]
