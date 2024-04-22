#main.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan, Deonta Williams
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypting complex code
# Citations:
# Anything else that's relevant:


"""
ENTRY POINT
This main py file imports all the libraries and packages with their 
functions we made or used to run our app. The app runs our encryption, 
prints the decyption numbers and decrypted group location
and finally prints out the group picture
"""

import json
from dataUtilitiesPackage.decryption import *
from jsonUtilitiesPackage.data import *
from dataPackage.image import *

if __name__ == "__main__":
    # Extract the movie name for Tricia McMillian
    MovieEncryption.decrypt_message_from_file(file_path, 'Tricia McMillan')
    
    # Print the numbers to decrypt the location for the group picture
    Number_Words()
     
    # Print the location to take a Group Picture
    txt_file = "..\\dataPackage\\UCEnglish.txt"
    row_numbers_to_extract = [30942, 46342, 42061, 103568, 5040, 41700, 31066]
    print_specific_rows(txt_file, row_numbers_to_extract)
    # Open the group picture 
    im.show()
