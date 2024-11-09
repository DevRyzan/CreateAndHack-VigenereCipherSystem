import random
from Models.TurksihAlphabet import TurksihAlphabetProp


turkish_alphabet = TurksihAlphabetProp().turkish_alphabet

def generate_key(length=3):
    return ''.join(random.choice(turkish_alphabet) for _ in range(length))