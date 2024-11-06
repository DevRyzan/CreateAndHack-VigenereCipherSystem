import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Factories')))
from Factories.KeyGenerator import generate_key

class ModelProp:
    _key = None   

    @classmethod
    def get_key(cls, length=10):  

        if cls._key is None:   
            cls._key = generate_key(length)   
        return cls._key

    @property
    def key(self):
        return self.get_key()   