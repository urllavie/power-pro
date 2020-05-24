#動画の読み込み
v = cv2.VideoCapture('douga\実況パワフルプロ野球２０１８_20200523160635.mp4')

# 動画ファイル保存用の設定
fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)
video2 = cv2.VideoWriter('video_out_wb.mp4', fourcc, fps, (w, h), False)


while(v.isOpened()):
    r, frame = v.read()
    if ( r == False ):
        break

    #グレースケールに変換
    gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #輪郭をとる
    contours, hierarchy = cv2.findContours(gray_frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

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
            center, radius = cv2.minEnclosingCircle(contours[i])
            x, y, w, h = cv2.boundingRect(rect)
            #元動画に□を書き込む
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame,(center), radius, (0,0,255), 2)

    cv2.imshow("", frame)
    video2.write(frame)   
v.release()
cv2.destroyAllWindows()