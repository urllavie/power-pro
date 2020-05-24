import cv2
import numpy as np
#import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)
th = 0
th2 = 30
v = cv2.VideoCapture('douga\実況パワフルプロ野球２０１８_20200524161252.mp4')

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

#解析開始条件
#輝度が一定を超えてから一定フレームたってから開始    
while(v.isOpened()):
    r, frame1 = v.read()
    video.write(frame1)
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    kido = np.sum(np.array(frame))
    if kido > 131400000:
        break

for i in range(42):
    r, frame1 = v.read()
    video.write(frame1)


r, frame1 = v.read()
frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
bg = frame
while(v.isOpened()):

    

    nframe += 1 
    r, frame1 = v.read()
    if ( r == False ):
        break
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    #RGBの抽出
    img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame1)
    #白いところを検出
    test = img_blue_c1 & img_green_c1
    test = test & img_red_c1
    #二値化
    test2= test
    test2[test < 180] = 0
    test2[test >= 180] = 255

    #輝度解析と解析終了条件
    kido = np.sum(np.array(frame))

    #/10しないとエラーが出るなぜ。。。
    skido = kido/10 - lkido/10
    if skido < -400000 /10:
        video.write(frame1)
        break
    lkido = kido
    kidolist.append(kido)
    
    #動画出力時間の調整
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

    #輪郭の検出
    contours, hierarchy = cv2.findContours(test2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    detect_count = 0

    # 各輪郭に対する処理
    miny = np.Infinity
    for i in range(0, len(contours)):

        # 輪郭の領域を計算
        area = cv2.contourArea(contours[i])

        # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
        if area < 10 or 1000 < area:
            continue

        # 外接矩形
        if len(contours[i]) > 0:
            
            rect = contours[i]
            x, y, w, h = cv2.boundingRect(rect)
            center, radius = cv2.minEnclosingCircle(contours[i])

            #描画する輪郭の条件
            if radius > 15 or radius < 6 or int(radius) == 14:
                continue
            if x > 755 or x < 560 or x == 690:
                continue
            
            detect_count = detect_count + 1
            if y < miny:
                targetc = contours[i]
    
    #輪郭検出されなければ次へ
    if detect_count == 0:
        cv2.imshow("", test2)
        video.write(frame1)
        continue
    x, y, w, h = cv2.boundingRect(targetc)
    center, radius = cv2.minEnclosingCircle(targetc)
    #輪郭の描画
    cv2.circle(frame1,(int(center[0]),int(center[1])), int(radius), (0,0,255), 2)
    #結果の出力
    nflist.append(nframe)
    xlist.append(x)
    ylist.append(y)
    wlist.append(w)
    hlist.append(h)
    rlist.append(radius)


    cv2.imshow("", test2)
    video.write(frame1)



print(nflist)
print(xlist)
print(ylist)
print(rlist)
#print(wlist)
#print(hlist)
#print(kidolist)
v.release()
cv2.destroyAllWindows()