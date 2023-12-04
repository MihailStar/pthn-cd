from functools import reduce

# pyTs2.3.1
string_a = "abcdef"
string_b = "fedcba"

print(string_a[-1] == string_b[0])  # -> True


# pyTs2.3.2
string = "0102030"

index_zero = -1
counter_zero = 1

while counter_zero <= 3:
    index_zero = string.find("0", index_zero + 1)

    if index_zero == -1:
        print(index_zero)
        break

    counter_zero += 1
else:
    print(index_zero)  # -> 4


# pyTs2.3.3
string = "12,34,56"

print(reduce(lambda acc, digits: acc + int(digits), string.split(","), 0))  # -> 102


# pyTs2.3.4
date = "2025-12-31"
y, m, d = date.split("-")
split_date = dict(year=y, month=m, day=d)

print(split_date)  # -> {'year': '2025', 'month': '12', 'day': '31'}


# pyTs2.3.5
dct = {"a": 1, "b": 2, "c": 3, "d": 4}

print(set(dct.values()))  # -> {1, 2, 3, 4}
