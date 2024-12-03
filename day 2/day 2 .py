#!/usr/bin/env python
# coding: utf-8

# # problem 1
# 
# --- Day 2: Red-Nosed Reports ---
# Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.
# 
# While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.
# 
# They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.
# 
# The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:
# 
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# This example data contains six reports each containing five levels.
# 
# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
# 
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:
# 
# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
# So, in this example, 2 reports are safe.
# 
# Analyze the unusual data from the engineers. How many reports are safe?

# In[1]:


def is_report_safe(report):
    """
    Determine if a report is safe based on two criteria:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    """
    levels = list(map(int, report.split()))
    if not levels:
        return False
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    if not (is_increasing or is_decreasing):
        return False
    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False
    return True

def analyze_safety_reports(input_data):
    """
    Analyze the safety of all reports in the input data
    """
    reports = input_data.strip().split('\n')

    safe_reports = sum(1 for report in reports if is_report_safe(report))

    return safe_reports
try:
    with open('input2.txt', 'r') as file:
        input_data = file.read()
    safe_report_count = analyze_safety_reports(input_data)
    print(f"Number of safe reports: {safe_report_count}")
except FileNotFoundError:
    print("Error: The file '/content/Input.txt' was not found.")



# # Problem 2 
# 
# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.
# 
# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!
# 
# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
# 
# More of the above example's reports are now safe:
# 
# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# Thanks to the Problem Dampener, 4 reports are actually safe!
# 
# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

# In[3]:


def is_report_safe(report):
    """
    Check if the report is safe based on the two conditions:
    1. The levels are either strictly increasing or strictly decreasing.
    2. The difference between adjacent levels is between 1 and 3.
    """
    levels = list(map(int, report.split()))
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False

    return True

def is_report_safe_with_dampener(report):
    """
    Check if the report can be made safe with the Problem Dampener
    (by removing at most one level).
    """
    levels = list(map(int, report.split()))
    if is_report_safe(report):
        return True
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_report_safe(' '.join(map(str, modified_report))):
            return True
    return False

def analyze_safety_reports(input_data, with_dampener=False):
    """
    Analyze the safety of all reports in the input data.
    If with_dampener is True, consider reports that can be made safe by removing one level.
    """
    reports = input_data.strip().split('\n')
    if with_dampener:
        safe_reports = sum(1 for report in reports if is_report_safe_with_dampener(report))
    else:
        safe_reports = sum(1 for report in reports if is_report_safe(report))
    return safe_reports
try:
    with open('input2.txt', 'r') as file:
        input_data = file.read()

    safe_report_count_part2 = analyze_safety_reports(input_data, with_dampener=True)
    print(f"Number of safe reports (Part 2): {safe_report_count_part2}")
except FileNotFoundError:
    print("Error: The file '/content/Input.txt' was not found.")


# In[ ]:




