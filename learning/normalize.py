from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.stem.porter import PorterStemmer as ps
def run():
	def normalize(words):
		filtered = [ stemmer.stem(w.lower()) for w in words if w not in stop_words and w not in punctuation]
		return filtered

	sentence = """This is one of the fastest cars. I will drive it to the extreme. Here, I come"""
	stop_words = set(stopwords.words('english'))
	stemmer = ps()
	words = word_tokenize(sentence)
	return normalize(words)


print run()