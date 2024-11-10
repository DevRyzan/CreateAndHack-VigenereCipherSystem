from collections import Counter
from Models.TurksihAlphabet import TurksihAlphabetProp

class FrequencyAnalysis:
    def __init__(self, wordlist_path="turkish_wordsList.txt"):
        self.alphabet = TurksihAlphabetProp().turkish_alphabet
        self.wordlist = self.load_wordlist(wordlist_path)
        
        self.turkish_frequency_order = "aeinrlktmusoüybdçgöşzfğhj"

        self.turkish_bigram_order = ["en", "ar", "an", "ve", "de", "ta", "in", "ya", "la", "ri"]

    def load_wordlist(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return set(word.strip().lower() for word in file)

    def analyze_frequency(self, encrypted_message):
        counter = Counter(encrypted_message.lower())  
        most_common_chars = [char for char, _ in counter.most_common() if char in self.alphabet]
        return most_common_chars

    def map_frequency(self, encrypted_message):
        most_common_chars = self.analyze_frequency(encrypted_message)
        
        char_map = {}
        for i, char in enumerate(most_common_chars):
            if i < len(self.turkish_frequency_order):
                mapped_char = self.turkish_frequency_order[i]
                char_map[char] = mapped_char
                char_map[char.upper()] = mapped_char.upper()  

        bigrams = Counter(encrypted_message[i:i+2].lower() for i in range(len(encrypted_message) - 1) if encrypted_message[i:i+2].lower() in self.alphabet)
        most_common_bigrams = [bigram for bigram, _ in bigrams.most_common()]
        
        for i, bigram in enumerate(most_common_bigrams):
            if i < len(self.turkish_bigram_order):
                mapped_bigram = self.turkish_bigram_order[i]
                char_map[bigram] = mapped_bigram
                char_map[bigram.upper()] = mapped_bigram.upper()  # Büyük harf versiyonunu ekliyoruz

        return char_map

    def decrypt_with_frequency(self, encrypted_message):
        char_map = self.map_frequency(encrypted_message)
        
        decrypted_message = ""
        skip_next = False
        for i, char in enumerate(encrypted_message):
            if skip_next:
                skip_next = False
                continue

            # İkili harf kontrolü
            if i < len(encrypted_message) - 1 and encrypted_message[i:i+2].lower() in char_map:
                bigram = encrypted_message[i:i+2]
                decrypted_message += char_map[bigram.lower()].upper() if bigram.isupper() else char_map[bigram.lower()]
                skip_next = True
            elif char.lower() in char_map:
                decrypted_message += char_map[char.lower()].upper() if char.isupper() else char_map[char.lower()]
            else:
                decrypted_message += char
        
        return decrypted_message

    def is_valid_decryption(self, decrypted_message):
        words_in_message = decrypted_message.lower().split()
        matched_words_count = sum(1 for word in words_in_message if word in self.wordlist)
        return matched_words_count >= 3