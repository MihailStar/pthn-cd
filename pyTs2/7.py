# pyTs2.7.1
symbol = "_"

if symbol.islower():
    print("lowercase")
elif symbol.isupper():
    print("uppercase")
else:
    print("nocase")  # -> 'nocase'


# pyTs2.7.2
number = 123789

print(int("".join(filter(lambda digit: int(digit) % 2 == 0, str(number)))))  # -> 28


# pyTs2.7.3
date = ("2025", "12", "31")
y, m, d = date

print(dict(year=y, month=m, day=d))  # -> {'year': '2025', 'month': '12', 'day': '31'}
