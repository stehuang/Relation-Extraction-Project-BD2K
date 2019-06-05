import nltk, imp, textwrap
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 
from ast import literal_eval


char1 = '\''
char2 = ','

h = open("verbs.txt", "x")

f = open("iepa_parse.txt", "r")
for line in f:
	if('verb' in line):
		line = textwrap.dedent(line)
		#line = literal_eval(line)
		h.write(str(line[line.find(char1)+1 : line.find(char2)-1]) + '\n')
