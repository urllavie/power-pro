import cv2
import numpy as np



np.set_printoptions(threshold=np.inf)
th = 0
th2 = 30
IMROOT="C:/image/"
v = cv2.VideoCapture('実況パワフルプロ野球２０１８_20200523160635.mp4')
r, bg = v.read()
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

# 動画ファイル保存用の設定
fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)

while(v.isOpened()):
    r, frame = v.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #mask = cv2.absdiff(frame, bg)
    mask2 = np.array(frame).astype(int)- np.array(bg).astype(int)
    mask = frame -bg
    #print(bg[1])
    #print(frame[1])
    #print(mask[1])
    #ret, binary = cv2.threshold(mask,60, 255,cv2.THRESH_BINARY)
    mask[mask2 < th2] = 0
    mask[mask2 > th2] = 255

    
    if ( r == False ):
        break
    cv2.imshow("", mask)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    #video.write(mask)

    bg = frame
v.release()
cv2.destroyAllWindows()