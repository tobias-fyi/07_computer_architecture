"""
Computer Architecture - Day 4
"""

# === Stack frames === #
# Stack grows downward

# 701:
#
# 700: # return point 1     |
# 699: a = 2                |   main()'s stack frame
# 698: b = ??               |
#
# 697: # return point 2     |
# 696: x = 2                |
# 695: y = 7                |   mult2()'s stack frame
# 694: z =14                |
#

# When you call, return address gets pushed ont the stack
# When you return, return addr gets popped off the stack and stored in PC

# def mult2(x, y):
#     z = x * y
#     return z

# def main():
#     a = 2

#     b = mult2(a, 7)

#     # return point 2

#     print(b)  # 14

#     return

# main()

# # return point 2

# print("All done")


# === Recursive example === #

# 701: # return point 1
# 700: n = 4
#
# 699: # return point 2
# 699: n = 3
#
# 697: # return point 2
# 696: n = 2
#
# 695: # return point 2
# 694: n = 1
#
# 693: # return point 2
# 692: n = 0


def count(n):
    if n == 0:
        return

    print(n)

    count(n - 1)

    # return point 2

    return


count(4)

# return point 1

# tail call optimization
