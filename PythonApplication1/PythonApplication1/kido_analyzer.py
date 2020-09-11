import cv2 
import numpy as np


def analyze(frame1):
    height, width, channels = frame1.shape
#    x = 480
#    y = 155
#    w = 300
#    h = 55
    x = 580
    y = 450
    w = 125
    h = 130
    img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame1)
    img_red_c1 = img_red_c1[y:y + h, x :x +w]
    img_green_c1 = img_green_c1[y:y + h, x :x +w]
    img_blue_c1 = img_blue_c1[y:y + h, x :x +w]
    img_red_c1[img_green_c1 > 110] = 0
    img_red_c1[img_red_c1 > 100] = 255
    img_red_c1[img_red_c1 <= 100] = 0
    #img_red_c1[img_green_c1 > 110] = 0
    #img_green_c1[img_green_c1 > 165] = 0
    #img_green_c1[img_green_c1 <= 165] = 0
    #img_blue_c1[img_blue_c1 > 165] = 0
    #img_blue_c1[img_blue_c1 <= 165] = 0
    

    #test1=-1 * np.sum(np.array(img_red_c1))/255 
    #test2=np.sum(np.array(img_green_c1))/255
    #test3=np.sum(np.array(img_blue_c1))/255

    kido = 1 * np.sum(np.array(img_red_c1))/255
   #+ np.sum(np.array(img_green_c1))/255 + np.sum(np.array(img_blue_c1))/255
  
    
    #print(kido)
    #x1 = 580
    #y1 = 625
    #w1 = 125
    #h1 = 30
    #frame1 = cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.imshow("", frame1)
    #cv2.waitKey(100)
    
    return kido
