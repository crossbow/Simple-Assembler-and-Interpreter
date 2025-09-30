# Extended Python interpreter for the assembly language in sample.dat.txt
# GENERATO da COPILOT!!!

# Define opcodes
opcodes = {
    "const": 0,
    "get": 1,
    "put": 2,
    "ld": 3,
    "st": 4,
    "add": 5,
    "sub": 6,
    "jpos": 7,
    "jz": 8,
    "j": 9,
    "halt": 10
}

# Read the assembly source file
with open("sample.dat", "r") as f:
    lines = f.readlines()

# First pass: build symbol table and intermediate instructions
symbol_table = {}
instructions = []
nextmem = 0

for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    line = line.split("#")[0].strip()
    tokens = line.split()
    if len(tokens) == 0:
        continue
    if tokens[0] in opcodes:
        label = None
        op = tokens[0]
        addr = tokens[1] if len(tokens) > 1 else None
    else:
        label = tokens[0]
        op = tokens[1] if len(tokens) > 1 else None
        addr = tokens[2] if len(tokens) > 2 else None
        symbol_table[label] = nextmem
    instructions.append((op, addr))
    nextmem += 1

# Second pass: generate memory
memory = [0] * 1000
for i, (op, addr) in enumerate(instructions):
    if op == "const":
        if addr is None:
            memory[i] = 0
        else:
            memory[i] = int(addr)
    else:
        opcode = opcodes[op]
        if addr is None:
            address = 0
        elif addr.isdigit():
            address = int(addr)
        else:
            address = symbol_table.get(addr, 0)
        memory[i] = 1000 * opcode + address

# Simulated input values
input_values = [5, 7, 0]
input_pointer = 0

# Interpreter
pc = 0
acc = 0
output_values = []

def print_state():
    print(f"PC={pc}, ACC={acc}")
    print("Memory (non-zero cells):")
    for i, val in enumerate(memory):
        if val != 0:
            print(f"  [{i}] = {val}")
    print("-" * 40)

while pc >= 0:
    instr = memory[pc]
    addr = instr % 1000
    code = instr // 1000
    pc += 1

    if code == opcodes["get"]:
        if input_pointer < len(input_values):
            acc = input_values[input_pointer]
            input_pointer += 1
        else:
            acc = 0
    elif code == opcodes["put"]:
        print(acc)
        output_values.append(acc)
    elif code == opcodes["st"]:
        memory[addr] = acc
    elif code == opcodes["ld"]:
        acc = memory[addr]
    elif code == opcodes["add"]:
        acc += memory[addr]
    elif code == opcodes["sub"]:
        acc -= memory[addr]
    elif code == opcodes["jpos"]:
        if acc > 0:
            pc = addr
    elif code == opcodes["jz"]:
        if acc == 0:
            pc = addr
    elif code == opcodes["j"]:
        pc = addr
    elif code == opcodes["halt"]:
        pc = -1
    else:
        pc = -1

    print_state()

# Save output to file
with open("asm_output.txt", "w") as f:
    for val in output_values:
        f.write(str(val) + "\n")