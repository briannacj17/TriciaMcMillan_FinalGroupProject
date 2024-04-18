# decryption.py
# Movie name

import json
from cryptography.fernet import Fernet
from pathlib import Path
  
    # Assuming your JSON file is named "data.json"
file_path = "..\\dataPackage\\TeamsAndEncryptedMessagesForDistribution - 002.json"
    
class Movie_encryption():    
        with open(file_path, 'r') as f:
            data = json.load(f)
    
    # Extract specific data
        name = data['Tricia McMillan']
    
    
    # Print the extracted data
        print("Data:", name)



def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    f = Fernet("8viv7QrLsAKgvcV3JsZkKjZwQiinhtPQhUvbS2B14LM=")
    message = encrypted_message.encode('utf-8')
    decrypted_message = f.decrypt(message)

    return(decrypted_message)

def decryptMessage(StringToDecrypt):
    decryptedMessage = decrypt_message(StringToDecrypt)
    return decryptedMessage