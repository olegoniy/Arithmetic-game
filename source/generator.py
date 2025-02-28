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
        a, b = 101, random.choice(range(max(self.num_range)//2))
        while a>100 or a == b or a == 0:
            print("new try", a, b, max(self.num_range)//b)
            a = b * random.choice(range(max(self.num_range)//b+1))
        return [f"{a} / {b}", a/b]
    
    def genRandom(self):
        questList = [self.genAdd(), self.genSub(), self.genMult(), self.genDiv()]
        return random.choice(questList)