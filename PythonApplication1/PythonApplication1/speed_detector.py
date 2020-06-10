from ocr import Ocr
import cv2
import numpy as np

class SpeedDetector:
    THRESHOLD_VALUE = 225 # 極力ノイズを取って文字認識の結果を安定させる狙いで高めのチューニングにしている
    THRESHOLD_MAX_VALUE = 255
    X = 575
    Y = 626
    WIDTH = 25
    HEIGHT = 50

    def __init__(self):
        self.ocr = Ocr(lang='eng', type='text')

    def detect(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, self.THRESHOLD_VALUE, self.THRESHOLD_MAX_VALUE, cv2.THRESH_BINARY)
        speed_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X : self.X + self.WIDTH * 3]
        cv2.imshow('',speed_image)
        cv2.waitKey(100)
        # 一桁ずつ認識させることで揺らぎ率を下げる狙い
        one_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 0 : self.X + self.WIDTH * 1]
        one_speed = self.__image_to_string(one_image, allow_blank=True)
        two_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 1: self.X + self.WIDTH * 2]
        two_speed = self.__image_to_string(two_image)

        if one_speed == '':
            kd = np.sum(one_image)
            if 5600 < kd and kd < 5900:
                one_speed = '1'
        if two_speed == '8':
            kd = np.sum(two_image)
            if  25754 < kd and kd < 27796:
                two_speed = '0'
        elif two_speed == '9':
            kd = np.sum(two_image)
            if  25754 < kd and kd < 27796:
                two_speed = '0'
            elif  33404 < kd and kd < 34936:
                two_speed = '8'
        elif two_speed == '0':
            kd = np.sum(two_image)
            if  33404 < kd and kd < 34936:
                two_speed = '8'

        if one_speed == '1' and two_speed == '9':
            two_speed = '0'
        elif one_speed == '' and two_speed == '0':
            two_speed = '9'

        three_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 2 : self.X + self.WIDTH * 3]
        three_speed = self.__image_to_string(three_image)
        kd = np.sum(three_image)
        if 28304 < kd and kd < 29326:
            three_speed = '9'
        if three_speed == '9':
            if kd < 25501:
                three_speed = '0'
            elif 30599 < kd and kd < 31621:
                three_speed = '6'
            elif 29834 < kd and kd < 30246:
                three_speed = '3'
            elif 32894 < kd and kd < 33916:
                three_speed = '8'
        if three_speed == '1':
            if 25244 < kd and kd < 25756:
                three_speed = '0'
        if three_speed == '0':
            ke = np.ones((3,3))
            dst = cv2.dilate(three_image, ke)
            kd = np.sum(dst)
            if 48449 < kd and kd < 51256:
                three_speed = '4'




        return one_speed + two_speed + three_speed, speed_image

    def __image_to_string(self, image, allow_blank=False):
        speed = self.ocr.image_to_string(image)
        ke = np.ones((3,3))
        dst = cv2.dilate(image, ke)
        print(np.sum(dst))
#        cv2.imshow('',image)
#        cv2.waitKey(500)
#         kd = np.sum(three_image)

        if allow_blank and speed == '':
            return ''

        # ここはもうパターン列挙で精度を上げにかかる
        # 上手く行かない数字があったらマッピングしてあげる
        if speed.startswith('q', 0) or speed.startswith('0', 0) or speed == 'y' \
            or speed == '9}' or speed == 'Q' or speed == 'iy' or speed =='(oR':
            return '0'
        elif speed == '|' or speed == 'i' or speed == '':
            return '1'
        elif speed.startswith('r', 0) or speed == '=':
            return '2'  
        elif speed.startswith('E', 0) or speed=='os' or speed == '3.':
            return '3'
        elif speed.startswith('u', 0) or speed == 'A' or speed == 'cs' or speed == 'cf' \
            or speed == '“':
            return '4'
        elif speed == '=)' or speed == '3}':
            return '5'
        elif speed == 'J' or speed == ']' or speed == '}':
            return '6'
        elif speed == 'ij':
            return '7'
        elif speed.endswith(')') or speed == 'S' or speed.startswith('io',0) or speed == 'co' \
            or speed == 'oo' or speed == 'Gg' or speed == 'toy' or speed == 'iT' \
            or speed.endswith(':') or speed == '5.': 
            return '9'

        return speed

    def __image_to_string1(self, image, allow_blank=False):

        #kernel = np.ones(3,3)

        speed = self.ocr.image_to_string(image)
        print(np.sum(image))
        cv2.imshow('',image)
        cv2.waitKey(500)
        
        kd = np.sum(image)

        # ここはもうパターン列挙で精度を上げにかかる
        # 上手く行かない数字があったらマッピングしてあげる
        if 5600 < kd and kd < 5900:
            return '1'
        else:
            return ' '

        return ' '
    def __image_to_string2(self, image, allow_blank=False):

        speed = self.ocr.image_to_string(image)
        print(np.sum(image))
        cv2.imshow('',image)
        cv2.waitKey(500)
        
        kd = np.sum(image)

        if 5600 < kd and kd < 5600:
            return '0'
        if 5600 < kd and kd < 5600:
            return '1'
        if 5600 < kd and kd < 5600:
            return '2'
        if 29000 < kd and kd < 31000:
            return '3'
        if 21000 < kd and kd < 22000:
            return '4'
        if 5600 < kd and kd < 5600:
            return '6'
        if 5600 < kd and kd < 5600:
            return '7'
        if 5600 < kd and kd < 5600:
            return '8'
        if 5600 < kd and kd < 5600:
            return '9'
        else:
            return ' '

        return ' '

    def __image_to_string3(self, image, allow_blank=False):

        speed = self.ocr.image_to_string(image)
        print(np.sum(image))
        cv2.imshow('',image)
        cv2.waitKey(500)
        
        kd = np.sum(image)

        if 5600 < kd and kd < 5600:
            return '0'
        if 5600 < kd and kd < 5600:
            return '1'
        if 25245 < kd and kd < 5600:
            return '2'
        if 29000 < kd and kd < 31000:
            return '3'
        if 21000 < kd and kd < 22000:
            return '4'
        if 5600 < kd and kd < 5600:
            return '6'
        if 5600 < kd and kd < 5600:
            return '7'
        if 5600 < kd and kd < 5600:
            return '8'
        if 5600 < kd and kd < 5600:
            return '9'
        else:
            return ' '

        return ' '
