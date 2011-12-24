#!/usr/bin/env python


def load_dict(dict_path):
    """ Read a dictionary located at the path provided. Add each of the words
    in the dictionary to a set that can then be used to provide spelling
    suggestions.

    Returns a dict with all words in the dictionary.
    """

    words = {}

    # add each line to our set representing the dictionary
    for line in dict_path:
        stripped = str.strip(line)
        lower_case = stripped.lower()
        words[lower_case] = stripped

    return words
