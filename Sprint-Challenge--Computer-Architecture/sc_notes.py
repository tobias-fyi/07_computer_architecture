"""
Computer Architecture :: Sprint Challenge
"""

import random

for i in range(16):
    print(random.randint(1, 256))


a = 0x0A
b = 0xBB


def add(a, b):
    print("add")
    return a + b


def sub(a, b):
    print("sub")
    return a - b


def mult(a, b):
    print("mult")
    return a * b


def div(a, b):
    print("div")
    return a / b


dict_exp = {
    0b00000001: add(a, b),
    0b00000010: sub(a, b),
    0b00000011: mult(a, b),
    0b00000100: div(a, b),
}

list_exp = [
    add(a, b),
    sub(a, b),
    mult(a, b),
    div(a, b),
]

# === Bitwise-AND === #
val_a = 0b00010100
val_b = 0b00100111

# Bitwise AND assignment
val_a &= val_b
# >>> 0b00010100
# >>> 0b00100111
# >>> 0b00000100 -> 4
