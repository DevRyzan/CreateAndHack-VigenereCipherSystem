

def decrypt(ciphertext, key):
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():  
            shift = ord(key[key_index % len(key)]) - ord('a')  
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)  

    return ''.join(plaintext)