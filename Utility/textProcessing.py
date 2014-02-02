'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''
import re
import os
from nltk.stem import PorterStemmer

class TextProcessing:
    
    """class for performing all text processing operations"""
    def __init__(self):
        """constructor for TextProcessing class"""
        self.stopWords = set([]) #set for containing the list of unique stop words
        self.text = "" #text to be processed
    
    
       
    def setText(self,txt):
        """method of setting the text to be processed"""
        self.text = txt
        
    
    def getText(self):
        """method for getting the text that is being processed"""
        return self.text
    
       
    def setStopWords(self,file="stopwords.txt"):
        """method for setting the stop word list from the given stopword file"""
        for lines in open(file):
            self.stopWords.add(lines.split("\n")[0])
    
            
    def getStopWords(self):
        """method for getting the stop word list"""
        self.setStopWords()
        return self.stopWords
    
    

    def tokenize(self,txt):
        """method for tokenizing the text on blanks"""
        tokenizedText = txt.split(" ")
        tokenizedText = set(tokenizedText)
        if "" in tokenizedText:
            tokenizedText.remove("")
        return tokenizedText
    
    
    def removeDigits(self,txt):
        """method for removing digit [0-9] characters from given text"""
        digitRemovedText = re.sub(r'[\d]',"",txt)
        return digitRemovedText
    
    
    def removeSpecialChars(self,txt):
        """
        method for removing special characters from given text
        """
        specialCharRemovedText = re.sub(r'[-+\\\[\]()?,><=*\:\'\"//\.]'," ",txt)
        return specialCharRemovedText
    
    def stem(self,tokens):
        """method for stemming the tokens using nltk"""        
        stemmer = PorterStemmer() #instantiating the stemmer
        stemmedTokens = set([]) #set for containing the stemmed tokens
        
        for token in tokens:
            stemmedTokens.add(stemmer.stem(token))
        return stemmedTokens
        
    def getFilteredText(self,txt):
        """method for getting the filtered text after removing the stop words"""
        return self.stem(self.tokenize(txt).difference(self.getStopWords()))
    
    
    
    
   
            
                   
        
    
    