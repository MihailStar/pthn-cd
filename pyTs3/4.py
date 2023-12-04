# pyTs3.4.1
VOWELS = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я", "ё"]

# print("".join(([char for char in string if char.lower() not in VOWELS])))

string = "случайная строка"
temp = ""

for char in string:
    if char.lower() not in VOWELS:
        temp += char

string = temp

print(string)  # -> 'слчйн стрк'


# pyTs3.4.2
st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

# print(st1.intersection(st2))
print(st1 & st2)  # -> {4, 5}


# pyTs3.4.3
st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

# print(st1.symmetric_difference(st2))
print(st1 ^ st2)  # -> {1, 2, 3, 6, 7, 8}
