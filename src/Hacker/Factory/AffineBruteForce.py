from Models.TurksihAlphabet import TurksihAlphabetProp
from math import gcd

class AffineBruteForce:
    def __init__(self, wordlist_path="turkish_wordsList.txt"):
        self.alphabet = TurksihAlphabetProp().turkish_alphabet
        self.alphabet_length = len(self.alphabet)
        self.wordlist = self.load_wordlist(wordlist_path)

    def load_wordlist(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return set(word.strip().lower() for word in file)

    def generate_affine_key_combinations(self):
        # `a` değeri, `alphabet_length` ile aralarında asal olan tüm değerler olabilir.
        possible_a_values = [a for a in range(1, self.alphabet_length) if gcd(a, self.alphabet_length) == 1]
        possible_b_values = range(self.alphabet_length)
        return [(a, b) for a in possible_a_values for b in possible_b_values]

    def affine_decrypt(self, encrypted_message, a, b):
        # `a`'nın modüler tersini hesapla
        try:
            a_inv = pow(a, -1, self.alphabet_length)
        except ValueError:
            return ""  # Eğer `a`'nın modüler tersi yoksa, atla

        decrypted_message = ""
        for char in encrypted_message:
            if char in self.alphabet:
                y = self.alphabet.index(char)
                x = (a_inv * (y - b)) % self.alphabet_length
                decrypted_message += self.alphabet[x]
            else:
                decrypted_message += char  # Alfabenin dışında kalan karakterler doğrudan eklenir

        return decrypted_message

    def is_valid_decryption(self, decrypted_message):
        words_in_message = decrypted_message.lower().split()
        matched_words_count = sum(1 for word in words_in_message if word in self.wordlist)
        return matched_words_count >= 3