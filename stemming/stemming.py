# stemming : reduces words to their root or base form by chopping off prefixes and suffixes
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "studies", "running"]

stemmed_words = [
    stemmer.stem(word)
    for word in words
]

print(stemmed_words)