import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import brown
# sentence = "The good farmer was feeding the poor crow with a bright smile"
# words = word_tokenize(sentence)

# tagged_words = pos_tag(words, tagset= None) # tagset = 'universal'
# for words in tagged_words:
# 	print words 
tagged_sents = brown.tagged_sents()
cp = nltk.RegexpParser(r'''
	NP: 
	{<JJ><N.*>}   
	''')

for sent in tagged_sents[:5]:
	chunked_sent = cp.parse(sent)
	for chunked in chunked_sent.subtrees():
		if chunked.label() == 'NP':
			print chunked
