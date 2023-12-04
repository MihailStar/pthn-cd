from functools import reduce


# pyTs3.9.1
def get_number_of_zeros(num):
    return reduce(
        lambda counter, digit: counter + 1 if digit == "0" else counter, str(num), 0
    )


nums = [10, 100, 1000, 10_000, 1000, 100, 10]
nums = list(
    filter(
        lambda num: get_number_of_zeros(num) <= 2,
        nums,
    )
)

print(nums)  # -> [10, 100, 100, 10]


# pyTs3.9.2
def get_sum_of_digits(num):
    return reduce(lambda accumulator, digit: accumulator + int(digit), str(num), 0)


result = [num for num in range(1, 1001) if get_sum_of_digits(num) == 13]

print(set(result))


# pyTs3.9.3
nums = [1, 2, 3]
temp = []

for num in nums:
    for _ in range(2):
        temp.append(num)


nums = temp

print(nums)  # -> [1, 1, 2, 2, 3, 3]


# pyTs3.9.4
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

if len(lst1) != len(lst2):
    raise Exception()

for index, _ in enumerate(lst1):
    print(f"{lst1[index]},{lst2[index]}")  # -> '1,4\n2,5\n3,6'
