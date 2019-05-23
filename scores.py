import bioc, imp
from bioc import BioCXMLWriter, BioCCollection, BioCDocument, BioCPassage, BioCXMLReader
from bioc import BioCAnnotation
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 
from os import curdir, sep
import sys


# read in the two documents
iepa_doc = open("iepa_relations.txt", "r")
co_doc = open("co_relations.txt", "r")

iepa_list = []
co_list = []

# read in every protein and save into list
for line in iepa_doc:
    iepa_list.append(line.strip('\n'))

for line in co_doc:
    co_list.append(line.strip('\n'))

# create dictionary
# key: relation, value: # of times appeared
iepa_relations = dict()
co_relations = dict()

# count individual interactions in lists
for relation in iepa_list:
    if relation in iepa_relations:
        iepa_relations[relation]  += 1
    else:
        iepa_relations[relation] = 1
        #print('added entry')

for relation in co_list:
    if relation in co_relations:
        co_relations[relation]  += 1
    else:
        co_relations[relation] = 1
        #print('added entry')

# get number of actual, retrived, and relevant relations
retrived_relations = len(co_list)
actual_relations = len(iepa_list)
relevant_relations_count = 0
relevant_relations = []
for relation in iepa_relations:
    if relation in co_relations:
        if(co_relations[relation] >= iepa_relations[relation]):
            relevant_relations_count += iepa_relations[relation]
        elif(co_relations[relation] < iepa_relations[relation]):
            relevant_relations_count += co_relations[relation]
            print("less than actual")


print(retrived_relations)
print(actual_relations)
print(relevant_relations)















