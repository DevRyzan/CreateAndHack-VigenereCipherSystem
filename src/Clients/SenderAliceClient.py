import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import subprocess  
from Models.Model import ModelProp
from Factories.Encryptor import encrypt




class SenderAliceClient:
    def __init__(self):
        self.key_value = ModelProp.get_key()
        generated_key = ModelProp.get_key()
        print("-----Alice Client-----")
        self.plaintext = "En güzel yaratıklardan artış isteriz, Böylece güzelliğin gülü asla solmasın, Ama olgunlaştığında zamanla yok olsun,Onun narin varisi hatırasını yaşatsın:Ama sen, yalnızca kendi parlak gözlerine bağlı,Kendi ışığının alevini kendi varlığınla besliyorsun,Bolluğun olduğu yerde kıtlık yaratıyorsun,Kendine tatlı, ama kendine de zalimsin:Sen ki şimdi dünyanın taze süsüsün,Ve gösterişli baharın tek habercisi,Kendi tomurcuğun içinde gömüyorsun mutluluğunu,Ve bencilce tutarak israf ediyorsun:Dünyaya acı, yoksa bu açgözlülük olur,Dünyanın hakkını tüketmek, mezar ve sen tarafından.Kırk kış kaşını kuşattığında,Ve güzelliğinin tarlasına derin hendekler kazdığında,Şimdi gururla bakılan gençlik kıyafetin,Değersiz bir eski püskü ot olacak:O zaman sorulduğunda, tüm güzelliğin nerede,Tüm o enerjik günlerinin hazinesi nerede;Kendi derin çukurlaşmış gözlerinde demek,Tüm yutan bir utanç ve boş bir övgü olurdu."

        # self.plaintext="merhaba Merhaba Akraba Araba"
        
        self.encrypted_message = self.encrypt_message(self.plaintext, self.key_value)
        print(f"Encrypted message: {self.encrypted_message}")
        print(f"Key : {generated_key}")
        print("Encrypted text saved")

        with open("encryptedtext.txt", "a") as f_plain:f_plain.write(f"-{self.encrypted_message}\n")

    def encrypt_message(self, plaintext, key):
        return encrypt(plaintext, key)

if __name__ == "__main__":
    sender = SenderAliceClient()