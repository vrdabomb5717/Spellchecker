import random
import cStringIO


def load_dict(dict_path):
    """ Read a dictionary located at the path provided. Add each of the words
    in the dictionary to a set that can then be used to provide misspelled
    words.

    Returns a set with all words in the dictionary.
    """

    f = open(dict_path, 'r')
    words = set({})

    # add each line to our set representing the dictionary
    for line in f:
        words.add(str.strip(line))

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

    errors = [generate_case_error, generate_vowel_error, generate_repeat_error]

    random_word = random.sample(words, 1)
    mistake_func = random.choice(errors)
    return mistake_func(random_word[0])


def generate_case_error(word):
    """ Takes a string and chooses characters at random to make UPPERCASE, e.g.
    "inside" => "inSIDE"

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


def generate_vowel_error(word):
    """ Takes a string and makes vowels in the string other vowels, at random,
    e.g. "wake" => "weke". NOTE: 'y' is not considered to be a vowel.

    Returns a string with incorrect vowels.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    output = cStringIO.StringIO()

    for letter in word:

        if letter in vowels:
            v = random.choice(vowels)
            output.write(v)
        else:
            output.write(letter)

    contents = output.getvalue()
    output.close()
    return contents


def generate_repeat_error(word):
    """ Takes a string and randomly chooses letters to repeat.
    e.g. "job" => "jjoobbb".

    Returns a string with repeated errors.
    """

    return word


if __name__ == '__main__':
    dict_loc = '/usr/share/dict/words'
    words = load_dict(dict_loc)

    for x in xrange(15):
        print misspell(words)
