from Models.TurksihAlphabet import TurksihAlphabetProp

import sys
sys.path.append('../../src')

def encrypt(plaintext, key):
    turkish_alphabet = TurksihAlphabetProp().turkish_alphabet
     
    for k in key:
        if k.lower() not in turkish_alphabet:
            raise ValueError(f"Key has wrong character {k}")
    
    ciphertext = []
    key_index = 0
    for char in plaintext:
        if char.isalpha():   
            shift = turkish_alphabet.index(key[key_index % len(key)].lower())
            
            if char.islower():
                encrypted_char = turkish_alphabet[(turkish_alphabet.index(char) + shift) % len(turkish_alphabet)]
            elif char.isupper():
                encrypted_char = turkish_alphabet[(turkish_alphabet.index(char.lower()) + shift) % len(turkish_alphabet)].upper()
            
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)