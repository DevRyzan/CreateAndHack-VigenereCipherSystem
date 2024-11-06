import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Factories')))
from Factories.KeyGenerator import generate_key

class ModelProp:
    _key = None  # Tek bir anahtar olarak saklanacak

    @classmethod
    def get_key(cls, length=10):  # length parametresi eklenmeli
        if cls._key is None:  # Anahtar henüz yoksa oluştur
            cls._key = generate_key(length)  # Anahtar uzunluğunu parametre olarak al
        return cls._key

    @property
    def key(self):
        return self.get_key()  # Property olarak anahtarı döndür