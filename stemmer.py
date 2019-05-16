import bioc, imp
from bioc import BioCXMLWriter, BioCCollection, BioCDocument, BioCPassage, BioCXMLReader
from bioc import BioCAnnotation
from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer
from os import curdir, sep
import sys

test_file = "./iepa_bioc.xml"
BIOC_OUT = 'iepa_output.xml'

# write proteins to file
f = open("relations.txt","x")


reader = BioCXMLReader(test_file)
bioc_writer = BioCXMLWriter(BIOC_OUT)
reader.read()
bioc_writer.collection = reader.collection

stemmer = PorterStemmer()

# Get documents to manipulate
documents = bioc_writer.collection.documents
    
# Go through each document
annotation_id = 0
for document in documents[0:0]:
        
    # Go through each passage of the document
    for passage in document:
        #  Stem all the tokens found
        stems = [stemmer.stem(token) for token in wordpunct_tokenize(passage.text)]
            # Add an anotation showing the stemmed version, in the given order
        for stem in stems:
            annotation_id += 1
                # For each token an annotation is created, providing
                # the surface form of a 'stemmed token'.
                # (The annotations are collectively added following
                #  a document passage with a <text> tag.)
            bioc_annotation = BioCAnnotation()
            bioc_annotation.text = stem
            bioc_annotation.id = str(annotation_id)
            bioc_annotation.put_infon('surface form', 'stemmed token')
            passage.add_annotation(bioc_annotation)


# Print file to screen w/o trailing newline
# (Can be redirected into a file, e. g output_bioc.xml)
sys.stdout.write(str(bioc_writer))
    
# Write to disk
bioc_writer.write()










# with open(test_file, 'r') as fp:
#     collection = bioc.load(fp)


