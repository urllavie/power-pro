import video_analyzer
import numpy as np
import os

filepath = 'douga\実況パワフルプロ野球２０１８_20200524161252.mp4'
filename = os.path.basename(filepath)
filename_withoutEx = os.path.splitext(filename)[0]

shade, ball = video_analyzer.video_analyze(filepath)


np.savetxt(filename_withoutEx + '_shade.txt', shade, fmt='%.5f', delimiter=',')
np.savetxt(filename_withoutEx + '_ball.txt', ball, fmt='%.5f', delimiter=',')
