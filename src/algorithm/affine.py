from src.algorithm import general
import math 

# X that satisfy aX = 1 mod m
def mod_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

class Affine:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def preprocess(self):
        # Preprocess text
        text = self.text.lower()
        text = general.sanitize(text)
        self.text = text

        # Preprocess key
        try:
            self.m = int(self.key['m'])
            self.b = int(self.key['b'])
        except ValueError as err:
            raise Exception("key is not integer", 400)

        self.n = 26
        if math.gcd(self.m, self.n) != 1:        
            raise Exception(f"{self.m} and {self.n} are not relatively prime", 400)

    def encrypt(self):
        chiper_text = ''
        for char in self.text:
            chiper_char = self.m * general.char_to_order(char) + self.b 
            chiper_text += general.order_to_char(chiper_char)

        return chiper_text
  
    def decrypt(self):
        chiper_text = ''
        for char in self.text:
            m_inverse = mod_inverse(self.m, self.n)
            chiper_char = m_inverse * (general.char_to_order(char) - self.b )
            chiper_text += general.order_to_char(chiper_char)

        return chiper_text