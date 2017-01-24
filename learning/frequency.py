import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer as ps
from nltk.corpus import stopwords
from string import punctuation

def run(sentence):
	def normalize(words):
		filtered = [ stemmer.stem(w.lower()) for w in words if w not in stop_words and w not in punctuation]
		return filtered

	stop_words = set(stopwords.words('english'))
	stemmer = ps()
	words = word_tokenize(sentence)
	return normalize(words)

sentence = """ But I must explain to you how all this mistaken idea of
denouncing pleasure and praising pain was born and I will give you a complete
account of the system, and expound the actual teachings of the great explorer
of the truth, the master-builder of human happiness. No one rejects, dislikes,
or avoids pleasure itself, because it is pleasure, but because those who do
not know how to pursue pleasure rationally encounter consequences that are
extremely painful. Nor again is there anyone who loves or pursues or desires
to obtain pain of itself, because it is pain, but because occasionally
circumstances occur in which toil and pain can procure him some great
pleasure. To take a trivial example, which of us ever undertakes laborious
physical exercise, except to obtain some advantage from it? But who has any
right to find fault with a man who chooses to enjoy a pleasure that has no
annoying consequences, or one who avoids a pain that produces no resultant
pleasure? On the other hand, we denounce with righteous indignation and
dislike men who are so beguiled and demoralized by the charms of pleasure of
the moment, so blinded by desire, that they cannot foresee"""

result = run(sentence)
freq =  FreqDist(result)

for term in freq.keys():
	print term + ": "+ str(freq[term])
