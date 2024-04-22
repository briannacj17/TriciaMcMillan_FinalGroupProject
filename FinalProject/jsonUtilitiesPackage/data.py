#data.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan, Deonta Williams
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decode Tricia McMillian word rows for location
# Citations:
# Anything else that's relevant:

"""
This py file imports all the data files and json tools
so that for each line in the file it prints the row.
"""

from dataPackage import *
from jsonUtilitiesPackage.jsonUtilities import *

def print_specific_rows(txt_file, row_numbers):
    # Open the text file and read its contents
    with open(txt_file, 'r', encoding='utf-8') as file:
        # Create a dictionary to store the lines with their corresponding line numbers
        lines = {line_number: line.strip() for line_number, line in enumerate(file, 1)}
        
    # Iterate through the row numbers to print in the specified order
    for row_number in row_numbers:
        # Check if the row number exists in the lines dictionary
        if row_number in lines:
            # Print the line corresponding to the row number
            print(lines[row_number +1])
