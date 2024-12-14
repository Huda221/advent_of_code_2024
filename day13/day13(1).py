def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_solution(a1, a2, b1, b2, target_x, target_y):
    print(f"\nSolving for equations:")


    # Calculate determinant
    det = a1 * b2 - a2 * b1

    if det == 0:
        print("No solution - equations are dependent")
        return None

    # Using Cramer's rule
    n = (target_x * b2 - target_y * b1) / det
    m = (a1 * target_y - a2 * target_x) / det

    # Check if solution is integer and non-negative
    if n != int(n) or m != int(m) or n < 0 or m < 0:
        print(f"No valid solution: A={n}, B={m}")
        return None

    n = int(n)
    m = int(m)

    # Verify solution
    if (a1 * n + b1 * m == target_x) and (a2 * n + b2 * m == target_y):
        print(f"Found solution: A={n}, B={m}")
        return (n, m)

    return None

def solve_claw_machines_part2(input_data):
    total_tokens = 0
    possible_prizes = 0
    OFFSET = 10000000000000

    lines = input_data.strip().split('\n')

    for i in range(0, len(lines), 4):
        if i + 2 >= len(lines):
            break


        # Parse input
        a_line = lines[i].strip()
        ax = int(a_line[a_line.find('X+')+2:a_line.find(',')])
        ay = int(a_line[a_line.find('Y+')+2:])

        b_line = lines[i+1].strip()
        bx = int(b_line[b_line.find('X+')+2:b_line.find(',')])
        by = int(b_line[b_line.find('Y+')+2:])

        p_line = lines[i+2].strip()
        px = int(p_line[p_line.find('X=')+2:p_line.find(',')]) + OFFSET
        py = int(p_line[p_line.find('Y=')+2:]) + OFFSET


        # Find solution
        solution = find_solution(ax, ay, bx, by, px, py)

        if solution:
            n, m = solution
            tokens = 3 * n + m
            total_tokens += tokens
            possible_prizes += 1
            print(f"Tokens needed: {tokens}")
        else:
            print("No solution found")

    return total_tokens, possible_prizes

# Function to read input from file and process it
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    return input_data

# Sample usage
input_file_path = 'day13/input13.txt'  # Path to the input file
input_data = read_input_file(input_file_path)
total_tokens, possible_prizes = solve_claw_machines_part2(input_data)
print(f"Total tokens needed: {total_tokens}")
