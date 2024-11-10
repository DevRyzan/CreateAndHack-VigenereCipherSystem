from Models.TurksihAlphabet import TurksihAlphabetProp
from itertools import product


class BruteForceDecryptor:
    def __init__(self, encrypted_text, wordlist, max_key_length=2):
        self.encrypted_text = encrypted_text
        self.wordlist = set(wordlist)
        self.turkish_alphabet = TurksihAlphabetProp().turkish_alphabet
        self.alphabet_length = len(self.turkish_alphabet)
        self.max_key_length = max_key_length

    def decrypt_with_key(self, key):
        plaintext = []
        key_index = 0
        for char in self.encrypted_text:
            if char.isalpha():
                shift = self.turkish_alphabet.index(key[key_index % len(key)].lower())
                
                if char.islower():
                    decrypted_char = self.turkish_alphabet[(self.turkish_alphabet.index(char) - shift) % self.alphabet_length]
                elif char.isupper():
                    decrypted_char = self.turkish_alphabet[(self.turkish_alphabet.index(char.lower()) - shift) % self.alphabet_length].upper()
                
                plaintext.append(decrypted_char)
                key_index += 1
            else:
                plaintext.append(char)
        return ''.join(plaintext)
    
    def is_meaningful_text(self, text):
        words = text.split()
        meaningful_words = sum(1 for word in words if word.lower() in self.wordlist)
        
        # Çözülen metindeki kelimelerin %40'ı wordlist'te varsa anlamlı kabul edilir
        return meaningful_words >= 0.1 * len(words)

    def brute_force_decrypt(self):
        for key_length in range(1, self.max_key_length + 1):
            for key_tuple in product(self.turkish_alphabet, repeat=key_length):
                key = ''.join(key_tuple)
                decrypted_text = self.decrypt_with_key(key)
                
                if self.is_meaningful_text(decrypted_text):
                    return decrypted_text
        return None