import requests
import pandas as pd
import time
from functools import reduce
import numpy as np
import time
from bs4 import BeautifulSoup
import requests
import nltk 
#cleaning function
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import word_tokenize
import string
from nltk.tokenize import RegexpTokenizer
#clustering function
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

#collecting data from internet

def extractring_page(url):
    try:
        l=[]
        soup=BeautifulSoup(requests.get(url).text, "html.parser")
        time.sleep(2)
        try:
            y=soup.findAll('p',{'titolo text-primary'})
            for house in y:
                s='https://www.immobiliare.it'
                s1=house.contents[1]['href']
                if s1.startswith("https")==False:
                    s1=s+s1
                l.append(s1)
        except:
            pass
    except:
        l=['The page does not exit']
    return(l)

# retriving data from a given link
def Objective_page(url):
    try:
        tag=BeautifulSoup(requests.get(url).text, "html.parser")
        time.sleep(2)
        l1=['piano','bagni','superficie','locali']
        df=[]
        x=tag.findAll('div',{'class':'im-property__features'})
        y=tag.findAll('div',{'class':'clearfix description'})
        d={}
        house=[text for text in x[0].stripped_strings]
        house.reverse()
        house1=[text for text in y[0].stripped_strings]
        house1=" ".join(house1)
        for i in l1:
            if i in house:
                index=house.index(i)
                if i=='superficie':
                    d[i]=house[index+3]
                else:
                    d[i]=house[index+1]
                if house[-1].find('€')!=-1:
                    d['prezzo(€)']=house[-1]
        d['description']=house1
    except:
        d['description']="there was a problem in this link"
    del tag
    return(d)

# cleaning data function


