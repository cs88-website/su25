########################################################################################
# BEGIN [Demo00]
########################################################################################
# [Demo00] Intent: a simple demo of:
# (1) opening up VSCode
# (2) opening up a terminal within VSCode
# (3) entering a Python interpreter (via `python3.11`)
# (4) demo some simple Python expressions
# (5) Shakespeare: demo complicated Python expressions as a "fun preview" of things to come.

# Numeric expressions
2025
2000 + 25
10 * 2
# Note: `**` means "to the power"
10 ** 2
# Note: `//` means "floor division"
5 / 2
5 // 2
1 + 2 ** 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)

# Values
# We can represent text with something called a string
"Go Bears"

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
# shakespeare.txt contains (all of?) the works of Shakespeare.
# Each text file line is a line from one of his works.
shakes = open('shakespeare.txt')
# read the file and split by spaces/newlines, generating a list of words
text = shakes.read().split()
# number of words
len(text)
# first 25 words
text[:25]
# (for fun) let's preprocess the text to remove punctuation, and normalize text (all lowercase)
import string
# fortunately Python contains a constant containing all punctuation characters
string.punctuation
text_no_punctuation = [word for word in text if word not in string.punctuation]
# compare with punctuation vs no punctuation
text_no_punctuation[:25]
text[:25]

text_all_lowercase = [word.lower() for word in text_no_punctuation]
# compare orig case vs lower case'd
text_all_lowercase[:25]
text_no_punctuation[:25]

# rewrite `text` variable (for convenience)
text = text_all_lowercase
text[:25]

# count the number of times 'the' occurs in Shakespeare
text.count('the')
text.count('The')  # sanity check that lowercasing worked (should be 0)
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
# Question: how many unique words are there?
all_unique_words = set(text)
len(all_unique_words)

# Combinations 
'draw'
'draw'[0]
# "Grab the first letter from each unique word"
{w[0] for w in all_unique_words}

# Data
'draw'[::-1]
# Question: can you guess what these expressions do?
# (Can ask students to answer each one. Fun way to demonstrate how human-readable Python can be)
# Answer: get all palindromes that are longer than 4 letters
{w for w in all_unique_words if w == w[::-1] and len(w) > 4}
# Answer: get all 4-letter words whose reverse'd word also occurs in Shakespheare
{w for w in all_unique_words if w[::-1] in all_unique_words and len(w) == 4}
# Answer: get all >6 letter words whose reverse'd word also occurs in Shakespheare
{w for w in all_unique_words if w[::-1] in all_unique_words and len(w) >= 6}
########################################################################################
# END [Demo00]
########################################################################################
