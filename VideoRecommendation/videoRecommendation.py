'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''


class RecommendVideo:
    def __init__(self,vidTagIndxTable, vidCollect):
        self.videoTagIndexTable = vidTagIndxTable
        self.videoCollection = vidCollect
    
    
    def getVideo(self, vidId):
        
        return self.videoCollection[vidId]
    
    def recommendation(self):
        import sys
        
        sys.stdout = open("VideoRecommendations.txt","w")

        for video in self.videoCollection.keys():
            videoObj = self.getVideo(video)
            
            print "The selected video details are:"
            
            print "\n The system generated id of the video is: ", videoObj.getVideoId()
            print "\n The title of the video is: ", videoObj.getTitle()
            print "\n The description of the video is: ", videoObj.getDescription()
            videoTags = videoObj.getTags()
            print "\n The tags associated with the video are: ", videoTags
            
            if videoTags == []:
                pass
            else:
                print "###################################################"
                print "\n\nThe videos from the provided dataset that are related to the given video are:"
                count = 1
                for tag in videoTags:
#                    print "Tag: ", tag
#                    print "\n Videos related to the tag:"
                    videosRelatedToTag = self.videoTagIndexTable[tag]
                    
                    for videos in videosRelatedToTag:
                        
                        if videos == video:
                            pass
                        else:
                            vid = self.getVideo(videos)
                            print "Video No: ", str(count)
                            print "\n The system generated id of the video is: ", vid.getVideoId()
                            print "\n The title of the video is: ", vid.getTitle()
                            print "\n The description of the video is: ", vid.getDescription()
                            print "*****************************************"
#
#                            print "Video no: ", str(count)
#                            print "Video id: ", str(vid.getVideoId())
#                            print "The title of the video is: ", vid.getTitle()
#                            print "\n"
#                            print "The description of the video is: ", vid.getDescription()
                            count += 1
                            
                            
                
            print "\n\n-----------------------------------------------\n\n"
            
            
        
#        videoObj = self.getVideo(vidId)
#        
#        print "The selected video details are: "
#        print "The title of the video is: ", videoObj.getTitle()
#        print "\n"
#        print "The description of the video is: ", videoObj.getDescription()
#                    
#
#        
#        videoTags = videoObj.getTags()
#        
#        if videoTags == []:
#            pass
#        else:
#            print "\n\nThe videos related to the given video are:"
#            for tag in videoTags:
#                print "Tag: ", tag
#                print "\n Videos related to the tag:"
#                videosRelatedToTag = self.videoTagIndexTable[tag]
#                count = 1
#                for videos in videosRelatedToTag:
##                    if videos.getCount() == vidId:
##                    
##                    print videos.getTitle()
##                    print videos.getCount()
##                    print videos.getVideoId()
##                    print videos.getDescription()
##                    print "---------------------\n"
#                    if videos == vidId:
#                        pass
#                    else:
#                        vid = self.getVideo(videos)
#                        print "Video no: ", str(count)
#                        print "Video id: ", str(vid.getVideoId())
#                        print "The title of the video is: ", vid.getTitle()
#                        print "\n"
#                        print "The description of the video is: ", vid.getDescription()
#                        count += 1
        
        
        
        


        