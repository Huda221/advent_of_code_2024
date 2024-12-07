def parse_input(file_path):
    """Parse the input file to extract ordering rules and updates."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}. Please check the file path.")

    # Split into rules and updates sections
    try:
        rules_section, updates_section = content.strip().split('\n\n')
    except ValueError:
        raise ValueError("Input file must contain two sections separated by a blank line.")

    # Parse rules and updates
    try:
        rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
        updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    except ValueError:
        raise ValueError("Ensure that rules use '|' and updates use ',' as delimiters, and contain only integers.")

    return rules, updates


def is_update_valid(update, rules):
    """Check if an update follows the given rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def sum_middle_pages(file_path):
    """Determine the sum of middle pages for correctly ordered updates."""
    # Parse input
    rules, updates = parse_input(file_path)

    total = 0

    for pages in updates:
        if is_update_valid(pages, rules):
            # Find the middle page
            middle_index = len(pages) // 2
            middle_page = pages[middle_index]
            total += middle_page

    return total


# Ask for file path dynamically to avoid hardcoding
file_path = input("Enter the path to the input .txt file: ")

try:
    # Calculate the sum of middle pages
    result = sum_middle_pages(file_path)
    print("Sum of middle pages:", result)
except Exception as e:
    print(f"An error occurred: {e}")
