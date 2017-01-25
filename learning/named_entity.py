from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
 
sentence = "Mark and John are working at Google."
 
ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
iob_tag = tree2conlltags(ne_tree)
print iob_tag