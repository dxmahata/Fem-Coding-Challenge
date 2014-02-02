'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''

import Utility.readCodeDataset as rcd
import VideoTagging.taggingVideos as vt
import VideoRecommendation.videoRecommendation as vr

def main():
    
    #creates the object for reading data from the specified data set
    readCodeData = rcd.ReadCodeData()
    
    #gets the parsed data of the given dataset
    dataset = readCodeData.getDataset("C:\Users\cisstudent\workspace\Fem-Coding-Challenge\CodeAssignmentDataSet.json")
    
    procVideo = vt.ProcessVideos(dataset)
    
    videoTagIndexTable,videoCollection = procVideo.processData()
    
    videoRecommend = vr.RecommendVideo(videoTagIndexTable,videoCollection)
    
    videoRecommend.recommendation()
    
    
    
    
    
#    count = 1
#    
#    for data in dataset:
#        print "Video "+str(count)
#        print "\n"
#        
#        #description of the you tube video
#        description = data['description']
#        print "Description of the video is: ", description
#        print "\n"
#        
#        #title associated with you tube video
#        title = data['title']
#        print "The title of the video is: ", title
#        print "\n"
#        
#        #categories associated with the you tube video
#        categories = data['categories']
#        print "The categories associated with the video are:", str(categories).strip("[").strip("]")
#        print "\n"
#        
##        tags = []
#        
#        #create object for processing using Alchemy API
#        procAlchemy = pyAl.ProcessAlchemy()
#        
#        #full text associated with the you tube video title + description
#        textFromYoutubeVideo = str(description.encode("utf-8")+title.encode("utf-8")).lower()
#        
#        #getting the list of named entities mentioned in the associated text
#        entities = procAlchemy.getNamedEntitiesFromText(textFromYoutubeVideo)
#        
#        for entity in entities:
#            print "Tag: ",entity.getName()
#            print "Tag Type: ", entity.getType()
#            
#        print "The keywords associated with the video are:\n"
#        keywords = procAlchemy.getKeywordsFromText(textFromYoutubeVideo)
#        print keywords
#        for key in keywords:
#            print "Keyword: ", key.getText()
#        print "\n\n"
#        
#        
#        '''processing the text'''
#        toObj = tp.TextProcessing()
#        
#        #feed the text to the object
#        toObj.setText(textFromYoutubeVideo)
#        
#        #remove digits from given text
#        textWithoutDigits = toObj.removeDigits(toObj.getText())
#        
#        #remove special characters from given text
#        textWithoutSpecialCharacters = toObj.removeSpecialChars(textWithoutDigits)
#        
#        #tokenized filtered text
#        filteredText = toObj.getFilteredText(textWithoutSpecialCharacters)
#        
#        print filteredText
#        
#        count += 1
#        
#        print "-------------------"
        
if __name__ == '__main__':
    main()


