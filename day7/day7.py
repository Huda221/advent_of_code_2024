import itertools

# Function to evaluate the expression left-to-right
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '-':
            result -= numbers[i + 1]  # Handle subtraction as well
    return result

# Function to determine if test value can be achieved
def is_valid_equation(test_value, numbers):
    n = len(numbers) - 1  # Number of operator positions
    valid = False
    for ops in itertools.product("+-*", repeat=n):
        # Check if this combination of operators matches the test value
        if evaluate_expression(numbers, ops) == test_value:
            valid = True
            break
    return valid

# Read and process the input file
def process_calibration_file(filename):
    total_calibration_result = 0
    with open(filename, 'r') as file:
        for line in file:
            # Parse the line
            parts = line.strip().split(':')
            test_value = int(parts[0].strip())
            numbers = list(map(int, parts[1].strip().split()))

            # Check if the equation is valid
            if is_valid_equation(test_value, numbers):
                total_calibration_result += test_value

    return total_calibration_result

# Main function
def main():
    filename = "day7/input7.txt"  # Replace with your data file path
    result = process_calibration_file(filename)
    print(f"The total calibration result is: {result}")

# Run the main function
main()
