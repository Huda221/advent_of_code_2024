from itertools import product

def parse_input(file_path):
    """Parse the input file and return a list of test cases."""
    equations = []
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
        for line in lines:
            if line.strip() == "":
                continue
            test_value, numbers = line.split(":")
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((test_value, numbers))
    return equations

def concatenate(a, b):
    """Concatenate two numbers as per the || operator."""
    return int(str(a) + str(b))

def evaluate_expression(numbers, operators):
    """Evaluate the expression with the given numbers and operators."""
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = concatenate(result, numbers[i + 1])
    return result

def is_solvable(test_value, numbers):
    """Check if the test value can be achieved by inserting operators."""
    num_positions = len(numbers) - 1  # Number of operator positions
    operator_combinations = product(['+', '*', '||'], repeat=num_positions)

    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def total_calibration_result(file_path):
    """Calculate the total calibration result for all solvable equations."""
    equations = parse_input(file_path)
    total = 0

    for test_value, numbers in equations:
        if is_solvable(test_value, numbers):
            total += test_value

    return total

# Example usage
file_path = "day7/input7.txt"
result = total_calibration_result(file_path)
print("Total Calibration Result:", result)
     