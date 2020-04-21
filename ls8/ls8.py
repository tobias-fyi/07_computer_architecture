"""Computer Architecture :: Main LS-8 runtime script"""

import sys
from cpu import *

# Extract file to use from command line
try:
    program_filepath = sys.argv[1]
except IndexError:
    print("Please input valid filepath.")
    sys.exit()

# Instantiate CPU instance
cpu = CPU()

# Load the program into memory and run the CPU
cpu.load(program_filepath)
cpu.run()
