from src.algorithm import general
from src.algorithm import const

class ExtendedVigenere:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self, is_binary=False):
        # Preprocess text
        if(is_binary):
            self.text = str(self.text)
        self.text = [(ord(i)) for i in self.text]
                    
        # Preprocess key
        self.key = [(ord(i)) for i in self.key]

    def encrypt(self):
        chiper_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                idx = 0
            chiper_text += chr((char + self.key[idx]) % 256)
            idx += 1

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                idx = 0
            chiper_text += chr((char - self.key[idx]) % 256)
            idx += 1

        return chiper_text