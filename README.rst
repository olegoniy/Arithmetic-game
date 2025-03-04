Hi! This is a Python programm called "Arithmetic Game".
To run it on your computer from terminal you need to first create and then activate the virtual environment:
Note: Here and onwards the sample terminal commands are given for MacOs. Please figure it out yourself if you have another OS. 
$ python3 -m venv ./
$ source bin/activate
Then you need install the required libraries. To do that, run:
$ pip install requirements.rst
After that go to the src directory. You can use the programm by running:
$ python3 main.py
To checkout how to run the programm with docopts:
$ python3 main.py -h
or 
$ python3 main.py --help
If you want to run the tests:
$ pytest
Enjoy!
