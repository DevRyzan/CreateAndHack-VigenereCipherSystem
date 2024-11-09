import string
from collections import Counter
from Models.TurksihAlphabet import TurksihAlphabetProp

class FrequencyAnalysisDecryptor:
    def __init__(self, encrypted_message, turkish_frequency=None):
        self.encrypted_message = encrypted_message
        self.alphabet =  TurksihAlphabetProp().turkish_alphabet
        
        
        self.turkish_frequency = turkish_frequency or {
            'a': 0.082, 'e': 0.073, 'l': 0.065, 'k': 0.062, 't': 0.060,
            'i': 0.058, 'n': 0.055, 'r': 0.053, 'u': 0.048, 'm': 0.046,
            'b': 0.041, 'v': 0.038, 'y': 0.038, 'c': 0.033, 'o': 0.030,
            's': 0.029, 'd': 0.027, 'p': 0.024, 'g': 0.020, 'h': 0.017,
            'z': 0.015, 'f': 0.012, 'j': 0.008, 'x': 0.006, 'q': 0.004,
            'w': 0.003
        }

    def calculate_frequency(self):
        filtered_message = ''.join(filter(str.isalpha, self.encrypted_message.lower()))
        letter_count = Counter(filtered_message)
        total_letters = sum(letter_count.values())
        frequency = {char: letter_count[char] / total_letters for char in letter_count}
        return frequency

    def match_frequency(self, encrypted_frequency):
        sorted_encrypted = sorted(encrypted_frequency.items(), key=lambda item: item[1], reverse=True)
        sorted_turkish = sorted(self.turkish_frequency.items(), key=lambda item: item[1], reverse=True)
        
        mapping = {}
        for i in range(min(len(sorted_encrypted), len(sorted_turkish))):
            encrypted_letter = sorted_encrypted[i][0]
            turkish_letter = sorted_turkish[i][0]
            mapping[encrypted_letter] = turkish_letter

        return mapping

    def decrypt_message(self, letter_mapping):
        
        decrypted_message = []

        for char in self.encrypted_message:
            if char.lower() in letter_mapping:
                mapped_char = letter_mapping[char.lower()]
                if char.isupper():
                    decrypted_message.append(mapped_char.upper())
                else:
                    decrypted_message.append(mapped_char)
            else:
                decrypted_message.append(char)

        return ''.join(decrypted_message)