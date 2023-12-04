# 9.2.1
print(" abcde ".strip())  # -> 'abcde'


# 9.2.2
print(" abcde ".lstrip())  # -> 'abcde '


# 9.2.3
print(" abcde ".rstrip())  # -> ' abcde'


# 9.2.4
txt = ""
num = 6

# print(txt.ljust(6, "0"))
# print(txt.rjust(6, "0"))
print(txt.zfill(6))
