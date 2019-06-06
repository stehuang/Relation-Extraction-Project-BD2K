import nltk, imp
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 

# Scores using medpost parsed verbs:
	# Precision: 0.5531914893617021
	# Recall: 0.15522388059701492

# Scores using nltk parsed verbs:
	# Precision: 0.6046511627906976
	# Recall: 0.23283582089552238

def check_verb(index1, index2, line):
	verbs = []
	m = open("verbs_nltk.txt", "r")
	for line in m:
		verbs.append(line.rstrip('\n'))
	verbs = set(verbs)

	if(index1 < index2):
		start = index1
		end = index2
	else:
		start = index2
		end = index1

	line = line[start:end]
	#print(line + '\n')
	relation = False
	for token in verbs:
		if token in line:
			relation = True
			break
	return relation


# import list of proteins
proteins = []
g = open("proteins.txt", "r")
for line in g:
	proteins.append(line.rstrip('\n'))
proteins = set(proteins)

f = open("passages.txt", "r")
#results = open("interactions.txt", "w")
h = open("co_relations_verbs_nltk.txt", "w")


with open('passages.txt') as myFile:
  text = myFile.read()
corpus = text.split('!')


# create dict of interactions
interactions = dict()
count = 1
document = 1

# process passage by passage
for passage in corpus:
	#results.write('\n' + 'Passage ' + str(document))
	#h.write('\n' + '//' + '\n')
	document += 1
	#results.write(passage + '\n')
	mod_passage = passage.split('\n')
	for line in mod_passage:
		# tokenize sentence
		curr_proteins = []
		protein_index = []
		sentence = wordpunct_tokenize(line)
		# create list of proteins in sentence
		for token in proteins:
	 		if token in line:
	 			curr_proteins.append(token)
		redundant = []
	 	# list interactions by creating every possible pair of 2 proteins
	 	# save as tuple in dictionary
	 	# key: relation #, value: tuple of proteins

	 	# remove proteins that possibly don't exist
		for i in range(len(curr_proteins)):
	 		for j in range(len(curr_proteins)):
	 			if(curr_proteins[i]) in curr_proteins[j] and curr_proteins[i] != curr_proteins[j]:
	 				redundant.append(curr_proteins[i])

		curr_proteins = [x for x in curr_proteins if x not in redundant]
		curr_proteins = sorted(curr_proteins) #arrange tuple in alphabetical order

		# get the index of proteins in the sentence
		protein_index = dict()
		for protein in curr_proteins:
			protein_index[protein] = line.find(protein)
		# for i in range(len(curr_proteins)):
	 # 		for j in range(len(curr_proteins)):
		pairs = list(combinations(curr_proteins, 2))
		for relation in pairs:
			index1 = protein_index[relation[0]]
			index2 = protein_index[relation[1]]
			if check_verb(index1, index2, line) == True:
				relation = tuple(relation)
				print(relation)
				interactions['relation'+str(count)] = relation
			#results.write('relation ' + str(count) +': ' + str(relation) + '\n')
				h.write(str(relation) + '\n')
				count += 1
			
#print(interactions)
print(count)
h.close()
#results.close()





