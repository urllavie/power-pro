import video_analyzer
import shutil
import numpy as np
import os
import glob

filelist = glob.glob("douga\\*.mp4")

nFile = 0
for filepath in filelist:
    nFile += 1
    print(str(nFile) + ' / ' + str(len(filelist)))
    resultpath = 'result\\'
    filename = os.path.basename(filepath)
    filename_withoutEx = os.path.splitext(filename)[0]

    shade, ball, ptt, st, pn = video_analyzer.video_analyze(filepath)

    np.savetxt(resultpath + filename_withoutEx + '_shade.txt', shade, fmt='%.5f', delimiter=',')
    np.savetxt(resultpath + filename_withoutEx + '_ball.txt', ball, fmt='%.5f', delimiter=',')
    

    file = resultpath + filename_withoutEx + '_info.txt'
    f = open(file, "w", encoding = "shift_jis")
    f.write(filename_withoutEx + '\n')
    try:
        f.write(ptt+ '\n')
    except:
        f.write("error" + '\n')
    try:
        f.write(st + '\n')
    except:
        f.write("error" + '\n')
    try:
        f.write(pn)    
    except:
        f.write("error")
    
    f.close()
    shutil.move(filepath,"douga - コピー\\" + filename)

    