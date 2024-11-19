
from Hacker.Factory.BruteForce import BruteForce
from Hacker.Factory.FrequencyAnalysis import FrequencyAnalysis
from Hacker.Factory.AffineBruteForce import AffineBruteForce

from Factories.Decryptor import decrypt

class HackerOscarClient:
    def __init__(self, wordlist_path="turkish_wordsList.txt"):
        self.brute_force = BruteForce(wordlist_path)
        self.frequency_analysis = FrequencyAnalysis(wordlist_path)
        self.affine_brute_force = AffineBruteForce(wordlist_path)

    def start_decryption(self, encrypted_message):
        method = input("Choose decryption method (Polyalphabetic Cipher : 1 / Frequency : 2 / Affine : 3): ").strip().lower()
        if method in ['Polyalphabetic' , '1']:
            self.brute_force_decryption(encrypted_message)
        elif method in ['Frequency' , '2']:
            self.frequency_analysis_decryption(encrypted_message)
        elif method in ['Affine' , '3']:
            self.affine_decryption(encrypted_message)
        else:
            print("Invalid method. Please choose 'brute-force' or 'frequency'.")

    def brute_force_decryption(self, encrypted_message):
        key_length = int(input("Enter the key length to brute-force: "))
        
        print("Brute-forcing...")

        for key_tuple in self.brute_force.generate_key_combinations(key_length):
            key = ''.join(key_tuple)
            decrypted_message = decrypt(encrypted_message, key)
            print(f"Trying key: {key} -> {decrypted_message[:30]}...")

            if self.brute_force.is_valid_decryption(decrypted_message):
                print(f"Key found! The key is: {key}")
                print(f"Decrypted message: {decrypted_message}")
                break
        else:
            print("Failed to decrypt the message with brute-force.")
    def frequency_analysis_decryption(self,         encrypted_message):
        print("Starting frequency analysis...")

        decrypted_message = self.frequency_analysis.decrypt_with_frequency(encrypted_message)
        print(f"Decrypted message with frequency analysis: {decrypted_message[:100]}...")

        if self.frequency_analysis.is_valid_decryption(decrypted_message):
            print("Frequency analysis decryption successful!")
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Failed to decrypt the message with frequency analysis.")

    def affine_decryption(self, encrypted_message):
        print("Affine Cipher brute-forcing...")

        for a, b in self.affine_brute_force.generate_affine_key_combinations():
            decrypted_message = self.affine_brute_force.affine_decrypt(encrypted_message, a, b)
            print(f"Trying keys (a={a}, b={b}) -> {decrypted_message[:30]}...")

            if self.affine_brute_force.is_valid_decryption(decrypted_message):
                print(f"Keys found! a={a}, b={b}")
                print(f"Decrypted message: {decrypted_message}")
                break
        else:
            print("Failed to decrypt the message with affine brute-force.")