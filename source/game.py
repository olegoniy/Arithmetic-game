from generator import QuestionGenerator as QGen
from scores import ScoreRecord as SRec
import time


class Game():
    
    def _timer(func):
        def wrapper(self):
            start = time.time()
            func(self)
            end  = time.time()
            return end-start
        return wrapper

    def __init__(self, player:str=None, path:str="records.json"):
        self._player = player
        self._path = path

        self._current = 0

        self._qgen = QGen()
        
        self._records = SRec()
        self._records.importScoreBoard(self._path)

        self._gameOver = False

    @_timer
    def _question(self):
            [question, answer] = self._qgen.genRandom()
            print(f"What is {question} ?")
            userAns = input("Your answer: ")
            while not userAns.replace('-', '').isnumeric():
                print(f"\n{self._player}, your number should be an integer!\n")
                userAns = input("Your answer: ")
            if int(userAns) != answer:
                self._gameOver = True
                print(f"\nHoly Linus! The answer you gave is preposterously wrong!\n The correct answer is {answer}\n")
    
    @_timer
    def _quiz(self):
        cnt = 1
        while not self._gameOver:
            print(f"\nQuestion number {cnt}:")
            cnt += 1
            time = self._question()
            if time > 10:
                self._gameOver = True
                print(f"\nDear {self._player}, I hate to tell you, but at the moment your brain operates like windows vista - ridiculously slow!\n")
        self._current = cnt-2


    def start(self):
        overall_time = self._quiz()
        if not self._player in self._records.getScores():
            self._records.addPlayer(self._player)
        if self._current == 0:
            print(f"\n{self._player}, well your score is 0, so... That's it\n")
        else:
            if self._current > self._records.getScores()[self._player]:
                self._records.changeScore(self._player, self._current)
                self._records.exportScoreBoard(self._path)
                print("You did have outdone yourself, mate! Frankly, you made it seem too easy...\n")
                print(f"For this game you've gained {self._current} stunning points\n")
                print(f"Your average time per question is: {round(overall_time/self._current, 2)} seconds\n")
                print(f"You have to be pround of yourself, {self._player}\n")
            else:
                print("Well, it isn't that you are stupid, but rather our world is too complicated\n")
                print(f"Number of points you struggled for: {self._current}\n")
                print(f"Your average time per question is:{round(overall_time/self._current, 2)}... Why in the world did it take you so long?!\n")
                print(f"Don't worry, maybe next time you will study for the test, {self._player}")



