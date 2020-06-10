import numpy as np
import os
import glob
import cv2

import kido_analyzer
def video_tester(video_path):
    
    filepath = video_path
    filename = os.path.basename(video_path)
    filename_withoutEx = os.path.splitext(filename)[0]

    v = cv2.VideoCapture(filepath)
    while(v.isOpened()):

        r, frame = v.read()
        if ( r == False ):
            return
        kd = kido_analyzer.analyze(frame)



filelist = glob.glob("douga\\*.mp4")

for filepath in filelist:
    resultpath = 'result\\'
    filename = os.path.basename(filepath)
    filename_withoutEx = os.path.splitext(filename)[0]

    video_tester(filepath)
   




