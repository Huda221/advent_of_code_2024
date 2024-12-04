#!/usr/bin/env python
# coding: utf-8

# # problem 1
# 
# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!
# 
# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.
# 
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
# 
# 
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:
# 
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:
# 
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?

# In[1]:


def count_xmas_occurrences(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)   # Up-Right
    ]
    count = 0

    # Function to check if a word exists in a specific direction
    def search_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check all directions from the current cell
            for dr, dc in directions:
                if search_direction(r, c, dr, dc):
                    count += 1

    return count
     # Read the input grid from a file
with open('input4.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Find and print the number of occurrences of "XMAS"
result = count_xmas_occurrences(grid)
print(result)


# # Problem 2
# 
# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?
# 
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
# 
# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.
# 
# Here's the same example from before, but this time all of the X-MASes have been kept instead:
# 
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.
# 
# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

# In[2]:


def count_x_mas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Helper function to check if a diagonal matches MAS
    def check_diagonal(r, c, dr1, dc1, dr2, dc2):
        try:
            # Check one MAS diagonal (M-S) and the reverse (S-M)
            if (grid[r + dr1][c + dc1] == 'M' and
                grid[r][c] == 'A' and
                grid[r + dr2][c + dc2] == 'S'):
                return True
            if (grid[r + dr1][c + dc1] == 'S' and
                grid[r][c] == 'A' and
                grid[r + dr2][c + dc2] == 'M'):
                return True
        except IndexError:
            pass
        return False

    # Traverse the grid to find the center of the X
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check for the center 'A'
            if grid[r][c] == 'A':
                # Check for the top-left and bottom-right MAS
                if (check_diagonal(r, c, -1, -1, 1, 1) and
                    check_diagonal(r, c, -1, 1, 1, -1)):
                    count += 1

    return count

# Read the input grid from a file
with open('input4.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Find and print the number of X-MAS patterns
result = count_x_mas_patterns(grid)
print(result)
     


# In[ ]:




