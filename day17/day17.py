#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import os

# Adjust the input file path for Jupyter
input_path = 'input17.txt'
a, b, c, *program = map(int, re.findall(r"\d+", open(input_path).read()))

pointer = 0
output = []

def combo(operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    raise AssertionError(f"unrecognized combo operand {operand}")

while pointer < len(program):
    ins = program[pointer]
    operand = program[pointer + 1]
    if ins == 0: # adv
        a = a >> combo(operand)
    elif ins == 1: # bxl
        b = b ^ operand
    elif ins == 2: # bst
        b = combo(operand) % 8
    elif ins == 3: # jnz
        if a != 0:
            pointer = operand
            continue
    elif ins == 4: # bxc
        b = b ^ c
    elif ins == 5: # out
        output.append(combo(operand) % 8)
    elif ins == 6: # bdv
        b = a >> combo(operand)
    elif ins == 7: # cdv
        c = a >> combo(operand)
    pointer += 2

# Use standard print for Jupyter
print(*output, sep=",")


# In[3]:


import re
import os

# Adjust the input file path for Jupyter
input_path = 'input17.txt'
program = list(map(int, re.findall(r"\d+", open(input_path).read())[3:]))
assert program[-2:] == [3, 0], "program does not end with JNZ 0"

def find(target, ans):
    if target == []: 
        return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None
        adv3 = False

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:  # ADV
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:  # BXL
                b = b ^ operand
            elif ins == 2:  # BST
                b = combo(operand) % 8
            elif ins == 3:  # JNZ
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:  # BXC
                b = b ^ c
            elif ins == 5:  # OUT
                assert output is None, "program has multiple OUT"
                output = combo(operand) % 8
            elif ins == 6:  # BDV
                b = a >> combo(operand)
            elif ins == 7:  # CDV
                c = a >> combo(operand)
        
        if output == target[-1]:
            sub = find(target[:-1], a)
            if sub is None: 
                continue
            return sub

# Use standard print for output
print(find(program, 0))


# In[ ]:




