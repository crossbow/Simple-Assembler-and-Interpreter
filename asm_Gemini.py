import sys

# La classe che incapsula l'intera logica dell'assembler e dell'interprete.
class AssemblerInterpreter:
    def __init__(self):
        self.opcodes = {
            "const": 0, "get": 1, "put": 2, "ld": 3, "st": 4, "add": 5,
            "sub": 6, "jpos": 7, "jz": 8, "j": 9, "halt": 10
        }
        self.reverse_opcodes = {v: k for k, v in self.opcodes.items()}
        self.symbol_table = {}
        self.memory = [0] * 1000
        self.instructions = []
        self.acc = 0
        self.pc = 0

    def assemble(self, filename):
        # Passaggio 1: Costruisci la tabella dei simboli e la lista delle istruzioni intermedie.
        nextmem = 0
        with open(filename, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.split("#")[0].strip()
            if not line:
                continue
            
            parts = line.split()
            label = None
            op = None
            addr = None

            if parts[0] in self.opcodes:
                op = parts[0]
                addr = parts[1] if len(parts) > 1 else None
            else:
                label = parts[0]
                op = parts[1] if len(parts) > 1 else None
                addr = parts[2] if len(parts) > 2 else None
                self.symbol_table[label] = nextmem

            self.instructions.append({'op': op, 'addr': addr})
            if op:
                nextmem += 1
        
        # Passaggio 2: Genera la memoria virtuale
        nextmem = 0
        for instr in self.instructions:
            op_str = instr['op']
            addr_str = instr['addr']

            if not op_str:
                continue

            if op_str == "const":
                val = int(addr_str) if addr_str is not None else 0
                self.memory[nextmem] = val
            else:
                opcode = self.opcodes[op_str]
                address = 0
                if addr_str:
                    if addr_str.isdigit():
                        address = int(addr_str)
                    elif addr_str in self.symbol_table:
                        address = self.symbol_table[addr_str]
                    else:
                        print(f"Errore di assemblaggio: etichetta '{addr_str}' non trovata.")
                        sys.exit(1)
                
                self.memory[nextmem] = 1000 * opcode + address
            
            nextmem += 1

    def run(self, input_values):
        input_pointer = 0
        output_values = []
        self.pc = 0

        while self.pc >= 0:
            if self.pc >= len(self.memory):
                print(f"Errore di runtime: accesso a memoria non valida a PC={self.pc}")
                break

            instr = self.memory[self.pc]
            addr = instr % 1000
            code = instr // 1000
            self.pc += 1

            if code < 0 or code > max(self.reverse_opcodes.keys()):
                print(f"Errore di runtime: opcode non valido a PC={self.pc-1}")
                break

            instruction_str = self.reverse_opcodes[code]
            
            if instruction_str == "get":
                if input_pointer < len(input_values):
                    self.acc = input_values[input_pointer]
                    input_pointer += 1
                else:
                    self.acc = 0
            elif instruction_str == "put":
                print(self.acc)
                output_values.append(self.acc)
            elif instruction_str == "st":
                self.memory[addr] = self.acc
            elif instruction_str == "ld":
                self.acc = self.memory[addr]
            elif instruction_str == "add":
                self.acc += self.memory[addr]
            elif instruction_str == "sub":
                self.acc -= self.memory[addr]
            elif instruction_str == "jpos":
                if self.acc > 0:
                    self.pc = addr
            elif instruction_str == "jz":
                if self.acc == 0:
                    self.pc = addr
            elif instruction_str == "j":
                self.pc = addr
            elif instruction_str == "halt":
                self.pc = -1

        return output_values

# Uso del programma
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python asm.py <program_file.dat>")
        sys.exit(1)

    # Per questo esempio, usiamo il tuo file `sample.dat`
    program_file = sys.argv[1]

    # Esegui l'assembler e l'interprete
    vm = AssemblerInterpreter()
    vm.assemble(program_file)
    
    # Input simulato
    input_values = [5, 7, 0]
    vm.run(input_values)