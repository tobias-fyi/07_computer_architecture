# The System Stack

> Computer Architecture — Day 3

## Stack Pointer

    R0: 12
    R1: 23
    R2: 23

    R7: F3 (this is the SP)

    PUSH R0
    PUSH R1
    POP  R2
    PUSH R1 <<<
    POP  R1
    POP  R2
    POP  R1 <- Pop on an empty stack

> Memory map

    FF: 00
    FE: 00
    FD: 00
    FC: 00
    FB: 00
    FA: 00
    F9: 00
    F8: 00
    F7: 00
    F6: 00
    F5: 00
    F4: 00
    F3: 12
    F2: 23 <-- SP
    F1: 00
    .
    .
    .
    05: 00
    04: 00
    03: XX
    02: XX
    01: XX
    00: XX

### Steps

> Look at LS-8 spec for details

After first iteration

* PUSH (R1)
  * Decrement SP (F3 -> F2)
  * Copy value from reg (R1: 23) into memory at SP (F2)
  * Note:
    * LDI something into a register before pushing to stack
* POP (R2)
  * Copy value from memory at SP (F2) into reg (R2)
  * Increment SP (F2 -> F3)

## Edge Cases

### Popped off

When the SP is at FF and is popped (off the top), it will wrap around to "bottom".

That is basically what this syntax does - chops off the extra bits to make it wrap:

```py
(r1 + r2) & 0xff
```

### Pushed past program

    F5: 00
    F4: 00
    F3: 01
    F2: 01
    F1: 01
    .
    .
    .
    05: 01
    04: 01
    03: 01 <-- SP <-- PC
    02: XX
    01: XX
    00: XX

In this case, don't have to put extra code in to protect against the SP and PC colliding.

## Beej machine
