import detector
import cv2
import numpy as np

class Detector_shade(detector.Detector):

        #条件にあった輪郭の中で最も条件にあうもの選択する
    def select_target(self, contours):

        miny = 2000
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if miny > y:
                miny = y
                miny_contour = contour

        return miny_contour



    #二値化用関数　オーバーライドする
    def devalued(self,frame):
        #RGBの抽出
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame)

        img_devalued = img_blue_c1 | img_green_c1
        img_devalued = img_devalued | img_red_c1
        #二値化
        img_devalued2= img_devalued
        img_devalued2[img_green_c1 > 160] = 0
        kernel = np.ones((3,3))

        img_devalued2[img_devalued2 < 190 ] = 0
        img_devalued2[img_devalued2 >= 190 ] = 255
        
        img_devalued2 = cv2.dilate(img_devalued2, kernel)
        #img_devalued2[img_devalued < 190 ] = 0
        #img_devalued2[img_devalued >= 190 ] = 1
        #img_devalued2[img_devalued2 ==0 ] = 255
        #img_devalued2[img_devalued2 ==1 ] = 0        
        #cv2.imshow("", img_devalued2)
        #動画出力時間の調整
        #cv2.waitKey(100)
        
        return img_devalued2

    #条件に合う輪郭を探す　オーバーライドする
    def condition_target(self, contour):
        #x, y, w, h = cv2.boundingRect(contour)
        center, radius = cv2.minEnclosingCircle(contour)
        x = center[0]
        y = center[1] 
        #描画する輪郭の条件
        if y < 630 or y > 690 or x < 560 or x > 760:
            return False

        return True

