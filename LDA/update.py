from urllib2 import *
from solr import *
import urllib2
import logging
import simplejson
from stemming.porter2 import stem
logging.basicConfig(format=' %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities


lda = models.ldamodel.LdaModel.load('/tmp/try_lda_saver')
#lda = models.ldamodel.LdaModel.load('/tmp/try_lsi_saver')
documents = [line.strip() for line in open("output_lda.txt", 'r')]
doc_ids = [line.strip() for line in open("output_lda_ids.txt", 'r')]

#query similarity

index = similarities.MatrixSimilarity.load('/tmp/deerwester1.index')

dictionary=corpora.Dictionary.load('/tmp/deerwester1.dict')

counter=0;
final_topic=0;
for doc in documents:
    if 6000< counter <11051:
        vec_bow = dictionary.doc2bow(doc.lower().split())
        vec_lda = lda[vec_bow] # convert the query to LSI space
        for vec in vec_lda:
            if vec[1]>0.15:
                print(" "+doc_ids[counter])
                my_data='[{"id":"'+doc_ids[counter]+'","tweet_topics":{"add":'+str(vec[0])+'}}]'
                print(my_data)
                req = urllib2.Request(url='http://52.34.17.82:8983/solr/ezra/update/json?commit=true', data=my_data)
                req.add_header('Content-type', 'application/json')
                f = urllib2.urlopen(req)
                print(f)
    counter=counter+1
        
