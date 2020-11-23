#10球分の動画ファイルを１球ずつファイルに分割する
import glob
import cv2
import Common.C_frame
import os
import shutil

inputDir = "C:\\Users\\url_l\\Documents\\GitHub\\power-pro\\pawapro\\input\\"
outputDir = "C:\\Users\\url_l\\Documents\\GitHub\\power-pro\\pawapro\\output\\"
rowdataDir = "C:\\Users\\url_l\\Documents\\GitHub\\power-pro\\pawapro\\rowdata\\"

filelist = glob.glob(inputDir + "*.mp4")

x = 580
y = 450
w = 125
h = 130

kidoBorder = 800

for filepath in filelist:
    filename = os.path.basename(filepath)
    filename_withoutEx = os.path.splitext(filename)[0]

    v = cv2.VideoCapture(filepath)
    # 動画ファイル保存用の設定
    fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
    vw = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
    vh = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）

    fileNo = 0
    fKido = False
    flKido = False

    while (v.isOpened()):
            r,frame = v.read()
            if (r == False):
                v.release() 
                shutil.move(filepath,rowdataDir + filename)
                break            
            cFrame = Common.C_frame.smallframe(x,y,w,h,frame)
            kido = cFrame.zone
            #print(kido)
            if kido < kidoBorder :
                break


    while (v.isOpened()):
        outputFilePath = outputDir + filename_withoutEx + '-' + str(fileNo).zfill(2) +'.mp4'
        video = cv2.VideoWriter(outputFilePath, fourcc, fps, (vw, vh), True)
        print(outputFilePath)
        while True:
            r,frame = v.read()
            if (r == False):
                v.release() 
                shutil.move(filepath,rowdataDir + filename)
                break
            
            cFrame = Common.C_frame.smallframe(x,y,w,h,frame)
            kido = cFrame.zone
            #print(kido)
            #frame1 = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            video.write(frame)
            if kido >= kidoBorder :
                fKido = True
            else:
                fKido = False

            if (flKido == True) and (fKido == False):
                fileNo = fileNo + 1
                flKido = fKido
                break
            flKido = fKido



