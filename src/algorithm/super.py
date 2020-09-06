from src.algorithm import general
from src.algorithm import const
from src.algorithm.vigenere import Vigenere
import math
import numpy as np

def split_len(seq, length):
    matrices = [seq[i:i + length] for i in range(0, len(seq), length)]
    nRow = math.ceil(len(seq)/length)
    lengthLastRow = len(matrices[nRow-1])
    if(lengthLastRow != length):
        for i in range(0,(length-lengthLastRow)):
            matrices[nRow-1].append(-1)
    return matrices

class SuperEncryption:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self):
        # Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.text = [(ord(i)-const.LETTER) for i in text]
                
        # Preprocess key
        key = self.key.lower()
        key = general.sanitize(key)
        self.key = [(ord(i)-const.LETTER) for i in key]

    def encrypt(self):
        chiper_text = ''
        vig = Vigenere(self.text,self.key).encrypt()
        ord_vig = [(ord(i)-const.LETTER) for i in vig]
        matrices = split_len(ord_vig,4)
        print(matrices)
        transpose = np.transpose(matrices)
        print(transpose)
        for row in transpose:
            for col in row:
                if(col != -1):
                    chiper_text += general.order_to_char(col)

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''
        idx = 0
        for char in self.text:
            if(idx >= len(self.key)):
                idx = 0
            chiper_text += chr(((char - self.key[idx]) % 26)+const.LETTER)
            idx += 1

        return chiper_text