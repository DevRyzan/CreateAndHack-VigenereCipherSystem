from Models.TurksihAlphabet import TurksihAlphabetProp

def decrypt(ciphertext, key):
    turkish_alphabet = TurksihAlphabetProp().turkish_alphabet
    alphabet_length = len(turkish_alphabet)
    
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char in turkish_alphabet:  # Yalnızca Türk alfabesinde bulunan karakterler için işlem yap
            shift = turkish_alphabet.index(key[key_index % len(key)])
            
            if char.islower():
                decrypted_char = turkish_alphabet[(turkish_alphabet.index(char) - shift) % alphabet_length]
            elif char.isupper():
                decrypted_char = turkish_alphabet[(turkish_alphabet.index(char) - shift) % alphabet_length].upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Türk alfabesinde olmayan karakterler doğrudan eklenir
            plaintext.append(char)

    return ''.join(plaintext)