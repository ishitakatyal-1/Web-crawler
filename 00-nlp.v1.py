# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:41:43 2019

@author: Ishita
"""

import nltk
#nltk.download()
import urllib.request
from bs4 import BeautifulSoup

webadd = input("Enter the web add: ")
response = urllib.request.urlopen(webadd)
contents = response.read()
#print(contents)

soup = BeautifulSoup(contents,'html5lib')
text = soup.get_text(strip = True)
#print(text)

tokens = [t for t in text.split()]
#print(tokens)

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
#for key,val in freq.items():
#    print(str(key) + ':' + str(val))

freq.plot(30, cumulative=False)