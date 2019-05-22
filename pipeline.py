import nltk, imp
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 

# import list of proteins
proteins = []
g = open("proteins.txt", "r")
for line in g:
	proteins.append(line.rstrip('\n'))
proteins = set(proteins)

#f = open("passages.txt", "r")
results = open("interactions.txt", "w")


with open('passages.txt') as myFile:
  text = myFile.read()
corpus = text.split('!')


# create dict of interactions
interactions = dict()
count = 1
document = 1

# process passage by passage
for passage in corpus:
	results.write('\n' + 'Passage ' + str(document))
	document += 1
	results.write(passage + '\n')
	mod_passage = passage.split('\n')
	for line in mod_passage:
		# tokenize sentence
		curr_proteins = []
		sentence = wordpunct_tokenize(line)
		# create list of proteins in sentence
		for token in proteins:
	 		if token in line:
	 			curr_proteins.append(token)
		redundant = []
	 	# list interactions by creating every possible pair of 2 proteins
	 	# save as tuple in dictionary
	 	# key: relation #, value: tuple of proteins
		for i in range(len(curr_proteins)):
	 		for j in range(len(curr_proteins)):
	 			if(curr_proteins[i]) in curr_proteins[j] and curr_proteins[i] != curr_proteins[j]:
	 				redundant.append(curr_proteins[i])
	 				#break

		curr_proteins = [x for x in curr_proteins if x not in redundant]
		pairs = list(combinations(curr_proteins, 2))
		for relation in pairs:
			relation = tuple(relation)
			interactions['relation'+str(count)] = relation
			results.write('relation ' + str(count) +': ' + str(relation) + '\n')
			count += 1


results.close()


