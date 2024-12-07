def parse_input(file_path):
    """Parse the input file to extract ordering rules and updates."""
    with open(file_path, 'r') as file:
        content = file.read()

    # Split into rules and updates sections
    rules_section, updates_section = content.strip().split('\n\n')

    # Parse rules and updates
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

    return rules, updates


def is_update_valid(update, rules):
    """Check if an update follows the given rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def reorder_update(update, rules):
    """Reorder an update based on the rules to make it valid."""
    # Create a copy to avoid modifying the original update
    ordered_update = update[:]

    # Perform a topological sort based on the rules
    for _ in range(len(ordered_update)):
        for x, y in rules:
            if x in ordered_update and y in ordered_update:
                x_index = ordered_update.index(x)
                y_index = ordered_update.index(y)
                if x_index > y_index:
                    # Move x before y
                    ordered_update.remove(x)
                    ordered_update.insert(y_index, x)

    return ordered_update


def sum_middle_pages_for_incorrect(file_path):
    """Compute the sum of middle pages after reordering incorrect updates."""
    # Parse input
    rules, updates = parse_input(file_path)

    total = 0

    for pages in updates:
        if not is_update_valid(pages, rules):
            # Reorder the incorrect update
            corrected_update = reorder_update(pages, rules)

            # Find the middle page
            middle_index = len(corrected_update) // 2
            middle_page = corrected_update[middle_index]
            total += middle_page

    return total


# File path
file_path = 'input5.txt'

# Calculate the sum of middle pages for incorrectly ordered updates
try:
    result = sum_middle_pages_for_incorrect(file_path)
    print("Sum of middle pages for incorrect updates:", result)
except Exception as e:
    print(f"An error occurred: {e}")
