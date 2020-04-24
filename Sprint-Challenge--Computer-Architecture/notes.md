# Sprint Challenge - Computer Architecture

* [MVP](#mvp)
* [CMP](#cmp)
  * [Flags](#flags)
* [Number base practice](#number-base-practice)
  * [Binary to Decimal](#binary-to-decimal)
  * [Decimal to Binary](#decimal-to-binary)
  * [Hex to Decimal](#hex-to-decimal)
  * [Decimal to Hex](#decimal-to-hex)
* [Interview](#interview)

## MVP

> Sprint-Challenge.../README.md

Your finished project must include all of the following requirements:

* [ ] Add the `CMP` instruction and `equal` flag to your LS-8.
* [ ] Add the `JMP` instruction.
* [ ] Add the `JEQ` and `JNE` instructions.

## CMP

*This is an instruction handled by the ALU.*

`CMP registerA registerB`

Compare the values in two registers.

* If they are equal, set the Equal `E` flag to 1, otherwise set it to 0.
* If registerA is less than registerB, set the Less-than `L` flag to 1, otherwise set it to 0.
* If registerA is greater than registerB, set the Greater-than `G` flag to 1, otherwise set it to 0.

Machine code:

```txt
10100111 00000aaa 00000bbb
A7 0a 0b
```

### Flags

The flags register `FL` holds the current flags status. These flags
can change based on the operands given to the `CMP` opcode.

The register is made up of 8 bits. If a particular bit is set, that flag is "true".

`FL` bits: `00000LGE`

* `L` Less-than: during a `CMP`, set to 1 if registerA is less than registerB, zero otherwise.
* `G` Greater-than: during a `CMP`, set to 1 if registerA is greater than registerB, zero otherwise.
* `E` Equal: during a `CMP`, set to 1 if registerA is equal to registerB, zero otherwise.

## Number base practice

### Binary to Decimal

    00101101
    1 + 4 + 8 + 32 = 45

    11000000
    64 + 128 = 192

    10101100
    4 + 8 + 32 + 128 = 172

    01110111
    1 + 2 + 4 + 16 + 32 + 64 = 119

### Decimal to Binary

    7   = 0b00000111
    51  = 0b00110011
    72  = 0b01001000
    122 = 0b01111010
    56  = 0b00111000
    102 = 0b01100110
    142 = 0b10001110

### Hex to Decimal

    0E
    14 + 0 = 14

    A9
    9 + 10*16 = 169

    7B
    11 + 7*16 = 123

    DD
    13 + 13*16 = 13 + 208 = 221

    98
    8 + 9*16 = 152

### Decimal to Hex

    16  = 0x10
    58  = 0x3A
    88  = 0x58
    98  = 0x62
    147 = 0x93
    222 = 0xDE
    118 = 0x76
    185 = 0xB9

## Interview

1. What is the ALU in a CPU, and what does it do?

Arithmetic Logic Unit. It performs mathematical operations / instructions.

2. Why is a stack useful in a CPU?

To store values and addresses that are used in instructions. Particularly useful for running subroutines because it can hold the address of the return point, as well as values to be operated on during any instruction.

3. Convert 1101 0011 to hexidecimal

    1101 0011
      D   3
    -> D3
