import requests
import pickle
import string
import re


#data file downloaded once, text has been saved through pickle
# the_adventure_of_sherlock_holmes = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
# line_split=the_adventure_of_sherlock_holmes.split('\n')
# modified_sherlock_text=line_split[57:12682]
#
# f = open ('sherlock_texts.pickle', 'wb')
# pickle.dump(modified_sherlock_text,f)
# f.close()

input_file = open('sherlock_texts.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)

sherlock_texts = open('sherlock.text','w')
sherlock_texts.write ('\n'.join (reloaded_copy_of_texts))
sherlock_texts.close()

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('sherlock.text')
