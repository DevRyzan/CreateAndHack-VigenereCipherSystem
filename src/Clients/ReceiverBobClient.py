import sys
import os
sys.path.append('/Users/rezansoylemez/Desktop/UEMasterProjects/MuhammedRezan_Soylemez/Task1/src')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Factories')))
from Models.Model import ModelProp
from Factories.Decryptor import decrypt

class Receiver:
    def __init__(self):
        self.key = ModelProp.get_key()  # Model sınıfından anahtarı al
        self.received_message = ""  # Gelen mesaj burada tutulacak

    def receive_message(self, encrypted_message):
        """Gelen şifreli mesajı çözmek için kullanılır"""
        self.received_message = encrypted_message
        print(f"Received encrypted message: {self.received_message}")
        decrypted_message = decrypt(self.received_message, self.key)
        print(f"Decrypted message: {decrypted_message}")

# Ana çalışma bloğu
if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    receiver = Receiver()
    receiver.receive_message(encrypted_message)