import pytest
from source.scores import ScoreRecord as sr
import random
import string

def test_addPlayer():
    a = sr()
    nameCheck=''.join(random.choices(string.ascii_letters + string.digits, k=15))
    a.addPlayer(nameCheck)
    assert nameCheck in a.getScores()

def test_addPlayer_assertion():
    a = sr()
    nameCheck=''.join(random.choices(string.ascii_letters + string.digits, k=15))
    a.addPlayer(nameCheck)
    try:
        a.addPlayer(nameCheck)
        assert False
    except:
        assert True

def test_change_score():
    a = sr()
    nameCheck = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    pointCheck = round(random.randint(0,1000))
    a.changeScore(nameCheck, pointCheck)
    assert int(a.getScores()[nameCheck]) == pointCheck