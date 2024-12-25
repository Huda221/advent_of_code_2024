#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
import re

# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

# Perform logic gate operations
def apply_gate(gate, a, b):
    if gate == 'AND':
        return a & b
    elif gate == 'OR':
        return a | b
    elif gate == 'XOR':
        return a ^ b
    return None

# Simulate the circuit
def simulate_circuit(lines):
    wire_values = {}
    gate_operations = []

    # Parse input
    for line in lines:
        if ':' in line:
            wire, value = line.split(': ')
            wire_values[wire] = int(value)
        else:
            gate_operations.append(line)

    # Process gates until all outputs are computed
    while gate_operations:
        remaining_operations = []
        for operation in gate_operations:
            match = re.match(r'(.+) (AND|OR|XOR) (.+) -> (.+)', operation)
            if match:
                a, gate, b, output = match.groups()
                if a in wire_values and b in wire_values:
                    wire_values[output] = apply_gate(gate, wire_values[a], wire_values[b])
                else:
                    remaining_operations.append(operation)
        gate_operations = remaining_operations

    # Collect and sort output wires starting with 'z'
    output_bits = []
    for wire, value in wire_values.items():
        if wire.startswith('z'):
            output_bits.append((wire, value))

    output_bits.sort()  # Sort to ensure correct binary order (z00, z01, ...)

    # Construct binary output
    binary_result = ''.join(str(bit[1]) for bit in output_bits[::-1])
    return int(binary_result, 2)

if __name__ == "__main__":
    input_lines = read_input("input24.txt")
    result = simulate_circuit(input_lines)
    print("Output (Decimal):", result)


# In[ ]:


#!/usr/bin/env pypy3
from __future__ import annotations
import z3  # Corrected to z3
import random
from functools import cache
from itertools import product, combinations
from collections import defaultdict, deque

# Utility functions that were in util.py
def lines(s: str):
    return s.strip().split('\n')

def bfs(adj, start):
    dist = {start: 0}
    prev = {start: None}
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                prev[v] = u
                q.append(v)

    return dist, prev

def topsort(adj):
    indeg = defaultdict(int)
    for u in adj:
        for v in adj[u]:
            indeg[v] += 1

    q = deque()
    for u in adj:
        if indeg[u] == 0:
            q.append(u)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order, len(order) != len(adj)

# Read from input.txt
with open("input24.txt", "r") as f:
    A, B = f.read().split("\n\n")

G = dict()
for l in lines(A):
    a, b = l.split(": ")
    G[a] = int(b)

ops = {}
for l in lines(B):
    x, dest = l.split(" -> ")
    a, op, b = x.split()
    ops[dest] = (a, op, b)

zs = {s for s in ops if s[0] == "z"}
zs = sorted(zs, key=lambda x: int(x[1:]), reverse=True)

def sim(G):
    n = len(zs)
    i = 0
    while i < n:
        for d, (a, op, b) in ops.items():
            if d in G:
                continue
            if a in G and b in G:
                x, y = G[a], G[b]
                if op == "AND":
                    G[d] = x & y
                elif op == "OR":
                    G[d] = x | y
                elif op == "XOR":
                    G[d] = x ^ y
                else:
                    assert False

                if d in zs:
                    i += 1

    return int("".join(str(G[z]) for z in zs), 2)

def mkadj():
    adj = {s: [a, b] for s, (a, _, b) in ops.items()}
    for s in G:
        adj[s] = []
    return adj

def is_cyclic():
    return topsort(mkadj())[1]

def swappable(s: str):
    return set(bfs(mkadj(), s)[1]) - set(G)

@cache
def testf(i: int):
    DIFF = 6
    if i < DIFF:
        tests = list(product(range(1 << i), repeat=2))
    else:
        tests = []
        for _ in range(1 << (2*DIFF)):
            a = random.randrange(1 << i)
            b = random.randrange(1 << i)
            tests.append((a, b))

    random.shuffle(tests)
    return tests

def f(i: int, swapped: set[str]):
    if i == 46:
        res = ",".join(sorted(swapped))
        print(f"Answer: {res}")
        return

    def getv(s: str, a: int, b: int) -> int:
        if s[0] == "x":
            return (a >> int(s[1:])) & 1
        if s[0] == "y":
            return (b >> int(s[1:])) & 1
        av, op, bv = ops[s]
        x, y = getv(av, a, b), getv(bv, a, b)
        if op == "AND":
            return x & y
        if op == "OR":
            return x | y
        if op == "XOR":
            return x ^ y

    def check():
        for a, b in testf(i):
            for j in range(i+1):
                x = getv(f"z{j:02}", a, b)
                if x != ((a + b) >> j) & 1:
                    return False
        return True

    works = check()
    print(i, works, swapped)
    if works:
        f(i+1, swapped)
        return

    if len(swapped) == 8:
        return

    inside = swappable(f"z{i:02}") - swapped
    outside = set(ops) - swapped
    to_test = list(product(inside, outside)) + list(combinations(inside, 2))
    random.shuffle(to_test)

    for a, b in to_test:
        if a == b: continue
        ops[a], ops[b] = ops[b], ops[a]
        swapped.add(a)
        swapped.add(b)
        if not is_cyclic() and check():
            f(i, swapped)
        swapped.remove(a)
        swapped.remove(b)
        ops[a], ops[b] = ops[b], ops[a]

# Start the search
f(0, set())


# In[ ]:





# In[ ]:




