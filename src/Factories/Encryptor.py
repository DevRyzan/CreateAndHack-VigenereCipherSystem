from Models.TurksihAlphabet import TurksihAlphabetProp

def encrypt(plaintext, key):
    turkish_alphabet = TurksihAlphabetProp().turkish_alphabet
    alphabet_length = len(turkish_alphabet)
    
    for k in key:
        if k not in turkish_alphabet:
            raise ValueError(f"Key has invalid character: {k}")
    
    ciphertext = []
    key_index = 0
    for char in plaintext:
        if char in turkish_alphabet:  
            shift = turkish_alphabet.index(key[key_index % len(key)])
            
            if char.islower():
                encrypted_char = turkish_alphabet[(turkish_alphabet.index(char) + shift) % alphabet_length]
            elif char.isupper():
                encrypted_char = turkish_alphabet[(turkish_alphabet.index(char.lower()) + shift) % alphabet_length].upper()
            
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)