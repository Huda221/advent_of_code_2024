def transform_stones(stones):
    """
    Transform stones according to the given rules:
    1. If stone is 0, replace with 1
    2. If stone has even number of digits, split into two stones
    3. Otherwise, multiply stone by 2024
    """
    new_stones = []

    for stone in stones:
        # Rule 1: If stone is 0, replace with 1
        if stone == 0:
            new_stones.append(1)

        # Rule 2: If stone has even number of digits, split the stone
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            left_stone = int(stone_str[:mid])
            right_stone = int(stone_str[mid:])

            # Remove leading zeros
            left_stone = int(str(left_stone))
            right_stone = int(str(right_stone))

            new_stones.extend([left_stone, right_stone])

        # Rule 3: Multiply stone by 2024
        else:
            new_stones.append(stone * 2024)

    return new_stones

def simulate_blinks(initial_stones, num_blinks):
    """
    Simulate stone transformations for specified number of blinks
    """
    stones = initial_stones.copy()

    for _ in range(num_blinks):
        stones = transform_stones(stones)

    return stones

def main():
    # Read input from file
    with open('day11/input11.txt', 'r') as file:
        initial_stones = [int(x) for x in file.read().split()]

    # Simulate 25 blinks
    final_stones = simulate_blinks(initial_stones, 25)

    # Print number of stones after 25 blinks
    print(f"Number of stones after 25 blinks: {len(final_stones)}")

if __name__ == "__main__":
    main()