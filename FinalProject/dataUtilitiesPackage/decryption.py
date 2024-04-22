# decryption.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan, Deonta Williams
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu, willi6d3@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: To decrypt movie name
# Citations: https://stackoverflow.com/questions/67283961/decrypt-message-with-cryptography-fernet-do-not-work
# Anything else that's relevant:

"""
this python file imports json, cryptography, and path libraries to
open a json file.The key is cracked then used to loop through the json file 
to decrypt the name.
"""

import json
from cryptography.fernet import Fernet
from pathlib import Path
  
    # Assuming your JSON file is named "data.json"
file_path = "..\\dataPackage\\TeamsAndEncryptedMessagesForDistribution - 002.json"

class MovieEncryption:
    @staticmethod
    def decrypt_message(encrypted_message):
        """
        Decrypts an encrypted message
        """
        f = Fernet("8viv7QrLsAKgvcV3JsZkKjZwQiinhtPQhUvbS2B14LM=")
        message = encrypted_message.encode('utf-8')
        decrypted_message = f.decrypt(message)
        return decrypted_message.decode('utf-8')

    @staticmethod
    def decrypt_message_from_file(file_path, name):
        with open(file_path, 'r') as f:
            data = json.load(f)
        encrypted_message = data.get(name)
        if encrypted_message:
            decrypted_message = MovieEncryption.decrypt_message(encrypted_message[0])
            print("The movie name for", name, ":", decrypted_message)
        else:
            print("No encrypted message found for", name)
