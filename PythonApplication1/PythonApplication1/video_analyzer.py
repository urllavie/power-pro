
import numpy as np
import cv2
import detector_shade
import detector_ball
import os

def video_analyze(video_path):

    filepath = video_path
    filename = os.path.basename(video_path)
    filename_withoutEx = os.path.splitext(filename)[0]

    v = cv2.VideoCapture(filepath)

    # 動画ファイル保存用の設定
    fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
    w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
    h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter(filename_withoutEx + '_out.mp4', fourcc, fps, (w, h), True)


    #解析開始条件
    #輝度が一定を超えてから一定フレームたってから開始    
    while(v.isOpened()):
        r, frame = v.read()
        if ( r == False ):
            break
        video.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kido = np.sum(np.array(frame))
        if kido > 131400000:
            break
    #輝度が一定を超えて42フレームで解析を開始する
    for i in range(42):
        r, frame = v.read()
        if ( r == False ):
            break
        video.write(frame)


    #解析開始
    shade_detector = detector_shade.Detector_shade()
    ball_detector = detector_ball.Detector_ball()
    nframe = 0
    balllist=[]
    shadelist =[]
    kido = 0
    lkido = 0
    lradius_shade = 0
    lradius_ball = 0
    while(v.isOpened()):
        nframe += 1
        r, frame = v.read()
        if ( r == False ):
            break

        #終了条件　輝度解析
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kido = np.sum(np.array(gray))
        skido = kido/10 - lkido/10
        if skido < -400000 /10:
            video.write(frame)
            break
        lkido = kido

        #検出
        r1, shade_contour = shade_detector.detect(frame)
        r2, ball_contour = ball_detector.detect(frame)

        if r1 == False and r2 == False:
            video.write(frame)
            continue

        if r1 == True:
            x, y, w, h = cv2.boundingRect(shade_contour)
            center, radius = cv2.minEnclosingCircle(shade_contour)
            if radius >= lradius_shade:
                #輪郭の描画
                cv2.circle(frame,(int(center[0]),int(center[1])), int(radius), (0,0,255), 2)
                shadelist.append([nframe,x,y,radius])
                lradius_shade = radius

        if r2 == True:
            x, y, w, h = cv2.boundingRect(ball_contour)
            center, radius = cv2.minEnclosingCircle(ball_contour)
            if radius >= lradius_ball:
                #輪郭の描画
                cv2.circle(frame,(int(center[0]),int(center[1])), int(radius), (0,255,0), 2)
                balllist.append([nframe,x,y,radius])
                lradius_ball = radius

        video.write(frame)

    print(balllist)
    print(shadelist)
    v.release()
    cv2.destroyAllWindows()

    return shadelist, balllist








