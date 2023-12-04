import random

# 8.2.1
num1 = 10
num2 = 20
result = random.randint(num1, num2)

print(result)


# 8.2.2
num1 = 10
num2 = 20
result = random.uniform(num1, num2)

print(result)


# 8.2.3
lst = [1, 2, 3, 4, 5]
result = random.choice(lst)

print(result)


# 8.2.4
lst = [1, 2, 3, 4, 5]
result = random.sample(lst, 3)

print(result)


# 8.2.5
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)

print(lst)


# 8.2.6
lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# result = random.sample(lst, 3, counts=[1, 0, 0, 1, 0, 1, 0, 1, 1])
result = random.sample(list(set(lst)), 3)

print(result)
