import cv2
import numpy as np

class Detector(object):
    def __init__(self):
        self.smallest_area = 10
        self.biggest_area = 1000


    def detect(self, frame):
        #グレースケールの変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
        #二値化
        devalued_img = self.devalued(frame)

        #輪郭の検出
        contours, hierarchy = cv2.findContours(devalued_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
        # 各輪郭に対する処理
        detect_count = 0
        targetc =[]
        for i in range(0, len(contours)):

            # 輪郭の領域を計算
            area = cv2.contourArea(contours[i])
            # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
            if area < self.smallest_area or self.biggest_area < area:
                continue
            #フレーム内では条件にあう輪郭
            if self.condition_target(contours[i]) == True :           
                detect_count += 1
                targetc.append(contours[i])
        
        #条件に合う輪郭がなければ終了
        if len(targetc) == 0:
            return False, None

        target = self.select_target(targetc)

        return True, target
    
    #条件にあった輪郭の中で最も条件にあうもの選択する
    def select_target(self, contours):
        pass



    #二値化用関数　オーバーライドする
    def devalued(self,frame):
        pass

    #条件に合う輪郭を探す　オーバーライドする
    def condition_target(self, contour):
        pass



