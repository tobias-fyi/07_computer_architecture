"""
671 :: Whiteboard

Given a dictionary with keys that can be both strings and integers,
sum up only the items that have integer values.
"""

dict1 = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish",
}

result = 0
for key, value in dict1.items():
    if isinstance(value, int):
        result += value

print(result)
