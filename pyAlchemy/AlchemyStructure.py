'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''

class Sentiment:
    """Class for representing Sentiment"""
    
    def __init__(self):
        """Constructor of Sentiment class"""
        self.type = None
        self.score = None
    
    def getType(self):
        """method for getting the category of the sentiment -> positive, negative, neutral"""
        return self.type
    
    def getScore(self):
        """method for getting the score of the sentiment"""
        return self.score
    
    
    def setType(self,type):
        """method for setting the category of the sentiment"""
        self.type = type
    
    def setScore(self,score):
        """method for setting the score of the sentiment """
        self.score = score



class Entity:
    """"Class for representing Entity"""
    
    def __init__(self):
        """Constructor for the Entity class"""
        self.name = None
        self.frequecy = None
        self.sentiment = None
        self.relevance = None
        self.type = None
        
    
    def setName(self,name):
        """method for setting the name of the entity  """
        self.name = name
    
    
    def getName(self):
        """method for getting the name of the entity"""   
        return self.name
    

    def setFreq(self,freq):
        """method for setting the frequency of the entity"""
        self.frequency = freq
             

    def getFreq(self):
        """method for getting the frequency of the entity"""
        return self.frequency
    

    def getSentiment(self):
        """method for getting the sentiment of entity"""
        return self.sentiment
    

    def setSentiment(self,sentiment):
        """method for setting the sentiment"""
        self.sentiment = sentiment
        
    
    def setRelevance(self,relev):
        """method for setting the relevance"""
        self.relevance = relev
        
    
    def getRelevance(self):
        """method for getting the relevance"""
        return self.relevance
    

    def setType(self,type):
        """method for setting the type of the entity"""
        self.type = type
        

    def getType(self):
        """method for getting the type of the entity"""
        return self.type
    
    
    

class Keyword:
    """Class for representing Keyword Extraction"""
    
    def __init__(self):
        """constructor for Keyword class"""
        self.text = None
        self.relevance = None
        self.sentiment = None
        
    
    def setText(self,text):
        """method for setting the text"""
        self.text = text
        
    def getText(self):
        """method for getting the text"""
        return self.text
    
    def setRelevance(self,relev):
        """method for setting the relevance"""
        self.relevance = relev
        
    def getRelevance(self):
        """method for getting the relevance"""
        return self.relevance
    
    def setSentiment(self,sentiment):
        """method for setting the sentiment"""
        self.sentiment = sentiment
        
    def getSentiment(self):
        """method for getting the sentiment"""
        return self.sentiment
    

class Concept:
    """Class for representing Concept Tagging"""
    
    def __init__(self):
        """Constructor for Concept class"""
        self.text = None
        self.relevance = None
        
    def setText(self,text):
        """method for setting the text"""
        self.text = text
        
    def getText(self):
        """method for getting the text"""
        return self.text
    
    def setRelevance(self,relev):
        """method for setting the relevance"""
        self.relevance = relev
        
    def getRelevance(self):
        """method for getting the relevance"""
        return self.relevance    
    


class Categorization:
    """Class for representing Text Categorization"""
    
    def __init__(self):
        """constructor for Categorization class"""
        self.text = None
        self.score = None
        

    def setText(self,text):
        """method for setting the text"""
        self.text = text
        
    def getText(self):
        """method for getting the text"""
        return self.text   
      
    def setScore(self,score):
        """method for setting the score of the sentiment"""
        self.score = score
        
    def getScore(self):
        """method for getting the score of the sentiment"""
        return self.score



class Relation:    
    """Class for representing Relation Extraction"""

    def __init__(self):
        """constructor for Relation class"""
        self.subject = None
        self.action = None
        self.object = None
        
    def setSubject(self, subject):
        """method for setting the subject"""
        self.subject = subject
        
    def getSubject(self):
        """method for getting the subject"""
        return self.subject
    
    def setAction(self, action):
        """method for setting the action"""
        self.action = action
        
    def getAction(self):
        """method for getting the action"""
        return self.action
    
    def setObject(self, obj):
        """method for setting the object"""
        self.object = obj
        
    def getObject(self):
        """method for getting the object"""
        return self.object
                
    

class Language:
    """Class for representing Language Detection"""
    
    def __init__(self):
        """constructor for Language class"""
        self.language = None
        self.iso = None
        self.native = None
        
    def setLanguage(self, lang):
        """method for setting the language"""
        self.language = lang
        
    def getLanguage(self):
        """method for getting the language"""
        return self.language    
    
    def setIso(self, iso):
        """method for setting the iso"""
        self.iso = iso
        
    def getIso(self):
        """method for getting the iso"""
        return self.iso
    
    def setNative(self, native):
        """method for setting the native speakers"""
        self.native = native
        
    def getNative(self):
        """method for getting the native speakers"""
        return self.native         
        


class Author:
    """Class for representing Author Extraction"""
    
    def __init__(self):
        """constructor for author class"""
        self.author = None
    
    def setAuthor(self, author):
        """method for setting the author"""
        self.author = author
        
    def getAuthor(self):
        """method for getting the object"""
        return self.author
    
    
    
                
        
            
        
        
        
        
      