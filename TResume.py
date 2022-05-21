# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:37:11 2020

@author: hp
"""
import os
import nltk 
import pandas as pd 
from nltk.tokenize import sent_tokenize ,word_tokenize
import spacy
import fr_core_news_md
nlp = fr_core_news_md.load()


testfile=open('text.txt','r',errors='ignore')

phrase= testfile.read().lower().split('\n')

def removepunctuation(testfile):
    testfile1="".join([c for c in text if c not in string.punctuation])
    return testfile1
specialCharacters=['<h1>','</h1>','<h2>','</h2>','_','-','?','!','<p>','</p>']

def removespecialCharacters(text):
    testfile2="".join([c for c in test if c in specialCharacters])
    return testfile2

text=removepunctuation(testfile)
text=removespecialCharacters(testfile)
text=text.lower()
print(text)

pattern = re.compile(r'\b('+r'|'.join(stopwords.words('french'))+r')\b\s*')
testfile3=pattern.sub('',text)
print(testfile3)

token=word_tokenizet(testfile3)
print(token)

from nltk.probability import FreqDist
freqDist= FreqDist

plusFreq = freqDist.most_common(5)
print(plusFreq)

def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

return_token(testfile)


from nltk.corpus import stopwords
stopWords = set(stopwords.words('french'))

clean_words = []
for token in return_token(test):
    if token not in stopWords:
        clean_words.append(token)

return_stem(testfile)

#Tokenisation par phrases
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')

#stemming
def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]
return_stem(test)

#frequence
def frq(text, words):
   return [(word, text.count(word) for word in words]
