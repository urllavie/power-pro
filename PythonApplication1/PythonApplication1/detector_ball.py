import detector
import cv2
import numpy as np

class Detector_ball(detector.Detector):

        #条件にあった輪郭の中で最も条件にあうもの選択する
    def select_target(self, contours):

        maxy = 0
        for contour in contours:
            center, radius = cv2.minEnclosingCircle(contour)
            if maxy < center[1]:
                maxy = center[1]
                maxy_contour = contour

        return maxy_contour



    #二値化用関数　オーバーライドする
    def devalued(self,frame):

        #RGBの抽出
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame)

        img_devalued = img_blue_c1 & img_green_c1
        img_devalued = img_devalued & img_red_c1
        #二値化
        img_devalued2= img_red_c1
        img_devalued2[img_devalued < 150 ] = 0
        img_devalued2[img_devalued >= 150 ] = 255

        kernel = np.ones((4,4))
        img_devalued2 = cv2.dilate(img_devalued2, kernel)
        #cv2.imshow("", img_devalued2)
        #動画出力時間の調整
        #cv2.waitKey(100)        
        return img_devalued2

    #条件に合う輪郭を探す　オーバーライドする
    def condition_target(self, contour):
        x = 580
        y = 720 - (140 + 130)
        w = 130
        h = 130
        #x, y, w, h = cv2.boundingRect(contour)
        center, radius = cv2.minEnclosingCircle(contour)
        x1 = center[0]
        y1 = center[1]
        #描画する輪郭の条件
        if radius < 5 :
            return False
        if x > x1 or x1 > (x + w) or y > y1 or y1 > (y + h):
            return False
        return True

