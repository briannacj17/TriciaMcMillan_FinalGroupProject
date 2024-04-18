#jsonUtilities.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: To decrypt location
# Citations:
# Anything else that's relevant:

import json

if __name__ == "__main__":
       
    # Assuming your JSON file is named "data.json"
    file_path = "..\\dataPackage\\EncryptedGroupHints Spring 2024 Section 002.json"
    
class Number_Words():    
        with open(file_path, 'r') as f:
            data = json.load(f)
    
    # Extract specific data
        name = data['Tricia McMillan']
    
    
    # Print the extracted data
        print("Data:", name)