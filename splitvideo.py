  
import cv2
import numpy as np
import os
import random

class VideoSplit:
    season = random.randint(1, 8)
    path = "Grim Adventures of Billy and Mandy/Billy and Mandy-Season {}".format(season)
    dirs = os.listdir(path)
    pathFile = dirs[random.randint(0, len(dirs)-1)]
    path = os.path.join(path, pathFile)

    #get name of episode 
    nameofEpisode = pathFile.split(" - ", 2)
    nameofEpisode = nameofEpisode[1]
    
    #get file path for desired video and where to save frames locally
    cap = cv2.VideoCapture(path)
    path_to_save = 'D:\Projects\Twitter Bot\Grim Adventures of Billy and Mandy\Frames'

    # get numbers of frames
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(length)

    #capture  frame
    numFrame = random.randint(1, length - 1)
    cap.set(1, numFrame)
    ret, frame = cap.read()

    # Save frame as a jpg file
    name = nameofEpisode + ', frame '+ str(numFrame) + '.jpg'
    #print ('Creating: ' + name)
    namevideo = nameofEpisode + ', Frame '+ str(numFrame)
    path = os.path.join(path_to_save, name)
    cv2.imwrite(path, frame)

    #release capture 
    cap.release()
    #print('done')

    def getPathOfEpisode(self):
        return self.path

    def getNameofTweet(self):
        return self.nameofEpisode + ', Frame '+ str(self.numFrame)


