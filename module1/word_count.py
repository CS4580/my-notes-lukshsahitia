"""Read file from web and do analysis of the data.
"""

import requests

def count_words_from_web(url):

    # Read file from web
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the file: {e}")
        return

    # Count number of words
    words = text.split()
    word_count = len(words)

    return word_count

def main():
    """Driven Function
    """

    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'

    word_count = count_words_from_web(file_address)
    
    print(f"The number of words in the file is: {word_count}")

if __name__ == '__main__':
    main()