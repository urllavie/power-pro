filepath = 'douga\実況パワフルプロ野球２０１８_20200524161426.mp4'

# 動画ファイル保存用の設定
fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h), True)

