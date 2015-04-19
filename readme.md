About
-----

Takes a text file and gives a list of the highest occuring groups of n words. 

Installation
------------

Install Python 2.7.

How to Run
----------

n-grams.py takes 3 optional arguments:
    filePath - the path of the file to load (default text.txt)
    n - the number of grams (bigram, trigram, etc) (default 2)
    topX - the number of top n-grams to display (default 10)

With default arguments:
    ./n-grams.py

With file path:
    ./n-grams.py -f text.txt

With file path and number of grams:
    ./n-grams.py -f text.txt -n 7

With file path, number of grams and topX:
    ./n-grams.py -f text.txt -n 7 -t 100