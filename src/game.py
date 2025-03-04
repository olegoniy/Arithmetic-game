import time 
import numpy as np

class Game:
    def __init__(self, name):
        self.name = name 
        self.score = 0
        self.time_list = []

    def task_generator(self):
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        operator = np.random.choice(np.array(["+", "-", "*", "//"]))

        if operator == "+":
            ans = a + b
        elif operator == "-":
            ans = a - b
        elif operator == "*":
            ans = a * b
        elif operator == "//":
            ans = a // b

        print(f"{a} {operator} {b} = ")
        start = time.time()
        return ans, start

    def game_over(self, timed):
        self.time_list.append(timed)
        print(f"Your score is: {self.score}")
        print(f"Your average time per question was: {sum(self.time_list) / len(self.time_list)}")

    def run(self):
        while True:
            try:
                ans, start = self.task_generator()
                while True:
                    try:
                        x = int(input("> "))
                        end = time.time()
                        break
                    except ValueError:
                        print("Please enter an integer!")

                timed = end - start

                if timed > 10:
                    print("Too slow!")
                    self.game_over(timed)
                    break
                elif x != ans:
                    print("Wrong!")
                    self.game_over(timed)
                    break
                else:
                    self.time_list.append(timed)
                    self.score += 1

            except KeyboardInterrupt:
                print("Where do you think you are going?")
                

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("Empty name. Please try again!")
        else: 
            self.__name = new_name
 
