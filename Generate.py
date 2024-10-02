import random


def rand_int(bits=16, signed=True, negative=False):
    if not signed or negative:
        range_min = 2 ** (bits - 1)
        range_max = (2 ** bits) - 1
    else:
        range_min = 2 ** (bits - 2)
        range_max = (2 ** (bits - 1)) - 1
    return random.randint(range_min, range_max)


def rand_decimal(bits=16, signed=True, negative=False):
    value = rand_int(bits, signed, negative)
    if negative:
        return f"-0d{value}"
    return f"0d{value}"


def rand_hex(bits=16, signed=True, negative=False):
    value = rand_int(bits, signed, negative)
    if negative:
        return hex(value)
    hexadec = hex(value)
    if int(hexadec[2], 16) >= 8:
        hexadec = hexadec.replace('0x', '0x0')
    return hexadec


def rand_bin(bits=16, signed=True, negative=False):
    value = rand_int(bits, signed, negative)
    if negative:
        return format(value, f"#0{bits + 2}b")
    binary = format(value, f"#0{bits + 2}b")
    if binary.startswith('0b0'):
        return binary
    binary = binary.replace('0b', '0b0')
    return binary


def break_bin(binary):
    bits = len(binary) - 2
    offset = 2 + (bits % 4)
    formatted = "0b" + binary[2:offset] + ("|" if offset > 2 else "")
    for x in range(bits // 4):
        formatted += binary[offset:offset + 4] + "|"
        offset += 4
    return formatted.rstrip("|")


def ones_complement(binary):
    return binary.replace('1', '2').replace('0', '1').replace('2', '0').replace('1b', '0b')


def twos_complement(binary):
    negation = ones_complement(binary)
    return bin(int(negation, 2) + 0b01)


problem_1 = rand_decimal(16, False)
print(f"Solution to Problem #1 is: {problem_1} = {break_bin(format(int(problem_1.lstrip('0d'), 10), '#019b'))}")

problem_2 = rand_bin(16, True, True)
negation_2 = ones_complement(problem_2)
print(f"Solution to Problem #2 is: {break_bin(problem_2)} = -0d{int(negation_2, 2)}")

problem_3 = rand_decimal(16)
print(f"Solution to Problem #3 is: {problem_3} = {hex(int(problem_3.lstrip('0d'), 10))}")

problem_4 = rand_hex(16, True, True)
binary_4 = bin(int(problem_4, 16))
negation_4 = twos_complement(binary_4)
print(f"Solution to Problem #4 is: {problem_4} = -0d{int(negation_4, 2)}")

problem_5_1 = rand_bin()
problem_5_2 = rand_bin()
print(f"Solution to Problem #5 is: {break_bin(problem_5_1)} + {break_bin(problem_5_2)} = {break_bin(format(int(problem_5_1, 2) + int(problem_5_2, 2), '#019b'))}")

problem_6_1 = rand_hex(20)
problem_6_2 = rand_hex(20)
print(f"Solution to Problem #6 is: {problem_6_1} + {problem_6_2} = {hex(int(problem_6_1, 16) + int(problem_6_2, 16))}")

problem_7_1 = rand_bin()
while int(problem_7_1, 2) < 28000:
    problem_7_1 = rand_bin()
problem_7_2 = rand_bin()
while int(problem_7_2, 2) > int(problem_7_1, 2):
    problem_7_2 = rand_bin()
print(f"Solution to Problem #7 is: {break_bin(problem_7_1)} - {break_bin(problem_7_2)} = {break_bin(format(int(problem_7_1, 2) - int(problem_7_2, 2), '#018b'))}")

problem_8_1 = rand_bin(negative=True)
problem_8_2 = rand_bin()
print(f"Solution to Problem #8 is: {break_bin(problem_8_1)} and {break_bin(problem_8_2)} = {break_bin(format(int(problem_8_1, 2) & int(problem_8_2, 2), '#018b'))}")

problem_9_1 = rand_hex(20, True, True)
problem_9_2 = rand_hex(20, True, False)
print(f"Solution to Problem #9 is: {problem_9_1} xor {problem_9_2} = {hex(int(problem_9_1, 16) ^ int(problem_9_2, 16))}")

problem_10_1 = rand_decimal(16, True, False)
problem_10_2 = rand_decimal(16, True, False)
print(f"Solution to Problem #10 is: {problem_10_1} or {problem_10_2} = 0d{(int(problem_10_1.lstrip('0d'), 10) | int(problem_10_2.lstrip('0d'), 10))}")

problem_11_1 = rand_hex(4, False, False)
problem_11_2 = rand_hex(4, False, False)
int_a = int(problem_11_1, 16)
int_b = int(problem_11_2, 16)
product = int_a * int_b
binary_11 = format(product, '#010b')
print(f"Solution to Problem #11 is: {problem_11_1.replace('0x0', '0x')} * {problem_11_2.replace('0x0', '0x')} = 0d{product} = {binary_11} = {hex(int(binary_11, 2))}")

problem_12_1 = rand_bin(4, False, False)
problem_12_2 = rand_bin(4, False, False)
length = len(problem_12_1) + len(problem_12_2) - 2
problem_12_1 = problem_12_1.replace('0b0', '0b')
problem_12_2 = problem_12_2.replace('0b0', '0b')
print(f"Solution to Problem #12 is: {break_bin(problem_12_1)} * {break_bin(problem_12_2)} = {break_bin(format(int(problem_12_1, 2) * int(problem_12_2, 2), f'#0{length}b'))}")

sa_questions = [
    'Describe the role of the ALU within the CPU.  Give examples of six of the most basic operations handled by the ALU.',
    'Explain the key differences between volatile and non-volatile memory. Provide examples of each type of memory and their typical uses in a computer system.',
    'What is the function of the northbridge and southbridge in computer architecture, and how do they differ in terms of the components they manage?',
    'Outline the steps involved in the FDE cycle. Why is this cycle fundamental to the operation of a CPU?',
    'Why is the distinction between volatile and non-volatile memory important in terms of data storage and system functionality during power loss?',
    'What is the purpose of the system clock in a computer\'s CPU, and how does it affect the timing and synchronization of operations within the processor?',
    'RAM DIMMs are commonly sold in pairs, and the RAM slots on a motherboard are commonly arranged in pairs denoted A1,B1,A2,B2 or similar.  Why?'
]

sa_answers = [
    'The Arithmetic Logic Unit (ALU) is a key component of the CPU responsible for performing arithmetic operations and logic operations.  The basic operations it handles are: the arithmetic operations (add, sub, mul, div) and the logical operations (and, or, xor, not, nand, nor, xnor).',
    'Volatile memory loses its data when power is turned off, with RAM being a primary example, as it temporarily stores data that is actively being used by the CPU. Non-volatile memory, such as ROM or flash memory, retains data even when the system is powered down, making it useful for permanent storage of essential system instructions or user data.',
    'The northbridge and southbridge are key components of a motherboard\'s chipset, with the northbridge managing communication between high-speed components like the CPU, RAM, and GPU, while the southbridge handles slower peripheral devices such as USB ports, hard drives, and audio. The northbridge facilitates faster data transfers crucial for system performance, whereas the southbridge ensures efficient handling of input/output operations.',
    'The Fetch-Decode-Execute (FDE) cycle is the fundamental process by which a CPU executes instructions. During this cycle, the CPU fetches an instruction from memory, decodes it to understand the operation required, and then executes it, either performing a computation or interacting with memory or I/O devices. This cycle is continuous and forms the basis of program execution.',
    'The distinction between volatile and non-volatile memory is important because volatile memory (e.g., RAM) loses its contents when the power is turned off, while non-volatile memory (e.g., flash storage or ROM) retains data even without power. This distinction ensures that critical system information and user data are preserved after a shutdown or power loss.',
    'The system clock is responsible for providing the timing signals that synchronize all operations within the CPU and the broader system. It determines how fast instructions are executed by generating a steady stream of pulses, with each pulse coordinating the timing of the fetch-decode-execute cycle and communication between components.',
    'Dual Inline Memory Modules are commonly sold in pairs because in order to actually provide Double Data Rate (DDR) transfer speeds, the system must pair the RAM modules and use them together as a single unit. Therefore, in order for them to correctly function a pair of identical DIMMs must be inserted into the A1 and A2 slots.'
]

mobo_list = [
    'A',
    'B',
    'C',
    'D',
    'E'
]

p13_list = random.sample(mobo_list, 3)
while 'D' not in p13_list and 'E' not in p13_list:
    p13_list = random.sample(mobo_list, 3)
p13_list.sort()
problem_13 = f'{p13_list[0]}, {p13_list[1]}, and {p13_list[2]}'
print(problem_13)

p14_idx = random.randrange(len(sa_answers))
problem_14 = sa_questions[p14_idx]
print(f"Sample answer to Problem #14: {sa_answers[p14_idx]}")

latex_code = f'''\\documentclass[12pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage[all]{{xy}}


\\usepackage{{amsmath,amsthm,amssymb,color,latexsym}}
\\usepackage{{geometry}}
\\geometry{{letterpaper}}
\\usepackage{{graphicx}}
\\usepackage{{multicol}}
\\usepackage{{svg}}

\\newtheorem{{problem}}{{}}%Problem}}

\\newenvironment{{solution}}[1][\\it{{Solution}}]{{\\textbf{{#1. }} }}{{$\\square$}}


\\begin{{document}}
\\noindent \\Large \\textbf{{COSC-3310}}  \\hfill \\textbf{{Midterm}}  \\hfill \\textbf{{Oct 07, 2024}}\\\\

\\vspace{{.3cm}}

\\textbf{{Name}}: \\hrulefill

\\Large
\\begin{{itemize}}
    \\item No notes, calculators, or any form of tool or information other than a pencil and the provided (test) paper.
    \\item Prefix all applicable answers with $\\mathtt{{0b}}$, $\\mathtt{{0d}}$, etc. to match the requested format.
    \\begin{{itemize}}
        \\item For the "convert X to Y" problems, the format is specified.
        \\item For all other problems, the format should match that given by the numbers in the problem.
        \\item Thus, if you convert from hexadecimal to binary to perform a bitwise logical/arithmetic operation, your answer must be converted back to hexadecimal.
    \\end{{itemize}}
    \\item Be careful of signing and sign bits.  It may be necessary to \\textbf{{pad}} binary values with a leading 0 in the most-significant position.
    \\item Hexadecimal values with a most-significant digit of 0x8 or higher should be understood to be negative.
    \\item When writing negative decimal values, write the sign before the prefix (-$\\mathtt{{0d}})$.
    \\item It would be a good idea to write out the decimal, binary, and hexadecimal table on the back of this page.
    \\item You may also wish to write out a list of the powers of 2 from $2 ^ 0$ to $2 ^ {{15}}$, possibly in a margin.
\\end{{itemize}}

\\newpage

% Decimal to binary conversion
\\begin{{problem}}
\\Large Convert $\\mathtt{{{problem_1}}}$ to binary.
\\end{{problem}}

\\vspace{{9cm}}

% Binary to decimal conversion
\\begin{{problem}}
\\large Convert $\\mathtt{{{break_bin(problem_2)}}}$ (1's complement) to decimal.
\\end{{problem}}

\\newpage

% Decimal to hex conversion
\\begin{{problem}}
\\Large Convert $\\mathtt{{{problem_3}}}$ to hexadecimal.
\\end{{problem}}

\\vspace{{11cm}}

% Hex to decimal conversion
\\begin{{problem}}
\\Large Convert $\\mathtt{{{problem_4}}}$ (2's complement) to decimal.
\\end{{problem}}

\\newpage

% Binary addition
\\begin{{problem}}
\\large Find the sum $\\mathtt{{{break_bin(problem_5_1)}}} + \\mathtt{{{break_bin(problem_5_2)}}}$.
\\end{{problem}}

\\vspace{{6cm}}

% Hex addition
\\begin{{problem}}
\\Large Find the sum $\\mathtt{{{problem_6_1}}} + \\mathtt{{{problem_6_2}}}$.
\\end{{problem}}

\\vspace{{6cm}}

% Binary subtraction
\\begin{{problem}}
\\large Find the difference $\\mathtt{{{break_bin(problem_7_1)}}} - \\mathtt{{{break_bin(problem_7_2)}}}$.
\\end{{problem}}

\\newpage

% Binary bitwise and
\\begin{{problem}}
\\large Find the result $\\mathtt{{{break_bin(problem_8_1)}}}$ and $\\mathtt{{{break_bin(problem_8_2)}}}$.
\\end{{problem}}

\\vspace{{5cm}}

% Hex bitwise xor
\\begin{{problem}}
\\Large Find the result $\\mathtt{{{problem_9_1}}}$ xor $\\mathtt{{{problem_9_2}}}$.
\\end{{problem}}

\\vspace{{5cm}}

% Decimal bitwise or
\\begin{{problem}}
\\Large Find the result $\\mathtt{{{problem_10_1}}}$ or $\\mathtt{{{problem_10_2}}}$
\\end{{problem}}

\\newpage

% Hex multiplication
\\begin{{problem}}
\\Large Find the product $\\mathtt{{{problem_11_1}}} * \\mathtt{{{problem_11_2}}}$.
\\end{{problem}}

\\vspace{{11cm}}

% Binary multiplication
\\begin{{problem}}
\\Large Find the product $\\mathtt{{{problem_12_1}}} * \\mathtt{{{problem_12_2}}}$.
\\end{{problem}}

\\newpage

\\begin{{problem}}
    \\large Identify and briefly describe the components labeled {problem_13}.
    \\begin{{figure}}
        \\includegraphics[width=0.7\\linewidth]{{Test_MB.png}}
    \\end{{figure}}
\\end{{problem}}

\\begin{{problem}}
    \\Large {problem_14}
\\end{{problem}}

\\end{{document}}
'''

with open('test1.tex', 'w') as latex_file:
    latex_file.write(latex_code)
