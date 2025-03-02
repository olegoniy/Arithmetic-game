import os
import json

class ScoreRecord():
    
    def __init__(self):
        self.scores = {}

    def __str__(self):
        res = ""
        for player in self.scores:
            res += (f"{player} score: {self.scores[player]}\n")
        return res
    
    def addPlayer(self, name:str):
        assert name not in self.scores, f"Player {name} is already at a Score board!"
        self.scores[name] = 0

    def changeScore(self, player:str, score:int):
        self.scores[player] = score

    def importScoreBoard(self, file:str="records.json"):
        assert os.path.isfile(file), f"The file \"{file} \" wasn't found or doesn't exist!"
        with open(file, "r") as scoreBoard:
            self.scores = json.loads(scoreBoard.read())

    def exportScoreBoard(self, file:str="records.json"):
        if not os.path.isfile(file):
            print(f"A new file with name {file} is being created!")
        with open(file, "w") as scoreBoard:
            scoreBoard.write(json.dumps(self.scores))