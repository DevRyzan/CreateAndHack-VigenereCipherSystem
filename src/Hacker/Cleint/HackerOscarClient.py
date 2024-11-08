import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Hacker.Factory.BruteForceDecryptor import BruteForceDecryptor




class HackerOscarClient:
    def __init__(self):
        self.encrypted_message = None
        self.decrypted_message = None

    def get_input(self):
        """Kullanıcıdan şifreli mesajı al"""
        self.encrypted_message = input("Lütfen şifreli metni girin: ")
        if not self.encrypted_message:
            print("Geçerli bir şifreli metin girin.")
            return False
        return True

    def start_decryption(self):
        """Şifre çözme işlemini başlatır"""
        if not self.get_input():
            return

        decryptor = BruteForceDecryptor(self.encrypted_message, key_length=2)
        self.decrypted_message = decryptor.brute_force_decrypt()

        if self.decrypted_message:
            print(f"Çözülmüş mesaj: {self.decrypted_message}")
        else:
            print("Şifre çözme işlemi başarısız oldu.")

# Ana işlevi başlatan kod:
if __name__ == "__main__":
    client = Client()
    client.start_decryption()


# class HackerOscarClient:
#     def __init__(self, encrypted_message, max_key_length=3):
#         self.decryptor = BruteForceDecryptor(encrypted_message, max_key_length)
    
#     def attempt_hack(self):
#         print("Starting brute-force decryption...")
#         decrypted_message = self.decryptor.brute_force_decrypt()
        
#         if decrypted_message:
#             print("Decryption successful.")
#         else:
#             print("Failed to decrypt the message.")

# if __name__ == "__main__":
#     encrypted_message = input("Enter the encrypted message: ")
#     hacker = HackerOscarClient(encrypted_message, max_key_length=3)
#     hacker.attempt_hack()