import re as regexp

# pyTs3.8.1
nums = [993, 939, 399]

print(all(["3" in str(num) for num in nums]))  # -> True


# pyTs3.8.2
string = "399,993,939"

print(max(string.split(",")))  # -> '993'


# pyTs3.8.3
string = "some-formatted-string"

print(string.replace("-", "_"))  # -> 'some_formatted_string'


# pyTs3.8.4
string = "some_formatted_string"

print(
    regexp.sub(r"_([a-z])", lambda match: match.group(1).upper(), string)
)  # -> 'someFormattedString'


# pyTs3.8.5
string = "someFormattedString"

print(
    regexp.sub(r"([A-Z])", lambda match: f"_{match.group(1).lower()}", string)
)  # -> 'some_formatted_string'
