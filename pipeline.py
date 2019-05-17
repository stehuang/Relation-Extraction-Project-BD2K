import nltk, imp
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 

# list of proteins stored
proteins = ['protein kinase', 'PrPsc', 'prion protein', 'PrPc']
f = open("sample.txt", "r")
interactions = dict()
count = 1
for line in f:
	# tokenize sentence
	curr_proteins = []
	sentence = wordpunct_tokenize(line)
	# create list of proteins in sentence
	for token in proteins:
 		if token in line:
 			curr_proteins.append(token)

 	# list interactions by creating every possible pair of 2 proteins
 	# save as tuple in dictionary
 	# key: relation #, value: tuple of proteins

	pairs = list(combinations(curr_proteins, 2))
	for relation in pairs:
		relation = tuple(relation)
		interactions['relation'+str(count)] = relation
		count += 1

print(interactions)			





