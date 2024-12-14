def flood_fill(grid, x, y, visited, plant_type):
    """Performs flood-fill to find a region and calculates its area and perimeter."""
    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    area = 0
    perimeter = 0
    visited.add((x, y))

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cx, cy = stack.pop()
        area += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                else:
                    # Edge of the region
                    perimeter += 1
            else:
                # Edge of the grid
                perimeter += 1

    return area, perimeter


def calculate_fencing_cost(grid):
    """Calculates the total fencing cost for the garden."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cost = 0

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                # Start a new region for a specific plant type
                plant_type = grid[x][y]
                area, perimeter = flood_fill(grid, x, y, visited, plant_type)
                cost = area * perimeter
                total_cost += cost
                print(f"Region {plant_type}: Area={area}, Perimeter={perimeter}, Cost={cost}")

    return total_cost


def read_map(file_path):
    """Reads the garden map from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def main():
    # Read the garden map from the input file
    file_path = "day12/input12.txt"
    garden_map = read_map(file_path)

    # Calculate the total fencing cost
    total_cost = calculate_fencing_cost(garden_map)

    # Output the result
    print("Total fencing cost:", total_cost)


if __name__ == "__main__":
    main()
