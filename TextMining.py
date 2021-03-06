import requests
import pickle
import string
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""
data file downloaded once, text has been saved through pickle
text request needs to be be re-pickled when a new user runs the analysis(uncommet from line 11-17 and then run the file, then comment that part again after the text is pickled to user's computer)

the_adventure_of_sherlock_holmes = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
line_split=the_adventure_of_sherlock_holmes.split('\n')
modified_sherlock_text=line_split[57:12682]

f = open ('sherlock_texts.pickle', 'wb')
pickle.dump(modified_sherlock_text,f)
f.close()

"""

input_file = open('sherlock_texts.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file) #reload the pickled file

sherlock_texts = open('sherlock.txt','w') #open a writable text and convert the pickled list to the string
sherlock_texts.write ('\n'.join (reloaded_copy_of_texts))
sherlock_texts.close()

def process_line(line, hist):
    """Remove all the punctuation and whitespace in a line and
    change all words to lowercase to standardize all words
    then count the frequency of the words in a line.
    """
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def process_text(TextFile):
    """place all the frequencies for words into a dictionary.
    then process each line in the text and give an final result of the text.
    """
    hist = dict()
    fp = open(TextFile)
    for line in fp:
        process_line(line, hist)
    return hist

def most_common(hist):
    """with the dictionary we received from the last function,
    'key' represents the frequency of a word.
    Reorder the keys from high frequency to low frequency.
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort()
    t.reverse()
    return t

def total_words(hist):
    """sum up all the values in the dictionary
    """
    return sum(hist.values())

def different_words(hist):
    """the length of hist represents the total number of different words
    because each value is different
    """
    return len(hist)

def random_word(hist):
    t = []
    for word,freq in hist.items():
        t.extend([word])
    return random.choice(t) #pick a random word from the list.



def main():
    hist = process_text('sherlock.txt')
    print('\nThe total number of words in the Sherlock text is', total_words(hist),'.')

    print('\nThe book is consisted of a total number of', different_words(hist), 'different words in this book.')

    t = most_common(hist)
    print('\nThe most common words are:')
    for freq, word in t[:10]: # choosing the top 10 most common words
        print(word, '\t', freq)

    print("\nHere are some random words from the book:")
    for i in range(10):
        print(random_word(hist))


    data = open('sherlock.txt').read().replace('\n', '')
    analyzer = SentimentIntensityAnalyzer()
    print(analyzer.polarity_scores(data)) 


if __name__ == '__main__':
    main()
