"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
        
    Returns:
        A list of strings containing the words from 
        the document.
    """
    # Using with statement is a good practice of avoiding resource leaks.
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            story_words += line_words
            
        return story_words
            
            
def print_items(items):
    """Print items one per line.
    
    Args:
       items: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)
        
        
# Check if the module is executed as a script.
if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename.
