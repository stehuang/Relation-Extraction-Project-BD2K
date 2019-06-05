import nltk, imp
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords 
from nltk import PorterStemmer



stop_words = set(stopwords.words('english')) 
verbs_ps = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
with open('passages.txt') as myFile:
  text = myFile.read()
corpus = text.split('!')

verbs_nltk = []

h = open("verbs_nltk.txt", "w")

verbs = []
for passage in corpus:
	#results.write('\n' + 'Passage ' + str(document))
	#h.write('\n' + '//' + '\n')
	#results.write(passage + '\n')
	mod_passage = passage.split('\n')
	for line in mod_passage:
		# tokenize sentence
		curr_proteins = []
		protein_index = []
		sentence = wordpunct_tokenize(line)
		sentence = [w for w in sentence if not w in stop_words]
		tagged = nltk.pos_tag(sentence) 
		for word in tagged:
			if(word[1] in verbs_ps):
				verbs.append(word[0])
				h.write(word[0] + '\n')

print(verbs)