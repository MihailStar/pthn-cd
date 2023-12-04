# 7.10.1
lst = [1, 0, -1]
is_lst_positive = True

for num in lst:
    if num < 0:
        is_lst_positive = False
        break

print(is_lst_positive)  # -> False


# 7.10.2
num = 11

for divisor in range(2, num):
    if num % divisor == 0:
        print("not a prime number")
        break
else:
    print("prime number")  # -> 'prime number'
