# 5.1.1
st = {1, 2, 3}
st.add(3)
st.add(4)

print(st)  # -> {1, 2, 3, 4}


# 5.1.2
st = {1, 2, 3}
lst = [3, 4, 5, 6]
st.update(lst)

print(st)  # -> {1, 2, 3, 4, 5, 6}


# 5.1.3
st = {1, 2, 3, 4, 5}
st.remove(3)

print(st)  # -> {1, 2, 4, 5}


# 5.1.4
st = {1, 2, 3, 4, 5}
st.clear()

print(st)  # -> set()


# 5.1.5
st = set()
st.add("1")
st.update("2")
st.update(["3"])

print(st)  # -> {'1', '2', '3'}


# 5.1.6
st = {1, 2, 3, 4, 5}
length = len(st)

print(length)  # -> 5
