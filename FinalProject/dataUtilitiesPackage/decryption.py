# decryption.py
# Name: Brianna Jarrell, Leonie Troeger, Thomas Gilligan
# email: jarrelbc@mail.uc.edu, troegele@mail.uc.edu, gilligtp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4-23-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: To decrypt movie name
# Citations:
# Anything else that's relevant:
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
            print("Decrypted message for", name, ":", decrypted_message)
        else:
            print("No encrypted message found for", name)

# Example usage:
MovieEncryption.decrypt_message_from_file(file_path, 'Tricia McMillan')