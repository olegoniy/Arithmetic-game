import pytest
import source.generator as gen

def test_genAdd():
    generator = gen.QuestionGenerator()
    [question, answer] = generator.genAdd()
    a, b = question.split('+')
    assert int(a)+int(b) == answer

def test_genSub():
    generator = gen.QuestionGenerator()
    [question, answer] = generator.genSub()
    a, b = question.split('-')
    assert int(a)-int(b) == answer

def test_genMult():
    generator = gen.QuestionGenerator()
    [question, answer] = generator.genMult()
    a, b = question.split('*')
    assert int(a)*int(b) == answer

def test_genDiv():
    generator = gen.QuestionGenerator()
    [question, answer] = generator.genDiv()
    a, b = question.split('/')
    assert int(a)/int(b) == answer
