# Arithmania

It is a small console-based game using Python in an object oriented approach to learn general skills of a programm development.

## Rules of the game

A player will be presented with elementary arithmatic questions. A player has 10 seconds to give an answer. Otherwise the game will be over and players result will be displayed.

## Scores 

All the scores will be saved locally on your machine in a file the player gives or in a standart one called ```records.json``` 

## Installation

At first copy this repository to your machine.
In order for the progam to work you'll have to install some libraries. All of them are listed in a file ```requirements.rst```. For that create a python enviroment in folder of the project by running 
```bash
$ python3 -m venv
```
After that you'd want to activate it by typing:
```bash
$ source bin/activate
```
finally to install the libraries run:
```bash
$ pip install -r requirements.rst
```