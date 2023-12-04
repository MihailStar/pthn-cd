# pyTs3.7.1
string = "случайная строка"
string = " ".join([word[:-1] + word[-1].upper() for word in string.split(" ")])

print(string)  # -> 'случайнаЯ строкА'


# pyTs3.7.2
string = "2468"

print(all([int(char) % 2 == 0 for char in string]))  # -> True


# pyTs3.7.3
txt1 = "12345"
txt2 = "45678"

print("".join([char for char in txt1 if char in txt2]))  # -> '45'


# pyTs3.7.4
string = "a bc def ghij"

print(
    " ".join([word.upper() if len(word) <= 3 else word for word in string.split(" ")])
)  # -> 'A BC DEF ghij'
