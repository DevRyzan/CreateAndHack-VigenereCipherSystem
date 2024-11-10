from Hacker.Factory.BruteForce import BruteForce
from Factories.Decryptor import decrypt

class HackerOscarClient:
    def __init__(self, wordlist_path="turkish_wordsList.txt"):
        self.brute_force = BruteForce(wordlist_path)

    def start_decryption(self, encrypted_message):
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