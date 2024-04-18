# Python program to read
# json file
 
import json

if __name__ == "__main__":
       
    # Assuming your JSON file is named "data.json"
    file_path = "..\dataPackage\\EncryptedGroupHints Spring 2024 Section 002.json"
    
class Number_Words():    
        with open(file_path, 'r') as f:
            data = json.load(f)
    
    # Extract specific data
        name = data['Tricia McMillan']
    
    
    # Print the extracted data
        print("Data:", name)