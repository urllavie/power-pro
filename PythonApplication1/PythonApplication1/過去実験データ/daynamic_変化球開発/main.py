import video_analyzer
import numpy as np
import os
import glob

filelist = glob.glob("douga\\*.mp4")

for filepath in filelist:
    resultpath = 'result\\'
    filename = os.path.basename(filepath)
    filename_withoutEx = os.path.splitext(filename)[0]

    shade, ball = video_analyzer.video_analyze(filepath)


    np.savetxt(resultpath + filename_withoutEx + '_shade.txt', shade, fmt='%.5f', delimiter=',')
    np.savetxt(resultpath + filename_withoutEx + '_ball.txt', ball, fmt='%.5f', delimiter=',')
