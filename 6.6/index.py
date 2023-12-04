# 6.6.1
num = 45

if 10 <= num <= 99:
    digits = str(num)
    sum_of_digits = int(digits[0]) + int(digits[1])

    if sum_of_digits <= 9:
        print("сумма цифр однозначна")  # -> 'сумма цифр однозначна'
    else:
        print("сумма цифр двухзначна")
