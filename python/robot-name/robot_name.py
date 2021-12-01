import random
import string

class Robot:
    def __init__(self):
        letters = ''.join(random.choice(string.ascii_uppercase) for x in range(2))
        numbers = ''.join(str(random.randint(100, 999)))
        self.name = ''.join((letters, numbers)) 

    def reset(self):
        random.seed(4)
        letters = ''.join(random.choice(string.ascii_uppercase) for x in range(2))
        numbers = ''.join(str(random.randint(100, 999)))
        self.name = ''.join((letters, numbers)) 

