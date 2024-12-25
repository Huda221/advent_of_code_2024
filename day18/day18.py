#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from collections import deque

# Define the grid size (71x71)
GRID_SIZE = 71

# Read input from "input18.txt"
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Parse each line as (x, y) coordinates
        positions = [tuple(map(int, line.strip().split(','))) for line in lines if line.strip()]
        return positions
    except Exception as e:
        raise ValueError(f"Error reading input file: {e}")

# Update grid with corrupted positions
def update_grid(grid, positions):
    for x, y in positions:
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            grid[y, x] = 1  # Mark the position as corrupted

# Perform BFS to find the shortest path
def bfs_shortest_path(grid):
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (GRID_SIZE - 1, GRID_SIZE - 1)

    # Check if start or end is corrupted
    if grid[start[1], start[0]] == 1 or grid[end[1], end[0]] == 1:
        return -1

    # BFS setup
    queue = deque([(start, 0)])  # (current position, steps)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps  # Reached the exit

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE  # Check bounds
                and grid[ny, nx] == 0  # Check if the cell is not corrupted
                and (nx, ny) not in visited  # Avoid revisiting
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1  # If no path is found

# Main function
def main():
    input_file = "input18.txt"
    try:
        # Read positions from input file
        positions = read_input(input_file)

        # Initialize the grid
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

        # Simulate the first 1024 bytes falling
        update_grid(grid, positions[:1024])

        # Find the shortest path
        result = bfs_shortest_path(grid)

        # Print the result
        if result != -1:
            print(f"The minimum number of steps needed to reach the exit is: {result}")
        else:
            print("It is not possible to reach the exit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


# In[9]:


def find_first_blocking_byte(input_file):
   # Read coordinates of falling bytes from the input file
   try:
       with open(input_file, 'r') as f:
           coordinates = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]
   except Exception as e:
       raise ValueError(f"Error reading input file: {e}")

   # Define grid size and movement directions
   GRID_SIZE = 70
   DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

   # Check if a path exists from start to goal
   def is_path_exists(corrupted):
       start = (0, 0)
       goal = (GRID_SIZE, GRID_SIZE)

       # BFS initialization
       queue = [start]
       visited = set([start])

       while queue:
           current = queue.pop(0)

           if current == goal:
               return True

           for dx, dy in DIRECTIONS:
               neighbor = (current[0] + dx, current[1] + dy)

               # Check if the neighbor is valid (within grid and not corrupted)
               if (0 <= neighbor[0] <= GRID_SIZE and
                   0 <= neighbor[1] <= GRID_SIZE and
                   neighbor not in corrupted and
                   neighbor not in visited):
                   queue.append(neighbor)
                   visited.add(neighbor)

       return False

   # Track corrupted spaces and find the first blocking byte
   corrupted = set()
   for coord in coordinates:
       corrupted.add(coord)

       # Check if adding this byte blocks the path
       if not is_path_exists(corrupted):
           return coord

   return None  # No blocking byte found

# Main execution
if __name__ == "__main__":
   try:
       result = find_first_blocking_byte('input18.txt')
       if result:
           print(f"First blocking byte coordinates: {result[0]},{result[1]}")
       else:
           print("No blocking byte found.")
   except Exception as e:
       print(f"An error occurred: {e}")


# In[ ]:




