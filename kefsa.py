#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import re
import spacy
import textacy
import glob
import os
import time

start_time = time.time()

ENTRY_DIROCTORY_PATH=''
OUTPUT_DIRECTORY=''

fileIn=glob.glob(ENTRY_DIROCTORY_PATH+"/*")
for f in fileIn:
	file= open(f,"r")
	read_data = file.read()
	read_data=read_data.decode('utf8')
	filtre_data = re.sub(r"[^a-zA-Z\s]+|(?:\b[a-zA-Z]{1,3}\b)", "",read_data).lower()
	print "process of document "+os.path.basename(f)
	doc = textacy.TextDoc(filtre_data.strip())
	fout= open(OUTPUT_DIRECTORY+os.path.basename(f),"w")
	bot=doc.as_bag_of_terms(weighting='tfidf', normalized=True, lemmatize='auto', ngram_range=(1, 3),include_nes=True, include_ncs=True, include_kts=False)
	for element in [(doc.spacy_stringstore[term_id], count)for term_id, count in bot.most_common(n=26)]:
		fout.write(str(element)+"\n")
interval = time.time() - start_time
print 'Total time in seconds:', interval		
	#include_nes :if True, include named entities in terms list
	#include_ncs : if True, include noun chunks in terms list
    #include_kts: if True, include key terms in terms list
    #normalized : if True, normalize term freqs by the total number of unique terms
