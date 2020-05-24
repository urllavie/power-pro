import cv2
import numpy as np
import matplotlib.pyplot as plt

neiborhood8 = np.array([[1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]],
    np.uint8)

np.set_printoptions(threshold=np.inf)
th = 0
th2 = 30
IMROOT="C:/image/"
v = cv2.VideoCapture('douga\実況パワフルプロ野球２０１８_20200523160635.mp4')
r, bg = v.read()
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

xlist=[]
ylist=[]
wlist=[]
hlist=[]
nflist=[]
kidolist = []

# 動画ファイル保存用の設定
fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)
video2 = cv2.VideoWriter('video_out_wb.mp4', fourcc, fps, (w, h), False)

nframe=0

for i in range(1):
    r, frame1 = v.read()

r, frame1 = v.read()
frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
bg = frame
while(v.isOpened()):
    nframe += 1 
    r, frame1 = v.read()
    if ( r == False ):
        break
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(frame, 150, 250)
    can_subt = cv2.absdiff(canny_img,bg)
    img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame1)
    kido = np.sum(np.array(frame))
    kidolist.append(kido)
    #mask = cv2.absdiff(frame, bg)
    #mask2 =  np.array(frame).astype(int) - np.array(bg).astype(int)
    #mask = frame - bg
    mask = cv2.absdiff(frame, bg)

    #ret, binary = cv2.threshold(mask,60, 255,cv2.THRESH_BINARY)
    mask[mask < th2] = 0
    mask[mask > th2] = 255
#    print(bg[1])
#    print(frame[1])
#    print(mask[1])
#    break
    dim = cv2.dilate(can_subt,neiborhood8,iterations=1)    
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

    contours, hierarchy = cv2.findContours(can_subt, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    detect_count = 0

    # 各輪郭に対する処理
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

            #if h < 10 or h > 30 or w < 10 or w > 35 or x > 740 or abs(w - h) > 20 or  y > 475 or y < 100:
            #    continue
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame1,(int(center[0]),int(center[1])), int(radius), (0,0,255), 2)
            nflist.append(nframe)
            xlist.append(x)
            ylist.append(y)
            wlist.append(w)
            hlist.append(h)
          # 外接矩形毎に画像を保存
          #  cv2.imwrite('{ファイルパス}' + str(detect_count) + '.jpg', src[y:y + h, x:x + w])

            detect_count = detect_count + 1
    bg = canny_img
    cv2.imshow("", can_subt)
    video.write(frame1)
    video2.write(frame)

#print(nflist)
#print(xlist)
#print(ylist)
#print(wlist)
#print(hlist)
#print(kidolist)
v.release()
cv2.destroyAllWindows()