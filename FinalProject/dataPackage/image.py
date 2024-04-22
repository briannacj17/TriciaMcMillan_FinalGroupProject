#image.py 
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan, Deonta Williams
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: To show and store group photo
# Citations:
# Anything else that's relevant:


"""
this python file imports the PIL library and uses open function to read our jpg file
"""

# Importing Image class from PIL module
from PIL import Image
     
# Opens a image in RGB mode
im = Image.open(r"..\dataPackage\Image.jpg")
