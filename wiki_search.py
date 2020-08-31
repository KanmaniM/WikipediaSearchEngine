
import sys
import time
import os
import xml.sax
import re
from collections import defaultdict
import math
import bisect
import nltk
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
# import pickle
# nltk.download('porter')
# nltk.download('stopwords')
# from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem import PorterStemmer as porter
import operator
# import heapq
# import json
# import spacy
# from collections import OrderedDict
# nlp = spacy.load('en')
stemmer = SnowballStemmer("english")
# STOP_WORDS = spacy.lang.en.stop_words.STOP_WORDS


stopwords=["a", "about", "above", "above", "across", "after", "afterwards", "again",
           "against", "all", "almost", "alone", "along", "already", "also","although",
           "always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another",
           "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",
           "at", "back","be","became", "because","become","becomes", "becoming", "been",
           "before", "beforehand", "behind", "being", "below", "beside", "besides",
           "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can",
           "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe",
           "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either",
           "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every",
           "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill",
           "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found",
           "four", "from", "front", "full", "further", "get", "give", "go", "had", "has",
           "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein",
           "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred",
           "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself",
           "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may",
           "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
           "move", "much", "must", "my", "myself", "name", "namely", "neither", "never",
           "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not",
           "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only",
           "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out",
           "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same",
           "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should",
           "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
           "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take",
           "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there",
           "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv",
           "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
           "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two",
           "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were",
           "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas",
           "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
           "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without",
           "would", "yet", "you", "your", "yours", "yourself", "yourselves"
]


def tokenizeWords(data):
    # data = data.lower()
    tokenizer = RegexpTokenizer(r'[a-zA-Z0-9_]+')
    return tokenizer.tokenize(data)

def cleanData(data):
  # Tokenisation -> lower -> stopWords -> stemming
  data = data.lower()
  data = tokenizeWords(data)
 
  words = []
  for token in data:
    #   token = stemmer.stem(token)
      token = (token)
      if len(token) <= 1 or token in stopwords:
          continue
      # token = token.lower()  
      words.append(token)
  return words

class SearchEngine:
    
    def __init__(self):
        self.nonfieldQuery = 0
        self.tokensToSearch = []
    
    
    def createTokens(self,searchQuery):
        
        if ":" in  searchQuery:
            self.nonfieldQuery = 0
        else:
            self.nonfieldQuery = 1

        if self.nonfieldQuery == 1:
            self.tokensToSearch += cleanData(searchQuery)
        else:
            tokensList = re.split(r'^t:|b:|c:|i:|r:|e:',searchQuery)
            for token in tokensList:
                self.tokensToSearch +=  cleanData(token)
            
        # print(self.tokensToSearch)
        # print(self.nonfieldQuery)



    def printPostingList(self,indexFileSource):
        fpToIndexFile = open(indexFileSource,'r')
      
        if(self.nonfieldQuery == 1 or self.nonfieldQuery == 0):
            getLine = fpToIndexFile.readline().strip('\n')
            while(getLine and len(self.tokensToSearch)>=1):
                word = getLine.split(":")[0].strip()
                postingList = getLine.split(":")[1].strip()
                if word in self.tokensToSearch:
                    # print("word is :",word)
                    print(postingList)
                    self.tokensToSearch.remove(word)
                getLine = fpToIndexFile.readline().strip('\n')
            
        


query = sys.argv[2]
indexFileSource = sys.argv[1] + "index.txt"
search = SearchEngine()
search.createTokens(query)
search.printPostingList(indexFileSource)

