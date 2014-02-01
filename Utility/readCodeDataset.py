'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''
import json

class ReadCodeData:
    """Class for reading the json dataset extracted from youtube"""
    
    def __init__(self):
        """constructor for ReadCodeData class"""
        self.dataset = [] #list for containing the data associated with the youtube videos, where each element is a video
    
    
    def parseDataset(self,filename):
        """Parses the give json dataset of youtube videos"""
        fp = open(filename).read()
        jsonData = json.loads(fp)
        for entries in jsonData:
            self.dataset.append(entries)
    
          
    def getDataset(self,filename):
        """gets the parsed data"""
        self.parseDataset(filename)
        return self.dataset