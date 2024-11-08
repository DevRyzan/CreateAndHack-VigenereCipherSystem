
import sys
sys.path.append('../../src')

def encrypt(plaintext, key):
    ciphertext = []
    key_index = 0
    for char in plaintext:
        if char.isalpha():  
            shift = ord(key[key_index % len(key)]) - ord('a')   
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)  

    return ''.join(ciphertext)



# def encrypt(plaintext, key):
#     ciphertext = []
      
#     key_index = 0
#     for char in plaintext:
#         if char.isalpha():  
#             shift = ord(key[key_index % len(key)]) - ord('a')   
#             if char.islower():
#                 encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#             elif char.isupper():
#                 encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#             ciphertext.append(encrypted_char)
#             key_index += 1
#         else:
#             ciphertext.append(char)  

#     return ''.join(ciphertext)  