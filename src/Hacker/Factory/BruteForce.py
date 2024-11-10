import itertools
from Models.TurksihAlphabet import TurksihAlphabetProp

class BruteForce:
    def __init__(self, wordlist_path="turkish_wordsList.txt"):
        self.alphabet = TurksihAlphabetProp().turkish_alphabet
        self.wordlist = self.load_wordlist(wordlist_path)

    def load_wordlist(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return set(word.strip().lower() for word in file)

    def generate_key_combinations(self, length):
        return itertools.product(self.alphabet, repeat=length)

    def is_valid_decryption(self, decrypted_message):
        words_in_message = decrypted_message.lower().split()
        
        matched_words_count = sum(1 for word in words_in_message if word in self.wordlist)
        return matched_words_count >= 3