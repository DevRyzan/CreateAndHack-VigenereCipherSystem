# Decryptor.py
from Factories.KeyGenerator import generate_key

def decrypt(ciphertext, key):
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():  # Sadece harfler şifresini çözer
            shift = ord(key[key_index % len(key)]) - ord('a')  # Anahtar harfinin kaydırma miktarı
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)  # Harf olmayan karakterler değişmeden kalır

    return ''.join(plaintext)