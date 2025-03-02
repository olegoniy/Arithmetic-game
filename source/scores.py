import os
import json
from prettytable import PrettyTable

class ScoreRecord():
    
    def __init__(self):
        self._scores = {}

    def __str__(self):
        res = PrettyTable()
        res.field_names = ["Player", "Best score"]
        for player in self._scores:
            res.add_row([f"{player}", f"{self._scores[player]}"])
        return res.get_string(sortby="Best score", reversesort=True)
    
    def getScores(self):
        return self._scores
    
    def addPlayer(self, name:str):
        assert name not in self._scores, f"Player {name} is already at a Score board!"
        self._scores[name] = 0

    def changeScore(self, player:str, score:int):
        if player not in self._scores:
            print(f"A new player {player} is being created!")
        self._scores[player] = score

    def importScoreBoard(self, file:str="records.json"):
        assert os.path.isfile(file), f"The file \"{file} \" wasn't found or doesn't exist!"
        with open(file, "r") as scoreBoard:
            self._scores = json.loads(scoreBoard.read())

    def exportScoreBoard(self, file:str="records.json"):
        if not os.path.isfile(file):
            print(f"A new file with name {file} is being created!")
        with open(file, "w") as scoreBoard:
            scoreBoard.write(json.dumps(self._scores))