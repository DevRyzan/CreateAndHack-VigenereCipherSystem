import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import subprocess  
from Models.Model import ModelProp
from Factories.Encryptor import encrypt




class SenderAliceClient:
    def __init__(self):
        self.key_value = ModelProp.get_key()
        generated_key = ModelProp.get_key()
        print("-----Alice Client-----")
        self.plaintext = input("Alice: ")
        
        self.encrypted_message = self.encrypt_message(self.plaintext, self.key_value)
        print(f"Encrypted message: {self.encrypted_message}")
        print(f"Key : {generated_key}")
    def encrypt_message(self, plaintext, key):
        return encrypt(plaintext, key)

if __name__ == "__main__":
    sender = SenderAliceClient()