from Models.TurksihAlphabet import TurksihAlphabetProp


def decrypt(ciphertext, key):
    # Türk alfabesindeki harfler
    turkish_alphabet = TurksihAlphabetProp().turkish_alphabet
    
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():  
            shift = turkish_alphabet.index(key[key_index % len(key)].lower())
            
            if char.islower():
                decrypted_char = turkish_alphabet[(turkish_alphabet.index(char) - shift) % len(turkish_alphabet)]
            elif char.isupper():
                decrypted_char = turkish_alphabet[(turkish_alphabet.index(char.lower()) - shift) % len(turkish_alphabet)].upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)

    return ''.join(plaintext)