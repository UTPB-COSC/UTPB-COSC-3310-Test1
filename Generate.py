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
print(f"Solution to Problem #10 is: {problem_10_1} or {problem_10_2} = {(int(problem_10_1.lstrip('0d'), 10) | int(problem_10_2.lstrip('0d'), 10))}")

problem_11_1 = rand_hex(4, False, False)
problem_11_2 = rand_hex(4, False, False)
int_a = int(problem_11_1, 16)
int_b = int(problem_11_2, 16)
product = int_a * int_b
binary_11 = format(product, '#010b')
print(f"Solution to Problem #11 is: {problem_11_1} * {problem_11_2} = 0d{product} = {binary_11} = {hex(int(binary_11, 2))}")

problem_12_1 = rand_bin(4, False, False)
problem_12_2 = rand_bin(4, False, False)
length = len(problem_12_1) + len(problem_12_2) - 2
print(f"Solution to Problem #12 is: {break_bin(problem_12_1)} * {break_bin(problem_12_2)} = {break_bin(format(int(problem_12_1, 2) * int(problem_12_2, 2), f'#0{length}b'))}")

latex_code = f'''
\\documentclass[12pt]{{article}}
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
\\noindent \\Large \\textbf{{COSC-3310}}  \\hfill \\textbf{{Midterm}}  \\hfill \\textbf{{Oct 02, 2024}}\\\\

\\vspace{{.3cm}}

\\textbf{{Name}}: \\hrulefill

\\Large
\\begin{{itemize}}
    \\item No notes, calculators, or any form of tool or information other than a pencil and the provided (test) paper.
    \\item Prefix all applicable answers with $\\mathtt{{0b}}$, $\\mathtt{{0d}}$, etc. to match the requested format.
    \\begin{{itemize}}
        \\item For the "convert X to" problems, the format is specified.
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

\\end{{document}}

'''

with open('test1.tex', 'w') as latex_file:
    latex_file.write(latex_code)
