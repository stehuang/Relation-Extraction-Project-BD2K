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

# get list of actual, retreived, and relevant relations
retrieved = len(co_list)
actual = len(iepa_list)
relevant_relations_count = 0
relevant = []
# get list of relevant & actual relations from retrieved
# for every relation in iepa, if the relation has been retrieved, then add the relation to the list
for relation in iepa_relations:
    if relation in co_relations:
        if(co_relations[relation] >= iepa_relations[relation]):
            relevant_relations_count += iepa_relations[relation]
            for count in range(iepa_relations[relation]):
                relevant.append(relation)
        elif(co_relations[relation] < iepa_relations[relation]):
            relevant_relations_count += co_relations[relation]
            for count in range(co_relations[relation]):
                relevant.append(relation)

relevant = len(relevant)
print(retrieved)
print(actual)
print(relevant)

# precision is the fraction of retrieved documents that are relevant to the query
precision = (relevant)/(retrieved)

#recall is the fraction of the relevant documents that are successfully retrieved
recall = (relevant)/(actual)

print("Precision: " + str(precision))
print("Recall: " + str(recall))
















