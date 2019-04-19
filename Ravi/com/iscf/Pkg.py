#!/usr/sbin/env python3

"""Retrieves and prints words from a URL

usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch the list of words from a URL

    Args:
        url: the URL of a UTF-8 text tocument

    Returns:
        A list of strings containing the words of the story
    
    """

    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('UTF-8').split()
            for word in line_words:
                story_words.append(word)

def print_items(items):
    """print items one per line

    Args
        An iterable sequence of print items

    """

    for item in items:
        print(item)



def main(url):
    """ Print each word from a text document from a URL

    Args:
        The URL of a UETF-8 text document
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
