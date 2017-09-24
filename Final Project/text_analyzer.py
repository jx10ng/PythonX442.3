"""Question 2: Write a text analyzer. It should be in a form of a function that takes a file name as an argument. 
It should read and analyze a text file and then print:

- the top 5 most frequently used words in the file
- the number of times the top 5 words are used
- should be sorted by most frequently used count
- the longest word in the document
- the average size of each word"""

import re

def analyze_text(text):
    pattern = r'[\w-]+'  
    # Matches only letters and hyphens

    words = re.findall(pattern, text)

    # Create initial counters, variables, etc.
    word_occurances = {}
    word_length_sum = 0
    longest_word_length = 0
    longest_word = ''

    # For loop going through all words
    for word in words:
        if word in word_occurances:
        	# If word already exist, increase count
            word_occurances[word] += 1
        else:
        	# If word does not exist, add initial count
            word_occurances[word] = 0

        word_length = len(word)
        # determine length of individual word

        word_length_sum += word_length
        # increment word length of complete file

        # Determine longest word and length of longest word
        if word_length > longest_word_length:
            longest_word_length = word_length
            longest_word = word

    # Sort word_occurances by the values
    sorted_words = sorted(word_occurances, key=word_occurances.get, reverse=True)

    print('Top 5 words:')
    for word in sorted_words[:5]:
        print('{} - {}'.format(word, word_occurances[word]))
        # Print top 5 words and their number of occurences

    print()  # Blank line
    print('Longest word: {}'.format(longest_word))
    # Print longest word

    print()  # Blank line
    print('Average word size: {}'.format(word_length_sum / len(words)))
    # Print average word size

def main():
    f = open('long_text.txt', 'r')

    text = f.read()

    analyze_text(text)


if __name__ == '__main__':
    main()
