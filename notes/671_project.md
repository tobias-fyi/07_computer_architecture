# Project Notes :: 671

* [Task List](#task-list)
* [Objective](#objective)
* [Steps](#steps)

---

> Computer Architecture, Day 1: Get `print8.ls8` running

## Task List

* [x] Inventory what is here
* [ ] Implement the `CPU` constructor
* [ ] Add RAM functions `ram_read()` and `ram_write()`
* [ ] Implement the core of `run()`
* [ ] Implement the `HLT` instruction handler
* [ ] Add the `LDI` instruction
* [ ] Add the `PRN` instruction

Those are the tasks for today in the main README. More specifically, here are some notes from the LS8 README:

## Objective

> Objective: gain a deeper understanding of how a CPU functions at a low level

* 8-bit computer with 8-bit memory addressing
  * 8-bit CPU only has 8 slots available for addresses, computations, and instructions
  * CPU has total of `2^8 = 256` bytes of memory
  * Can only compute values up to 255
* Input file contains binary numeric values that represent:
    * Machine code of the instruction, or the `opcode` (three necessary instructions in this case)
      * `LDI` (load immediate): store a value in a register / set register to value
      * `PRN`: pseudo-instruction that prints the numeric value stored in a register
      * `HLT`: halt the CPU and exit the emulator
    * An argument for the opcode, or `operands`
      * The register to set (mailbox address)
      * The number to set in the register (mail)

## Steps

> Steps for implementation (Day 1)

* Step 0: take inventory of existing code, docs, and specs
  * Make a list of files with one sentence describing the purpose of each
  * Note what has been implemented and what hasn't
  * Read this whole file (ls8.readme)
  * Skim the LS8 spec
* Step 1: Add constructor to `cpu.py`
  * Add list properties to the `CPU` class to hold
    * 256 bytes of memory (8 bits * 256)
    * 8 general-purpose registers
  * Add properties for any internal registers needed
    * `PC` : Program Counter : address of currently executing instruction
    * `IR` : Instruction Register : contains a copy of currently executing instruction
* Step 2: Add RAM methods to access RAM inside the `CPU` object
  * `CPU.ram_read()`  : accepts address, reads and returns the value stored at that address
  * `CPU.ram_write()` : accepts value to write and address at which the value should be written
  * Two internal registers used for memory operations (parameter names for above methods):
    * Memory Address Register (MAR) : contains address to be read from or written to
    * Memory Data Register    (MDR) : contains data that was read or is to be written
* Step 3: Implement the core of `CPU.run()`
  * The workhorse method of the entire processor
  * Reads the memory address stored in register `PC`
  * Store that result in `IR` (Instruction Register)
    * This can be a local variable in `CPU.run()`
  * Some instructions require up to the next 2 bytes of memory after the `PC` to perform the operation(s)
    * Sometimes the byte value is a register number
    * other times it's a constant value (like in `LDI`)
  * Use `CPU.ram_read()` to read bytes at `PC+1` and `PC+2` from RAM into variables in case the instruction needs them:
    * `PC+1`: `operand_a`
    * `PC+2`: `operand_b`
  * The number of bytes needed for an instruction can be derived from the 2 high bits (6-7) of the instruction opcode
    * See the ls8 spec for details
  * Depending on the value of the opcode, perform the actions needed for the instruction per the ls8 spec
    * Could be if/elif "cascade"
    * Or ... ?
  * After running code for any instruction...
    * `PC` needs to be updated to point to the next instruction for the next iteration of the `CPU.run()` loop
* Step 4: Implement the `HLT` (HALT) instruction handler
  * Add the `HLT` instruction definition to `cpu.py` to call it by name instead of by numeric value
  * In the `CPU.run()` switch, exit loop if `HLT` is encountered
    * Regardless of any more lines of code in the loaded program
  * `HLT` is similar to `sys.exit()`
    * Stop whatever is happening, wherever it happens to be happening
* Step 5: Add the `LDI` (load immediate) instruction
  * `LDI` sets a specified register to a specified value
  * See ls8 spec for details and opcode value
* Step 6: Add the `PRN` instruction (print numeric value stored in register)
  * Process is very similar to adding `LDI` but the handler is simpler
  * See ls8 spec for more details
* Step 7: Run the program and profit from the nice big spanking `8` that is printed to the console!
