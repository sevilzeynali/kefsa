#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import re
import spacy
import textacy
import glob
import os
import textacy.keyterms

ENTRY_DIROCTORY_PATH='/home/zese150/Bureau/test'
OUTPUT_DIRECTORY='/home/zese150/Bureau/res/'

fileIn=glob.glob(ENTRY_DIROCTORY_PATH+"/*")
for f in fileIn:
    with open(f, 'r') as f1:
        print("process of document " +os.path.basename(f))
        read_data = f1.read()
    doc=textacy.Doc(read_data)
    bot = doc.to_bag_of_terms(ngrams=(1, 2), named_entities=True, weighting='count',as_strings=True)
    liste_tuples=sorted(bot.items(), key=lambda x: x[1], reverse=True)[:20]
    print(OUTPUT_DIRECTORY+os.path.basename(f))
    outfile=open(OUTPUT_DIRECTORY+os.path.basename(f),"w")
    for tup in liste_tuples:
        outfile.write(tup[0]+","+str(tup[1])+"\n")
