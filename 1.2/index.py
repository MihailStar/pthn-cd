# 1.2.1
txt1 = "abc"
txt2 = "def"
result = txt1 + txt2

print(result)  # -> 'abcdef'


# 1.2.2
txt = "abcdef"
result = len(txt)

print(result)  # -> 6


# 1.2.3
txt = "abcdef"
result = txt[0]

print(result)  # -> 'a'


# 1.2.4
txt = "abcdef"
result = txt[1]

print(result)  # -> 'b'


# 1.2.5
txt = "abcdef"
# result = txt[len(txt) - 1]
result = txt[-1]

print(result)  # -> 'f'


# 1.2.6
txt = "abcdef"
result = txt[-2]

print(result)  # -> 'e'


# 1.2.7
txt = ""
txt = "Имя\nФамилия\nОтчество"
txt = """Имя
Фамилия
Отчество"""

print(txt)  # -> 'Имя\nФамилия\nОтчество'
