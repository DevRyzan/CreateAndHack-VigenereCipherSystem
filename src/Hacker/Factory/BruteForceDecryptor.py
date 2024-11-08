import string
from itertools import product

class BruteForceDecryptor:
    def __init__(self, encrypted_message, max_key_length=3):
        self.encrypted_message = encrypted_message
        self.max_key_length = max_key_length
        self.alphabet = string.ascii_lowercase  

    def custom_decrypt(self, ciphertext, key):
        decrypted_text = []
        key_index = 0

        for char in ciphertext:
            if char.isalpha(): 
                shift = ord(key[key_index % len(key)]) - ord('a')  
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                elif char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted_text.append(decrypted_char)
                key_index += 1
            else:
                decrypted_text.append(char) 

        return ''.join(decrypted_text)

    def brute_force_decrypt(self):
        for length in range(1, self.max_key_length + 1):
            for key_tuple in product(self.alphabet, repeat=length):
                key = ''.join(key_tuple)
                decrypted_message = self.custom_decrypt(self.encrypted_message, key)
                
                print(f"Trying key '{key}': {decrypted_message}")
                
                if self.is_valid_decryption(decrypted_message):
                    print(f"Successful decryption with key '{key}': {decrypted_message}")
                    return decrypted_message
        
        print("No valid key found within the given key length limit.")
        return None

    def is_valid_decryption(self, decrypted_message):
        return ' ' in decrypted_message 