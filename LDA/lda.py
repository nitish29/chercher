from urllib2 import *
from solr import *
import urllib2
import logging
import simplejson
from stemming.porter2 import stem
logging.basicConfig(format=' %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities

#conn = urlopen('http://richieverma.koding.io:8983/solr/partB/select?q=tweet_tags:*&wt=json&rows=13000')
conn = urlopen('http://52.34.17.82:8983/solr/ezra/select?q=tweet_tags:*&wt=json&rows=11051')
initial=True

rsp = simplejson.load(conn)
f = open('output_lda.txt', 'w')
f1 = open('output_lda_ids.txt','w')
for doc in rsp['response']['docs']:
    last_trailing_word = "[^' 'a-zA-Z#:\/0-9._@,]*"
    pat = re.compile( last_trailing_word )

    f1.write(doc['id'] + "\n")
    for s in doc['tweet_tags']:
        tweet = pat.sub('',s)
        #if initial==True:
        f.write(tweet+" ")
        #initial=False
        #else:
        #f.write("\n" + tweet)
    f.write('\n')
f.close()
f1.close()
  


documents = [line.strip() for line in open("output_lda.txt", 'r')]
doc_ids = [line.strip() for line in open("output_lda_ids.txt", 'r')]
 
 # remove common words and tokenize
stoplist = set('for a of the and to in from'.split())
texts = [[stem(word.lower()) for word in document.lower().split() if word not in stoplist]
          for document in documents]
print(texts)
 # remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
     for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

from pprint import pprint   # pretty-printer
dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester1.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester1.mm', corpus) # store to disk, for later use



mm = corpora.MmCorpus('/tmp/deerwester1.mm')

lda = models.ldamodel.LdaModel(corpus=mm, id2word=dictionary, num_topics=10, update_every=200, chunksize=200, passes=15)

lda.save('/tmp/try_lda_saver')
index = similarities.MatrixSimilarity(lda[mm])
index.save('/tmp/deerwester1.index')
lda.print_topics(10)
