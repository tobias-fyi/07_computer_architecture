# Bitwise Operations

> Computer Architecture — Day 2

* [Boolean](#boolean)
* [Bitwise AND](#bitwise-and)
* [Bitwise Operators](#bitwise-operators)
* [Shift Operators](#shift-operators)
* [Instruction Layout](#instruction-layout)
  * [LDI](#ldi)
* [ALU: Arithmetic Logic Unit](#alu-arithmetic-logic-unit)

---

## Boolean

    and or    True False
    &&  ||    (javascript)

## Bitwise AND

    A   B   A BITWISE-AND B
    ========================
    0   0           0
    0   1           0
    1   0           0
    1   1           1

## Bitwise Operators

* and: &
* or : |
* not: ~
* xor: ^

        10100100
      & 10110111
      ============
        10100100

    In [2]: 0b10100100 & 0b10110111
    Out[2]: 164

Numbers only have a base when they are written down. Otherwise they just exist...

Also, Beej showed how to format binary numbers:

    In [1]: f"{164:b}"
    Out[1]: '10100100'

Very interesting how this works:

    In [3]: 0b11101001 & 0b00101100
    Out[3]: 40

    In [4]: 0b11101001
    Out[4]: 233

    In [5]: 0b00101100
    Out[5]: 44

Bitwise AND can be used as a filter. This is the use-case that we've seen in DS. I'm trying to remember exactly when we used it — I believe it was in Unit 4, deep learning.

        vvvv
        10100100
      & 11110000    # "AND mask"
      ============
        10100000

The "AND mask" can be used to extract any of the bits of a number.

## Shift Operators

* shift right: >>
* shift left : <<

      bits of interest
          vv
        10100100
      & 00110000
      ============
        00100000
        00010000
        00001000
        00000100
        00000010
        
        00000010  # Goal

```py
(0b10100100 & 0b00110000) >> 4
# >>> 2
```

> Same thing in base 10 / decimal

      vv
    123456
    009900
    ======
    003400
    000340
    000034 <<

## Instruction Layout

Meanings of the bits in the first byte of each instruction: `AABCDDDD`

* `AA` Number of operands for this opcode, 0-2
* `B` 1 if this is an ALU operation
* `C` 1 if this instruction sets the PC
* `DDDD` Instruction identifier

### LDI

`LDI register immediate`

Set the value of a register to an integer.

Machine code:

```txt
10000010 00000rrr iiiiiiii
              ^^^
  placeholder for register number
```

In the analogy of the mailboxes, the general-purpose registers are just another row of mailboxes.

## ALU: Arithmetic Logic Unit

[ALU: Arithmetic Logic Unit](https://en.wikipedia.org/wiki/Arithmetic_logic_unit)

That is where math is calculated.
