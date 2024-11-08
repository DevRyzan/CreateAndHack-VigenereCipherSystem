import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Hacker.Factory.BruteForceDecryptor import BruteForceDecryptor

class HackerOscarClient:
    def __init__(self, encrypted_message, max_key_length=3):
        self.decryptor = BruteForceDecryptor(encrypted_message, max_key_length)
    
    def attempt_hack(self):
        print("Starting brute-force decryption...")
        decrypted_message = self.decryptor.brute_force_decrypt()
        
        if decrypted_message:
            print("Decryption successful.")
        else:
            print("Failed to decrypt the message.")

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    hacker = HackerOscarClient(encrypted_message, max_key_length=3)
    hacker.attempt_hack()