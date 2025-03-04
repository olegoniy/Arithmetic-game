'''Arithmania

Usage:
    main.py [--Player=<Nickname>] [--File=<Path>]
    main.py (-r|--records) [--File=<Path>]
    main.py (-h|--help)
    

Options:
    -h --help               Show instructions
    --Player=<Nickname>     Start game as <Nickname>
    --File=<Path>           Use <Path> as records file

'''

from game import Game
from scores import ScoreRecord as SRec
from docopt import docopt
import pathvalidate as pv



def setUp(cnst):
    args = docopt(__doc__, version="Arithmania 0.0.69")
    if args["--File"] == None:
        cnst["STATS_FILE"] = input("Please enter a path to the stats file, you'd like to work with (if it doesn't exist, a new one will be created):")
    else:
        cnst["STATS_FILE"] = args["--File"]
    if cnst["STATS_FILE"] == "":
        cnst["STATS_FILE"] = "records.json"
    while not pv.is_valid_filepath(cnst["STATS_FILE"]):
        cnst["STATS_FILE"] = input("\nPath you entered isn't valid, please enter valid one:")
    if args["--records"] or args["-r"]:
        cnst["MODE"] = "Display"
    else:  
        cnst["MODE"] = "Game"
        if args["--Player"] == None:
            cnst["PLAYER"] = input("\nWhat is your Nickname?:")
        else:
            cnst["PLAYER"] = args["--Player"]
    #print(args)
    

if __name__ == "__main__":
    cnst={
        "STATS_FILE":"",
        "MODE":"",
        "PLAYER":""
    }
    setUp(cnst)
    print(cnst)
    if cnst["MODE"] == "Display":
        table = SRec()
        if not table.importScoreBoard(file=cnst["STATS_FILE"]):
            table.exportScoreBoard(file=cnst["STATS_FILE"])
        print(table)
    else:
        
        game = Game(player=cnst["PLAYER"], path=cnst["STATS_FILE"])
        game.start()
    
    input("\n Press ENTER to exit...\n")