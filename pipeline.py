import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer

proteins = ['protein kinase', 'PrPsc', 'prion protein', 'PrPc']
f = open("sample.txt", "r")
for line in f:
 	sentence = wordpunct_tokenize(line)
 	print(sentence)
 	for token in proteins:
 		if token in line:
 			print(token)





