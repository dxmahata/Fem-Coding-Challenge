'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''
import Utility.textProcessing as tp

import pyAlchemy.ProcessAlchemy as pyAl
import Utility.textProcessing as tp
import pyAlchemy.alchemyapi
import uuid


class Video:
    """
    class for YouTube videos.
    """
    
    def __init__(self):
        """Constructor for initializing a video object"""
        self.title = "" #title of the video instance
        self.description = "" #description of the video instance
        self.entities = [] #entities associated with the video instance
        self.categories = [] #categories associated with the video instance
        self.tokens = [] #tokens associated with the text of the video
        self.tags = [] #automated extracted tags of the video
        self.count = 0 #count of the video in the list of videos provided in the dataset
        self.videoId = ""  #system generated id of the video
        
    

    def setCount(self,count):
        """method for setting the count of a video instance"""
        self.count = count
    
        
    def getCount(self):
        """method for getting the count of a video instance"""
        return self.count
    
    
    def setTags(self,tags):
        """method for setting the tags associated with a video instance"""
        self.tags = tags
    
        
    def getTags(self):
        """method for getting the tags of a video instance"""
        return self.tags
    
    
    def setTitle(self,title):
        """method for setting the title of a video instance"""
        self.title = title
    
        
    def getTitle(self):
        """method for getting the title of a video instance"""
        return self.title
    
    
    def setDescription(self,desc):
        """method for setting the description of a video instance"""
        self.description = desc
    
        
    def getDescription(self):
        """method for getting the description of a video instance"""
        return self.description
    
    
    def setEntities(self,entities):
        """method for setting the entities extracted from the text of a video instance"""
        self.entities = entities
    
        
    def getEntities(self):
        """method for getting the entities associated with the text of a video instance"""
        return self.entities
    
    
    
    def setCategories(self,categories):
        """method for setting the catgories associated with a video instance"""
        self.categories = categories
    
       
    def getCategories(self):
        """method for getting the categories associated with a video instance""" 
        return self.categories
    
    
    def setToken(self,termVector):
        """method for setting the tokens associated with the text of a video instance"""
        self.tokens = termVector
    
        
    def getToken(self):
        """method for getting the tokens associated with the text of a video instance"""
        return self.tokens
    
        
    def setVideoId(self,vidId):
        """method for setting the system generated video Id"""
        self.videoId = vidId
    
       
    def getVideoId(self):
        """method for getting the system generated video Id""" 
        return self.videoId
    


class ProcessVideos:
    """Class for processing each video from the dataset and extracting the associated tags as well as the other details"""
    
    
    def __init__(self,data):
        """Constructor for initializing the ProcessVideos class""" 
        self.videoTagIndexTable = {} #videos indexed by tags
        self.data = data #parsed dataset
        self.videoCollection = {} #videos indexed by their ids.
        
    def getData(self):
        """method for getting the parsed dataset"""
        return self.data
    
    def processData(self):
        """method for processing the data associated with the videos in order to extract the tags associated with it. Also the method
        creates an object of class Video for each video instance and stores its details in the respective object. The method also creates
        a dictionary/hash table for storing the videos where the system generated video ids are the keys and the created video instances 
        are the values. For example:
        566898e1-8ac6-11e3-9883-ecb7572c5936 -> videoObj1
        5677db1e-8ac6-11e3-890c-ecb7572c5936 -> videoObj2
        The method also creates another hash table where it stores all the videos by its tags. In this case the tag becomes the key and
        a list of videos associated with the tag are the values represented by their videoIds.
        """
        
        import sys
        
        sys.stdout = open("VideoTaggingOutput.txt","w")#output file that shows the details associated with each video and the automatically generated tag associated with the video.
        
        count = 1 #counter for maintaining the count of the videos
        
        
        
        for data in self.data:
            
            # system generated video id
            videoId = uuid.uuid1() 
            
            #instantiating a Video object
            video = Video() 
            
            #setting the id of the video 
            video.setVideoId(str(videoId)) 
            
            #setting the count of the video
            video.setCount(count) 
            
            print "Video "+str(count)
            print "\n"
            
            print "Video Id: "+str(videoId)
            print "\n"
            
            #description of the you tube video
            description = data['description']
            print "Description of the video is: ", description
            print "\n"
            
            #setting the description associated with the video
            video.setDescription(description)
            
            #title associated with you tube video
            title = data['title']
            print "The title of the video is: ", title
            print "\n"
            
            #setting the title associated with the video
            video.setTitle(title)
            
            #categories associated with the you tube video
            categories = data['categories']
            print "The categories associated with the video are:", str(categories)
            print "\n"
            
            #setting the categories associated with the video
            video.setCategories(categories)
            
            
            #create object for extracting entities using Alchemy API
            entityExtract = pyAl.EntityExtraction()
        
            #full text associated with the you tube video title + description
            textFromYoutubeVideo = str(description.encode("utf-8")+title.encode("utf-8")).lower()
        
            #getting the list of named entities mentioned in the associated text
            entities = entityExtract.getNamedEntitiesFromText(textFromYoutubeVideo)
            
            #list for storing the extracted tags
            tags = []
            
            print "The tags associated with the video along with their types are:"
            if entities != []:
                for entity in entities:
                    entityName = entity.getName()
                    print "Tag: ", entityName
                    tags.append(entityName)
                    entityType = entity.getType()
                    print "Tag type: ", entityType
                    
                    print "\n"
            else:
                print entities
            
            #set the list of entities associated with the video
            video.setEntities(entities)
            
            #instantiating object for processing the text associated with the video
            toObj = tp.TextProcessing()
            
            #feed the text to the object
            toObj.setText(textFromYoutubeVideo)
            
            #remove digits from given text
            textWithoutDigits = toObj.removeDigits(toObj.getText())
            
            #remove special characters from given text
            textWithoutSpecialCharacters = toObj.removeSpecialChars(textWithoutDigits)
            
            #tokenized filtered text
            filteredText = toObj.getFilteredText(textWithoutSpecialCharacters)
            
            print "The term vector associated with the video is:"
            print filteredText
            
            #set the list of tokens associated with the text of the video
            video.setToken(filteredText)
            
            #hash table entry
#            self.videoCollection[videoId] = video
            self.videoCollection[count] = video
            
            #setting the tags associated with the video
            video.setTags(tags)
            
            #hash table entry
            for tag in tags:
                if tag.lower() in self.videoTagIndexTable:
                    self.videoTagIndexTable[tag.lower()].append(count)
                else:
                    self.videoTagIndexTable[tag.lower()] = []
                    self.videoTagIndexTable[tag.lower()].append(count)
            
            print "-------------------"
            
            #increasing the counter
            count += 1

        return self.videoTagIndexTable, self.videoCollection   
            
            

    
    
        
        
    