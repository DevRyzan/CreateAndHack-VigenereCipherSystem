import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src'))) 
from Hacker.Factory.BruteForceDecryptor import BruteForceDecryptor
from Hacker.Factory.FrequencyAnalysisDecryptor import FrequencyAnalysisDecryptor  

class HackerOscarClient:
    def __init__(self):
        self.encrypted_message = None
        self.decrypted_message = None

    def load_wordlist(self, filepath):
        """Dosyadan kelimeleri okuyup bir wordlist seti olarak döndürür."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                words = file.read().splitlines()  # Satır satır okuyup listeye dönüştürür
            return set(words)  # Hızlı arama için set olarak döndür
        except FileNotFoundError:
            print(f"Wordlist file not found at {filepath}")
            return set()  # Boş set döndür, böylece işlem devam edebilir

    def get_input(self):
        self.encrypted_message = input("Please enter the encrypted message: ")
        if not self.encrypted_message:
            print("You must enter an encrypted message.")
            return False
        return True

    def get_method_choice(self):
        print("\nChoose the decryption method:")
        print("1. Brute Force Decryption")
        print("2. Frequency Analysis Decryption")

        choice = input("Enter 1 or 2: ")
        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            return self.get_method_choice()
        
        return int(choice)

    def start_decryption(self):
        """Start the decryption process based on user input."""
        if not self.get_input():
            return

        method_choice = self.get_method_choice()

        if method_choice == 1:
            wordlist_file = os.path.join(os.path.dirname(__file__), "turkish_wordsList.txt")
            self.wordlist = self.load_wordlist(wordlist_file)
        
            # Brute Force Decryption
            print("\nStarting brute force decryption...")

            decryptor = BruteForceDecryptor(self.encrypted_message, self.wordlist, max_key_length=2)
            self.decrypted_message = decryptor.brute_force_decrypt()

        elif method_choice == 2:
            # Frequency Analysis Decryption
            print("\nStarting frequency analysis decryption...")
            decryptor = FrequencyAnalysisDecryptor(self.encrypted_message)  # Assuming class exists
            
            # Calculate the frequency of letters in the encrypted message
            encrypted_frequency = decryptor.calculate_frequency()
            
            # Match frequencies between encrypted message and Turkish letter frequency
            letter_mapping = decryptor.match_frequency(encrypted_frequency)
            
            # Decrypt the message using the mapped letters
            self.decrypted_message = decryptor.decrypt_message(letter_mapping)

        # Output the decryption result
        if self.decrypted_message:
            print(f"\nDecrypted message: {self.decrypted_message}")
        else:
            print("Decryption failed.")