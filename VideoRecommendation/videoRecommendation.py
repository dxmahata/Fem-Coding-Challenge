'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''

from operator import itemgetter


class RecommendVideo:
    """Constructor for RecommendVideo"""
    def __init__(self,vidTagIndxTable, vidCollect):
        self.videoTagIndexTable = vidTagIndxTable #hashtable consisting of videos indexed by tags
        self.videoCollection = vidCollect #hashtable consisting of videos indexed by videoIds
    
    
    def getVideo(self, vidId):
        """method of retrieving a video by its videoId from videoCollection"""
        return self.videoCollection[vidId]
    
    def recommendation(self):
        """method that returns ranked recommendations for a given video"""
        import sys
        
        #output file for getting the videos and its related recommendations
        sys.stdout = open("VideoRecommendations.txt","w")
        
        #getting video recommendations for each video provided in the dataset
        for video in self.videoCollection.keys():
            videoObj = self.getVideo(video)
            self.ranking(videoObj)                
            print "\n\n-----------------------------------------------\n\n"
            
            
        
    def ranking(self,videoObj):
        """method for ranking the related videos"""
        print "The selected video details are:"
        
        print "\n The system generated id of the video is: ", videoObj.getVideoId()
        print "\n The title of the video is: ", videoObj.getTitle()
        print "\n The description of the video is: ", videoObj.getDescription()
        videoTags = videoObj.getTags()
        print "\n The tags associated with the video are: ", videoTags
        print "\n The categories associated with the video are: ", videoObj.getCategories()
        
        videoTokens = videoObj.getToken()
        #print "\n The tokens associated with the video text is: ",videoTokens
        
        
        if videoTags == []:
            pass
        else:
            print "###################################################"
            print "\n\nThe videos from the provided dataset that are related to the given video are:"
            count = 1
            
            #dictionary for storing the jaccard coefficient scores indexed by the videoIds
            scoredVideos = {} 
            
            for tag in videoTags:
#                    print "Tag: ", tag
#                    print "\n Videos related to the tag:"

                #list of videos related to the selected tag 
                videosRelatedToTag = self.videoTagIndexTable[tag]
                
                for videos in videosRelatedToTag:                    
                    if videos == videoObj.getVideoId():
                        pass
                    else:
                        jacCof = self.jaccardCoefficient(videoTokens, self.getVideo(videos).getToken())
                        scoredVideos[videos] = jacCof 
                        
                        
            #sorting the simlarity scores of the videos
            items = scoredVideos.items()
            items.sort(key=itemgetter(1),reverse=True)      
            
#                if len(items) <= 3:
#                    top3VideoIds = items
#                else:
#                    top3VideoIds = items[:2]   

            for vids in items:
                vid = self.getVideo(vids[0])
                print "Video No: ", str(count)        
                print "\n The system generated id of the video is: ", vid.getVideoId()        
                print "\n The title of the video is: ", vid.getTitle()        
                print "\n The description of the video is: ", vid.getDescription() 
                print "\n The tags associated with the video are: ", vid.getTags()
                print "\n The categories associated with the video are: ", vid.getCategories()
                #print "\n The term vector associated with the video text is:", vid.getToken()       
                print "*****************************************"
                count += 1        
                        
                            
                            
    def jaccardCoefficient(self,termVector1,termVector2):
        """method for calculating the Jaccard Coefficient between the set of terms associated with the video being processed and the chosen related video"""
        jacCof = float(len((set(termVector1).intersection(set(termVector2))))/(len(set(termVector1).union(set(termVector2)))))
        return jacCof
        

            
            

        


        