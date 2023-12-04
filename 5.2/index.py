# 5.2.1
st1 = {"a", "b", "c", "d", "e"}
st2 = {"d", "e", "f", "g", "h"}
# Объединение
# result = st1.union(st2)
result = st1 | st2

print(result)  # -> {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}


# 5.2.2
st1 = {"a", "b", "c", "d", "e"}
st2 = {"d", "e", "f", "g", "h"}
# Пересечение
# result = st1.intersection(st2)
result = st1 & st2

print(result)  # -> {'d', 'e'}


# 5.2.3
st1 = {"a", "b", "c", "d", "e"}
st2 = {"d", "e", "f", "g", "h"}
# Разница
# result = st1.difference(st2)
result = st1 - st2

print(result)  # -> {'a', 'b', 'c'}


# 5.2.4
st1 = {"a", "b", "c", "d", "e"}
st2 = {"d", "e", "f", "g", "h"}
# Разница
# result = st2.difference(st1)
result = st2 - st1

print(result)  # -> {'f', 'g', 'h'}


# 5.2.5
st1 = {"a", "b", "c", "d", "e"}
st2 = {"d", "e", "f", "g", "h"}
# Симметричная разница
# result = st1.symmetric_difference(st2)
result = st1 ^ st2

print(result)  # -> {'a', 'b', 'c', 'f', 'g', 'h'}
