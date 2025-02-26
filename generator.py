import random
class QuestionGenerator():

    def __init__(self):
        self.num_range = range(1, 100)

    def genAdd(self):
        a, b = random.choice(self.num_range), random.choice(self.num_range)  
        return [f"{a} + {b}", a+b]
    
    def genSub(self):
        a, b = random.choice(self.num_range), random.choice(self.num_range)
        return [f"{a} - {b}", a-b]
    
    def genMult(self):
        a, b = random.choice(self.num_range), random.choice(self.num_range)
        return [f"{a} * {b}", a*b]
    
    def genDiv(self):
        a, b = 101, random.choice(self.num_range)
        while (a > 100):
            a = b * random.choice(self.num_range)
        return [f"{a} / {b}", a/b]
    
        