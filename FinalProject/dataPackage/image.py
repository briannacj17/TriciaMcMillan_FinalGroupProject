#image.py 
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: To show and store group photo
# Citations:
# Anything else that's relevant:

    # open an image file. The default path is where this python module is
  #  im = Image.open("../image_Package/and_name.jpg") # Image manipulation class
   # im.show()
    #save_image(im, "../image_Package/and_name.jpg")

# Importing Image class from PIL module
from PIL import Image
     
# Opens a image in RGB mode
im = Image.open(r"..\dataPackage\Image.jpg")
     
# Shows the image in image viewer
im.show()