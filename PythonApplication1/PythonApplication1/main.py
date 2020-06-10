import video_analyzer
import numpy as np
import os
import glob

filelist = glob.glob("douga\\*.mp4")

for filepath in filelist:
    resultpath = 'result\\'
    filename = os.path.basename(filepath)
    filename_withoutEx = os.path.splitext(filename)[0]

    shade, ball, ptt, st = video_analyzer.video_analyze(filepath)

    np.savetxt(resultpath + filename_withoutEx + '_shade.txt', shade, fmt='%.5f', delimiter=',')
    #np.savetxt(resultpath + filename_withoutEx + '_ball.txt', ball, fmt='%.5f', delimiter=',')
    

    file = resultpath + filename_withoutEx + '_info.txt'
    f = open(file, "w", encoding = "shift_jis")
    f.write(filename_withoutEx + '\n')
    f.write(ptt+ '\n')
    f.write(st)
    f.close()