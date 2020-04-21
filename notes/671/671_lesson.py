"""
Computer Architecture — Day 1 :: Bases and Basics

Python program that runs programs
"""

# PRINT_TOBY = 1
# HALT = 2

# memory = [
#     PRINT_TOBY,
#     PRINT_TOBY,
#     PRINT_TOBY,
#     PRINT_TOBY,
#     PRINT_TOBY,
#     HALT,
# ]

# for v in memory:
#     if v == PRINT_TOBY:
#         print("Toby")
#     elif v == HALT:
#         break

# For loop is not flexible enough

# # === Program counter === #
# # Address (index) of current instruction
# pc = 0
# running = True

# while running:
#     inst = memory[pc]

#     if inst == PRINT_TOBY:
#         print("Toby")
#         pc += 1

#     elif inst == HALT:
#         running = False


# === Register === #

PRINT_TOBY = 1
HALT = 2
SAVE_REG = 3  # Store a value in register (in LS8 it's called LDI)
PRINT_REG = 4  # Corresponds to print in the LS8

memory = [
    PRINT_TOBY,
    SAVE_REG,  # SAVE R0,37 store 37 in R0 - the opcode
    0,  # R0   operand ("argument")
    37,  # 37   operand
    PRINT_TOBY,
    PRINT_REG,  # PRINT_REG R0
    0,  # R0
    HALT,
]

# Store values in the register
register = [0] * 8  # Like variables R0-R7

# Address (index) of current instruction
pc = 0
running = True

while running:
    inst = memory[pc]

    if inst == PRINT_TOBY:
        print("Toby")
        pc += 1

    elif inst == SAVE_REG:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        pc += 3  # 3-bit instruction

    elif inst == PRINT_REG:
        reg_num = memory[pc + 1]
        # Register num is one thing, address is another
        value = register[reg_num]
        print(value)
        pc += 2  # 2-bit instruction

    elif inst == HALT:
        running = False

    else:
        print("Invalid instruction")
        running = False
