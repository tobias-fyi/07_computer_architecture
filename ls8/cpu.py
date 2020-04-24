"""Computer Architecture :: CPU emulator class"""

import os
import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # 256 bytes (8 bits = 1 byte) of RAM
        self.ram = [0b00000000] * 256

        # === Internal registers === #
        self.reg = [0b00000000] * 0b00001000  # 8 general-purpose registers
        self.sp = 0b00000111  # R7 is reserved as the Stack Pointer (SP)
        self.reg[self.sp] = 0xF4  # Stack starts at memory address F4
        # PC: address (index) of currently executing instruction
        self.pc = 0b00000000
        # FL: flags - used in CMP opcode
        self.fl = 0b00000000

        # Attribute to control runtime
        self.running = False

        # === Opcodes and operands === #
        # Attribute to share operands across methods
        self.operands = []
        # Dictionary to look up opcodes / instructions
        self.opcodes = {
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b00000001: self.hlt,
            0b01000101: self.push,
            0b01000110: self.pop,
            0b01010000: self.call,
            0b00010001: self.ret,
            0b01010100: self.jmp,
            0b01010101: self.jeq,
            0b01010110: self.jne,
        }

    def load(self, program_filepath: str) -> None:
        """Load a program into memory from file.
        
        : param program_filepath (str) : Path to program file.
        """
        address = 0  # Address (index) of current instruction

        try:  # Load instructions from file
            with open(program_filepath, "r") as f:
                program = f.read().splitlines()
        except FileNotFoundError:
            print(f"File '{program_filepath}' failed to load.")

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
            address += 0b00000001  # Move to next memory slot

    def ram_read(self, address) -> int:
        """Returns the value (MDR) stored at a memory address (MAR)."""
        return self.ram[address]

    def ram_write(self, value, address) -> None:
        """Writes a value (MDR) to a memory address (MAR)."""
        self.ram[address] = value

    def ldi(self):
        """LDI: Instruction loader handler"""
        reg_a, reg_b = self.operands  # Extract operands from array
        self.reg[reg_a] = reg_b

    def prn(self):
        """PRN: Print instruction handler."""
        print(self.reg[self.operands[0]])

    def hlt(self):
        """HLT: Halt instruction handler."""
        self.running = False

    def push(self):
        """PUSH: Push the value in the 
        given register onto the stack.
        """
        # Decrement stack pointer
        self.reg[self.sp] -= 0b00000001
        # Copy value to be pushed to stack from reg to ram
        value = self.reg[self.operands[0]]
        address = self.reg[self.sp]  # Get address from R7
        # Assign value to (memory address of) top of stack
        self.ram[address] = value

    def pop(self):
        """POP: Pop the value at the top of
        the stack into the given register.
        """
        address = self.reg[self.sp]  # Get address from SP / R7
        # Copy value from memory at address
        value = self.ram[address]
        # Assign value to the given register
        self.reg[self.operands[0]] = value
        # Increment the stack pointer
        self.reg[self.sp] += 0b00000001

    def call(self):
        """CALL: Calls a subroutine (function) at the
        address stored in the register."""
        # Get return address (PC + 2)
        self.reg[self.sp] -= 0b00000001  # Decrement stack pointer
        # Push return address -> stack
        self.ram[self.reg[self.sp]] = self.pc + 0b00000010

        # Set PC to value in given register (dest address)
        dest_addr = self.reg[self.operands[0]]
        self.pc = dest_addr

    def ret(self):
        """RET: Return from subroutine to main scope."""
        # Pop return address from stack
        return_addr = self.ram[self.reg[self.sp]]
        self.reg[self.sp] += 0b00000001  # Increment stack pointer
        # Set PC to return address
        self.pc = return_addr

    def jmp(self):
        """JMP: Jump to the address stored in the given register."""
        # Set PC to address stored in register
        self.pc = self.reg[self.operands[0]]
        # self.pc = self.operands[0]

    def jeq(self):
        """If `equal` flag is set (true), jump to
        the address stored in the given register."""
        if self.fl == 1:
            self.jmp()
        else:
            self.pc += 2

    def jne(self):
        """If `E` flag is clear (false, 0), jump to
        the address stored in the given register."""
        if self.fl == 0:
            self.jmp()
        else:
            self.pc += 2

    def run(self):
        """Run the CPU."""
        self.running = True
        while self.running:
            # Read memory address stored in register PC
            # Store result in Instruction Register
            ir = self.ram_read(self.pc)

            # Get instruction length (pc increment amt)
            inst_len = ((ir & 0b11000000) >> 6) + 1
            alu_op = (ir & 0b00100000) >> 5
            sets_pc = (ir & 0b00010000) >> 4
            inst_id = ir & 0b00001111

            # Assign operands according to inst_len
            self.operands = []  # Reset operands
            for i in range(1, inst_len):
                self.operands.append(self.ram_read(self.pc + i))

            # Look up / execute the current instruction
            if ir in self.opcodes:
                self.opcodes[ir]()
            elif alu_op == 1:  # ALU instructions
                self.alu(ir)
            else:  # Catch invalid / other instruction
                print("Unrecognized instruction")
                self.running = False

            # If instruction does not set PC, increment by length
            if sets_pc == 0:
                self.pc += inst_len

    def alu(self, op) -> None:
        """ALU operations."""
        reg_a, reg_b = self.operands  # Extract operands from array

        if op == 0b10100000:  # ADD
            self.reg[reg_a] += self.reg[reg_b]
        elif op == 0b10101000:  # AND
            # Bitwise-AND then store result at reg_a
            self.reg[reg_a] &= self.reg[reg_b]
        elif op == 0b10100111:  # CMP
            # Set self.fl to 1 if equal, 0 if not
            if self.reg[reg_a] == self.reg[reg_b]:
                self.fl = 0b00000001
            else:
                self.fl = 0b00000000
        elif op == 0b10100100:  # MOD
            # Get modulo of values at the two regs
            mod = self.reg[reg_a] % self.reg[reg_b]
            if mod > 0:
                # If there is any remainder, store at reg_a
                self.reg[reg_a] = mod
            else:  # Otherwise, print error and HLT
                print("Modulo result is 0. Quitting...")
                self.hlt()
        elif op == 0b10100010:  # MUL
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == 0b01101001:  # NOT
            self.reg[reg_a] = ~self.reg[reg_a]
        elif op == 0b10101010:  # OR
            # Bitwise-OR then store result at reg_a
            self.reg[reg_a] |= self.reg[reg_b]
        elif op == 0b10101100:  # SHL
            # Shift val at reg_a left by val of reg_b
            self.reg[reg_a] << self.reg[reg_b]
        elif op == 0b10101101:  # SHR
            # Shift val at reg_a left by val of reg_b
            self.reg[reg_a] >> self.reg[reg_b]
        elif op == 0b10101011:  # XOR
            # Bitwise-XOR, store result at reg_a
            self.reg[reg_a] ^= self.reg[reg_b]
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


if __name__ == "__main__":
    # === Debugging setup === #
    to_repo = "/Users/Tobias/workshop/buildbox/lambda_cs"
    to_dir = "07_computer_architecture/ls8/examples/"
    to_file = "sctest.ls8"
    filepath = os.path.join(to_repo, to_dir, to_file)

    cpu = CPU()
    cpu.load(filepath)
    cpu.run()
