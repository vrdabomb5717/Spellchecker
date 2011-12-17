import random
import cStringIO


def load_dict(dict_path):
    """ Read a dictionary located at the path provided. Add each of the words
    in the dictionary to a set that can then be used to provide misspelled
    words.

    Returns a set with all words in the dictionary.
    """

    f = open(dict_path, 'r')
    words = {}

    # add each line to our set representing the dictionary
    for line in f:
        words.add(line)

    return words


def misspell(words):
    """ Takes a set of words, picks one at random, and generates misspellings.

    Spelling mistakes may include:
        - Case (upper/lower) errors: "inside" => "inSIDE"
        - Repeated letters: "job" => "jjoobbb"
        - Incorrect vowels: "wake" => "weke"

    This method should not modify the set. It pops an element from the set
    to get one at random, but this element is then re-added right away.

    Returns an English word spelled incorrectly, as a string.
    """

    random_word = words.pop()
    words.add(random_word)


def generate_case_error(word):
    """ Takes a string and chooses characters at random to make UPPERCASE.

    Returns a string with a case error in it.
    """
    output = cStringIO.StringIO()
    choices = [str.lower, str.upper]

    for letter in word:
        f = random.choice(choices)
        output.write(f(letter))

    contents = output.getvalue()
    output.close()
    return contents


dict_loc = '/usr/share/dict/words'
words = load_dict(dict_loc)
