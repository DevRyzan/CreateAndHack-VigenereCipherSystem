import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Models.Model import ModelProp
from Factories.Decryptor import decrypt

class Receiver:
    def __init__(self):
        self.key = ModelProp.get_key()  
        self.received_message = ""   
    def receive_message(self, encrypted_message):

        print("-------Bob Client------")

        self.received_message = encrypted_message
        print(f"Received encrypted message: {self.received_message}")
        decrypted_message = decrypt(self.received_message, self.key)
        print(f"Alice message :  {decrypted_message}")
        
        with open("decryptedtext.txt", "a") as f_plain:f_plain.write(f"-{decrypted_message}\n")

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    receiver = Receiver()
    receiver.receive_message(encrypted_message)