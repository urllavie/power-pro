import cv2
import kido_analyzer

#動画の読み込み
v = cv2.VideoCapture('douga\実況パワフルプロ野球２０１８_20200526210204.mp4')

kl =[]
while(v.isOpened()):
    r, frame = v.read()
    if ( r == False ):
        break

    kido = kido_analyzer.analyze(frame)
    kl.append(kido)

    #cv2.imshow("", frame)
    #video2.write(frame)   
v.release()
cv2.destroyAllWindows()

print(kl)