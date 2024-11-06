
import sys
sys.path.append('/Users/rezansoylemez/Desktop/UEMasterProjects/MuhammedRezan_Soylemez/Task1/src')

def encrypt(plaintext, key):
    ciphertext = []
      
    key_index = 0
    for char in plaintext:
        if char.isalpha():  # Sadece harfler şifrelenir
            shift = ord(key[key_index % len(key)]) - ord('a')  # Anahtar harfinin kaydırma miktarı
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)  # Harf olmayan karakterler değişmeden kalır

    return ''.join(ciphertext)  