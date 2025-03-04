""" Arithmetic Game
Usage:
    main.py [--name=<name>] [--filename=<filename>] [-h | --help]

Options: 
    -h --help               Show this screen.
    --name=<name>           Name of the player.
    --filename=<filename>   Filename to save statistics (containing inly letters).
"""

from docopt import docopt
from game import *
import json

def main():
    args = docopt(__doc__)

    name = args["--name"]
    try: 
        name = name.strip()
    except AttributeError:
        name = ""

    filename = args["--filename"]
    try: 
        filename = filename.strip()
    except AttributeError:
        filename = ""

    if name:
        game = Game(name)
    else:
        while True:
            try: 
                name = input("Your name: ").strip()
                if name == "":
                    raise ValueError("Name cannot be empty. Try again!")
                else:
                    game = Game(name)
                    break
            except ValueError as e:
                print(e)

    if not filename:
        while True: 
            try: 
                filename = input("Where to store the stats (only letters): ")
                if filename == "":
                    raise ValueError("The filename should not be empty. Please try again!")
                elif filename.isalpha() == False:
                    raise ValueError("The filename should contain only letters. Please try again!")
                else:
                    break
            except ValueError as e: 
                print(e)

    game.run()

    file = filename + ".json"
    try: 
        with open (file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if data == {}:
        data = {game.name: game.score}
    elif (game.name in data.keys() and game.score > data[game.name]) or (game.name not in data.keys()):
        data[game.name] = game.score

    with open(file, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()




        
