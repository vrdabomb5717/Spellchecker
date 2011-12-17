
dict_loc = '/usr/share/dict/words'

def read(dict_path):
    """ Read a dictionary located at the path provided. Add each of the words in
    the dictionary to a set that can then be used to provide misspelled 
    words.

    Returns a set with all words in the dictionary.
    """

    f = open(dict_path, 'r)    
    words = {}

    # add each line to our set representing the dictionary
    for line in f:
        word.add(line)

def misspell(words):
    """ Takes a set of words, picks one at random, and generates misspellings.

    Spelling mistakes may include:
        - Case (upper/lower) errors: "inside" => "inSIDE"
        - Repeated letters: "job" => "jjoobbb"
        - Incorrect vowels: "wake" => "weke"

    Returns an English word spelled incorrectly, as a string.
    """

    