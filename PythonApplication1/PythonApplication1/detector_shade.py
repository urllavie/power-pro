import detector
import cv2

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
        img_devalued2[img_devalued < 180 ] = 0
        img_devalued2[img_devalued >= 180 ] = 1
        img_devalued2[img_devalued2 ==0 ] = 255
        img_devalued2[img_devalued2 ==1 ] = 0        
        
        return img_devalued2

    #条件に合う輪郭を探す　オーバーライドする
    def condition_target(self, contour):
        x, y, w, h = cv2.boundingRect(contour)
        #描画する輪郭の条件
        if y < 500 or x < 560 or x > 760:
            return False

        return True

