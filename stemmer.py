import bioc, imp
from bioc import BioCXMLWriter, BioCCollection, BioCDocument, BioCPassage, BioCXMLReader
from bioc import BioCAnnotation
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from itertools import combinations 
from os import curdir, sep
import sys

test_file = "./iepa_bioc.xml"
BIOC_OUT = 'iepa_output.xml'


reader = BioCXMLReader(test_file)
bioc_writer = BioCXMLWriter(BIOC_OUT)
reader.read()
bioc_writer.collection = reader.collection

stemmer = PorterStemmer()
interactions = dict()
count = 1
passage_num = 1

# file to save all text
f = open("passages.txt", "w")
# g = open("proteins.txt", "w")
h = open("interactions_true.txt", "w")

# Get documents to manipulate
documents = bioc_writer.collection.documents
    
# Go through each document
annotation_id = 0
for document in documents:
        
    # Go through each passage of the document
    for passage in document:

    	# create dictionary that maps protein id to protein name
    	proteins = dict()
    	for annotation in passage.annotations:
            proteins[annotation.id] = annotation.text	

        # Stem all the tokens found
    	stems = [stemmer.stem(token) for token in wordpunct_tokenize(passage.text)]

    	h.write('\n' + 'Passage ' + str(passage_num) + '\n')
    	h.write(passage.text + '\n')

        #save passage
    	f.write(passage.text + '!' +'\n')

        # Add an anotation showing the stemmed version, in the given order
    	# for stem in stems:
     #        annotation_id += 1
     #            # For each token an annotation is created, providing
     #            # the surface form of a 'stemmed token'.
     #            # (The annotations are collectively added following
     #            #  a document passage with a <text> tag.)
     #        bioc_annotation = BioCAnnotation()
     #        bioc_annotation.text = stem
     #        bioc_annotation.id = str(annotation_id)
     #        bioc_annotation.put_infon('surface form', 'stemmed token')
     #        passage.add_annotation(bioc_annotation)

        # extract all proteins present in corpus
    	# for relation in passage.relations:
     #    	for node in relation.nodes:
     #    		if(node.refid in proteins.keys()):
     #    			g.write(proteins[node.refid] + '\n')

     	# extract all interactions
    	for relation in passage.relations:
    		curr_proteins = []
    		for node in relation.nodes:
        		if(node.refid in proteins.keys()):
        			curr_proteins.append(proteins[node.refid])
    		if(len(curr_proteins) == 2):
        		pairs = list(combinations(curr_proteins, 2))
        		for relation in pairs:
        			relation = tuple(relation)
        			h.write('relation ' + str(count) +': ' + str(relation) + '\n')
        			count += 1
    	passage_num += 1


f.close()
# g.close()

# Write to disk
bioc_writer.write()


