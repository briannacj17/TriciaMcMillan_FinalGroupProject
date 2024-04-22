#jsonUtilities.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan, Deonta Williams
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Extract Tricia McMillian word rows
# Citations:
# Anything else that's relevant:


"""
This py file imports json then opens the json file to print the data for desired 
name.
"""

import json

def Number_Words():
    with open("..\\dataPackage\\EncryptedGroupHints Spring 2024 Section 002.json", 'r') as f:
        data = json.load(f)
                    
        # Extract specific data
        name = data['Tricia McMillan']       
        # Print the extracted data
        print(name)
