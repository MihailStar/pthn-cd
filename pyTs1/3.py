# pyTs1.3.1
string = "123456"

if len(string) > 1:
    print(string[-2])  # -> '5'


# pyTs1.3.2
number_a = 123456
number_b = 61728

print(number_a % number_b == 0)  # -> True


# pyTs1.3.3
string = "abcde"

print(list(string))  # -> ['a', 'b', 'c', 'd', 'e']


# pyTs1.3.4
lst = [1, 2, 3, 4, 5, 6]

print(lst[2:-1])  # -> [3, 4, 5]


# pyTs1.3.5
date = {
    "year": "2025",
    "month": "12",
    "day": "31",
}

# print('-'.join(date.values()))
# print(f"{date["year"]}-{date["month"]}-{date["day"]}")
print("{}-{}-{}".format(date["year"], date["month"], date["day"]))  # -> '2025-12-31'
