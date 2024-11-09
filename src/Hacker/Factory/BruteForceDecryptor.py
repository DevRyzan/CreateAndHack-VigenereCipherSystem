import string
from itertools import product
import os
import requests

class BruteForceDecryptor:
    def __init__(self, encrypted_message, key_length=2, wordlist_url=None):
        self.encrypted_message = encrypted_message
        self.key_length = key_length
        self.alphabet = string.ascii_lowercase

        if wordlist_url:
            self.wordlist = self.load_wordlist_from_github(wordlist_url)
        else:
            wordlist_file = os.path.join(os.path.dirname(__file__), "turkish_wordsList.txt")
            self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        if not os.path.exists(wordlist_file):  
            raise FileNotFoundError(f"Error: {wordlist_file} file not found!")

        try:
            with open(wordlist_file, "r", encoding="utf-8") as file:
                words = set(word.strip().lower() for word in file.readlines()) 
            print(f"Loaded {len(words)} words from wordlist.")
            return words
        except Exception as e:
            print(f"Error wordlist. {e}")
            raise

    def load_wordlist_from_github(self, wordlist_url):
        print(f"Attempting to download wordlist from {wordlist_url}...")
        wordlist = download_wordlist(wordlist_url)
        if wordlist:
            print(f"Loaded {len(wordlist)} words from GitHub wordlist.")
            return set(wordlist)
        else:
            raise Exception("Failed to download GitHub wordlist!")

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

    def simple_stem(self, word):
        suffixes = ["lar", "ler", "dır", "dir", "dan", "den", "ın", "in", "a", "e", "la", "le","m","n","nız","sın","ım","ın"]
        for suffix in sorted(suffixes, key=len, reverse=True):
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word

    def is_valid_decryption(self, decrypted_message):
        words = decrypted_message.lower().split()

        for word in words:
            root_word = self.simple_stem(word) 
            if root_word not in self.wordlist:
                return False  

        return True  
    def brute_force_decrypt(self):
        counter =0

        for length in range(1, self.key_length + 1):
            for key_tuple in product(self.alphabet, repeat=length):
                
                key = ''.join(key_tuple)
                decrypted_message = self.custom_decrypt(self.encrypted_message, key)
                print(f"Trying key '{key}': {decrypted_message} , counter: {counter}")
                
                if self.is_valid_decryption(decrypted_message):
                    print(f"Successful decryption with key '{key}': {decrypted_message}")
                    return decrypted_message
                counter=counter+1
        print("No valid key found within the given key length limit.")
        return None

def download_wordlist(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(f"Error: Failed to fetch wordlist. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None