"""
Computer Architecture — Day 2 :: Bitwise
"""

# === Bitwise AND === #
1 & 1
# >>> 1

f"{164:b}"
# >>> '10100100'

"""
# From print8.ls8

10000010  # LDI R0,8
00000000
00001000
01000111  # PRN R0
00000000
00000001  # HLT
"""


import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # 256 bytes (8 bits = 1 byte) of RAM
        self.ram = [0] * 256

        # === Internal registers === #
        # 8 general-purpose registers
        self.reg = [0] * 8
        # PC: address (index) of currently executing instruction
        self.pc = 0

        # Attribute to control runtime
        self.running = False

    def load(self, program_filepath: str) -> None:
        """Load a program into memory from file.
        
        : param program_filepath (str) : Path to program file.
        """
        address = 0  # Address (index) of current instruction

        # === Load instructions from file === #
        with open(program_filepath, "r") as f:
            program = f.read().splitlines()

        # === Parse each line: string -> bits === #
        for inst in program:
            # === Remove anything after octothorpe === #
            if inst.startswith("#") or inst.strip() == "":
                continue  # If line comment or empty line
            elif inst.rfind("#") > 0:  # If comment on same line as inst
                cut_index = inst.rfind("#")  # Get index of octothorpe
                inst = inst[:cut_index]  # Slice from index to end
            inst = int(inst, 2)  # Convert to bit
            self.ram[address] = inst  # Assign value to memory address
            address += 1  # Move to next memory slot

    def ram_read(self, address) -> int:
        """Returns the value (MDR) stored at a memory address (MAR)."""
        return self.ram[address]

    def ram_write(self, value, address) -> None:
        """Writes a value (MDR) to a memory address (MAR)."""
        self.ram[address] = value

    def ldi(self):
        """LDI: Load instruction handler."""
        # Read bytes at ram[self.pc + 1]
        operand_a = self.ram_read(self.pc + 1)
        # And ram[self.pc + 2]
        operand_b = self.ram_read(self.pc + 2)
        self.reg[operand_a] = operand_b
        self.pc += 3

    def prn(self):
        """PRN: Print instruction handler."""
        operand = self.ram_read(self.pc + 1)
        print(self.reg[operand])
        self.pc += 2

    def hlt(self):
        """HLT: Halt instruction handler."""
        self.running = False

    def run(self):
        """Run the CPU."""
        self.running = True
        while self.running:
            # Read memory address stored in register PC
            # Store result in Instruction Register
            ir = self.ram_read(self.pc)

            # Get instruction length (pc increment amt)
            inst_len = ((ir & 0b11000000) >> 6) + 1

            # Execute the current instruction
            if ir == 0b10000010:  # LDI: Load immediate
                self.ldi()
            elif ir == 0b01000111:  # PRN: Print operand
                self.prn()
            elif ir == 0b00000001:  # HLT: Halt
                self.hlt()
            else:  # Catch invalid / other instruction
                print("Unrecognized instruction")
                self.running = False

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """Handy function to print out the CPU state.
        
        You might want to call this from `run()` if you
        need help debugging.
        """

        print(
            f"TRACE: %02X | %02X %02X %02X |"
            % (
                self.pc,
                # self.fl,
                # self.ie,
                self.ram_read(self.pc),
                self.ram_read(self.pc + 1),
                self.ram_read(self.pc + 2),
            ),
            end="",
        )

        for i in range(8):
            print(" %02X" % self.reg[i], end="")

        print()
