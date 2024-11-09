class TurksihAlphabetProp:
    _turkish_alphabet = None  

    @classmethod
    def get_turkish_alphabet(cls):
        if cls._turkish_alphabet is None:
            cls._turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'  
        return cls._turkish_alphabet

    @property
    def turkish_alphabet(self):
        return self.get_turkish_alphabet()

model = TurksihAlphabetProp()
