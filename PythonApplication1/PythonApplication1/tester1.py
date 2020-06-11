
import cv2
import numpy as np
import kido_analyzer
#import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)
th = 0
th2 = 30
v = cv2.VideoCapture('douga\実況パワフルプロ野球２０１８_20200531135150.mp4')

xlist=[]
ylist=[]
wlist=[]
hlist=[]
nflist=[]
kidolist = []
rlist = []


# 動画ファイル保存用の設定
fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)

flag = False
nframe=0
lkido = -1
skido = -1
kido = 0

#


while(v.isOpened()):
    r, frame = v.read()
    if ( r == False ):
        break
    kido = kido_analyzer.analyze(frame)
    kidolist.append(kido)
    #動画出力時間の調整

    video.write(frame)



#print(nflist)
#print(xlist)
#print(ylist)
#print(rlist)
#print(wlist)
#print(hlist)
print(kidolist)
v.release()
cv2.destroyAllWindows()