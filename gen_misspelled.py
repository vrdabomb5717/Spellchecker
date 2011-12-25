#!/usr/bin/env python
""" Provides load_dict, misspell, generate_case_error, generate_vowel_error,
and generate_repeat_error, functions to load a dictionary and then generate
misspelled words with case errors, vowel errors, and repeated letters.
"""

import argparse
import random
import cStringIO
import sys

__author__ = "Varun Ravishankar"
__copyright__ = "Copyright 2011, Varun Ravishankar"
__license__ = "BSD New"
__version__ = "0.9"
__email__ = "varun.ravishankar@gmail.com"
__status__ = "Development"


def load_dict(dict_path):
    """ Read a dictionary located at the path provided. Add each of the words
    in the dictionary to a set that can then be used to provide misspelled
    words.

    Returns a set with all words in the dictionary.
    """

    words = set({})

    # add each line to our set representing the dictionary
    for line in dict_path:
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

    repeat_case = lambda x: generate_repeat_error(generate_case_error(x))
    repeat_vowel = lambda x: generate_repeat_error(generate_vowel_error(x))
    case_vowel = lambda x: generate_case_error(generate_vowel_error(x))
    repeat_case_vowel = lambda x: generate_repeat_error(case_vowel(x))

    errors = [generate_case_error, generate_vowel_error, generate_repeat_error,
    repeat_case, repeat_vowel, case_vowel, repeat_case_vowel]

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

    output = cStringIO.StringIO()

    for letter in word:
        repeated_letters = random.randint(1, 4)
        for x in xrange(repeated_letters):
            output.write(letter)

    contents = output.getvalue()
    output.close()
    return contents


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate misspelled words \
    with case errors, vowel errors, or repeated letters.', add_help=True,
    version='1.0')

    parser.add_argument('-d', help='location of system dictionary file',
    action="store", dest='dict_loc', type=argparse.FileType('r'),
    default='/usr/share/dict/words')

    parser.add_argument('-c', help='number of misspelled words to generate',
    dest='count', type=int, default=15)

    results = parser.parse_args()

    words = load_dict(results.dict_loc)

    if results.count < 0:
        print >> sys.stderr, "gen_misspelled.py: error: argument -c: invalid \
int value less than 0"

    for x in xrange(results.count):
        print misspell(words)
