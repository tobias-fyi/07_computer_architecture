# 671 :: Computer Architecture 1

* [Number Bases](#number-bases)
  * [Decimal (Base 10)](#decimal-base-10)
  * [Binary (Base 2)](#binary-base-2)
* [Conversions](#conversions)
  * [Binary to Decimal](#binary-to-decimal)
  * [Binary to Hex](#binary-to-hex)

## Number Bases

12 apples
oxC apples
0b1100 apples

> What are the bases?

* Decimal: base 10
* Binary:  base 2
* Hex:     base 16
* Octal:   base 8

### Decimal (Base 10)

1234

* 1 -> 1000
* 2 -> 100
* 3 -> 10
* 4 -> 1

### Binary (Base 2)

    +----8s place
    |+---4s place
    ||+--2s place
    |||+-1s place
    ||||
    1101 -> 8 + 4 + 0 + 1 = 13

## Conversions

### Binary to Decimal

* 1 in the 8s place
* 1 in the 4s place
* 0 in the 2s place
* 1 in the 1s place

### Binary to Hex

* 4 binary digits (bits) == 1 hex digit
* Byte is 8 bits

    11010011

    1101 0011
      d    3

    13 = d

    0b11010011 == 0xd3

Max number for 8 bits: 0b11111111
