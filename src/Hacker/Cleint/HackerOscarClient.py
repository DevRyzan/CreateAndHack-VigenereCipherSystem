import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Hacker.Factory.BruteForceDecryptor import BruteForceDecryptor


# Add the src directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# Import the BruteForceDecryptor class from the Factory directory for decryption purposes
from Hacker.Factory.BruteForceDecryptor import BruteForceDecryptor

class HackerOscarClient:
    def __init__(self):
        self.encrypted_message = None
        self.decrypted_message = None

    def get_input(self):
        self.encrypted_message = input("Please encrypted message: ")
        if not self.encrypted_message:
            # Ensure a valid encrypted message is provided
            print("enter encrypted message.")
            return False
        return True

    def start_decryption(self):
        if not self.get_input():
            return

        # Initialize the decryptor with the encrypted message and a key length limit of 2
        decryptor = BruteForceDecryptor(self.encrypted_message, key_length=2)
        self.decrypted_message = decryptor.brute_force_decrypt()

        # Output the decryption result
        if self.decrypted_message:
            print(f"Decrypted message: {self.decrypted_message}")
        else:
            print("Decryption failed.")

# Main function to initiate the decryption client
if __name__ == "__main__":
    client = HackerOscarClient()
    client.start_decryption()

# class HackerOscarClient:
#     def __init__(self, encrypted_message, max_key_length=3):
#         self.decryptor = BruteForceDecryptor(encrypted_message, max_key_length)
    
#     def attempt_hack(self):
#         print("Starting brute-force decryption...")
#         decrypted_message = self.decryptor.brute_force_decrypt()
        
#         if decrypted_message:
#             print("Decryption successful.")
#         else:
#             print("Failed to decrypt the message.")

# if __name__ == "__main__":
#     encrypted_message = input("Enter the encrypted message: ")
#     hacker = HackerOscarClient(encrypted_message, max_key_length=3)
#     hacker.attempt_hack()