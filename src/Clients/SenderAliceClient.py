import sys
import os
sys.path.append('/Users/rezansoylemez/Desktop/UEMasterProjects/MuhammedRezan_Soylemez/Task1/src')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Factories')))
import subprocess  
from Models.Model import ModelProp
from Factories.Encryptor import encrypt




class SenderAliceClient:
    def __init__(self):
        # Model'den key alınır
        self.key_value = ModelProp.get_key()
        
        # Kullanıcıdan plaintext alınır
        self.plaintext = input("Enter the plaintext to encrypt: ")
        
        # Mesajı şifrele ve sonucu yazdır
        self.encrypted_message = self.encrypt_message(self.plaintext, self.key_value)
        print(f"Encrypted message: {self.encrypted_message}")

    def encrypt_message(self, plaintext, key):
        """Verilen metni ve anahtarı kullanarak şifreler."""
        return encrypt(plaintext, key)

if __name__ == "__main__":
    sender = SenderAliceClient()