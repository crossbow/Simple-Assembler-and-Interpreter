# Simple Assembler and Interpreter

This repository contains a simple assembler and interpreter for a custom, low-level instruction set. The project includes two versions: the original implementation in **AWK** and a port to **Python 3**.

-----

## Project Purpose

The primary goal of this project is to demonstrate the fundamental principles of computer architecture, including:

  * **Assembler Design:** The process of converting human-readable assembly code into machine-executable instructions.
  * **Interpreter Design:** The execution of machine code by a program that simulates a virtual machine.
  * **Low-Level Programming:** Understanding how basic operations like data storage, arithmetic, and control flow are managed at the machine level.

The AWK and Python implementations serve as a comparison, showing how the same core logic can be expressed in two very different programming paradigms: AWK, a powerful text-processing language, and Python, a general-purpose scripting language.

-----

## The Assembly Language

The assembly language is designed to be minimalistic and easy to understand. It operates on a single accumulator register (`acc`) and a simple memory model.

### Instruction Set

The available instructions are as follows:

  * `const <value>`: Defines a constant value at a given memory location.
  * `get`: Reads a number from standard input and stores it in the accumulator (`acc`).
  * `put`: Prints the value of the accumulator to standard output.
  * `ld <address>`: Loads the value from a memory `address` into the accumulator.
  * `st <address>`: Stores the value of the accumulator into a memory `address`.
  * `add <address>`: Adds the value at a memory `address` to the accumulator.
  * `sub <address>`: Subtracts the value at a memory `address` from the accumulator.
  * `jpos <address>`: Jumps to the specified `address` if the accumulator's value is positive (`> 0`).
  * `jz <address>`: Jumps to the specified `address` if the accumulator's value is zero (`== 0`).
  * `j <address>`: Unconditionally jumps to the specified `address`.
  * `halt`: Halts program execution.

The assembler also supports **labels**, which are symbolic names for memory addresses (e.g., `loop`, `done`, `zero`).

-----

## How to Run

### Original AWK Version

The original AWK script `asm.awk` acts as both the assembler and the interpreter.

To assemble and run a program, use the following command:

```sh
awk -f asm.awk <program-file> <data-files ...>
```

For example, to run the `sample.asm` program:

```sh
awk -f asm.awk sample.asm
```

and pass each value on CLI. Press 0 to terminate. This example add 5 to 7 and print 12 as a result.

```sh
5
7
0
12
```

### Python 3 Version

The Python script `asm_Gemini.py` provides the same functionality.

To run an assembly program:

```sh
python3 asm_Gemini.py <program-file>
```

For example, with `sample.asm`:

```sh
python3 asm_Gemini.py sample.asm
```

The Python script also simulates input, so you can easily test programs without manual entry.
