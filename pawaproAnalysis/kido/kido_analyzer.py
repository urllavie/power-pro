import cv2
import numpy as np

class Kido_analyzer:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def analyze(self, frame):
        gray_image = cv2.cvtColor(frame.image, cv2.COLOR_RGB2GRAY)
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame.image)
        gray_image = gray_image[self.y:self.y + self.h, self.x :self.x +self.w]
        img_red_c1 = img_red_c1[self.y:self.y + self.h, self.x :self.x +self.w]
        img_green_c1 = img_green_c1[self.y:self.y + self.h, self.x :self.x + self.w]
        img_blue_c1 = img_blue_c1[self.y:self.y + self.h, self.x :self.x + self.w]
        frame.kido = 1 * np.sum(np.array(gray_image)) / 255
        frame.red = 1 * np.sum(np.array(img_red_c1)) / 255
        frame.blue * np.sum(np.array(img_blue_c1)) / 255
        frame.green = 1 * np.sum(np.array(img_green_c1)) / 255
        frame.image = cv2.merge((img_green_c1,img_blue_c1,img_red_c1))
        return frame

    def update_with_threshold (self, frame, red_flag, green_flag, blue_flag, red_border, green_border, blue_border):
        gray_image = cv2.cvtColor(frame.image, cv2.COLOR_RGB2GRAY)
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame.image)
        #gray_image = gray_image[self.y:self.y + self.h, self.x :self.x +self.w]
        #img_red_c1 = img_red_c1[self.y:self.y + self.h, self.x :self.x +self.w]
        #img_green_c1 = img_green_c1[self.y:self.y + self.h, self.x :self.x + self.w]
        #img_blue_c1 = img_blue_c1[self.y:self.y + self.h, self.x :self.x + self.w]

        if red_flag == True:
            ret,img_red_c1 = cv2.threshold(img_red_c1,red_border,255,cv2.THRESH_BINARY)
        else:
            ret,img_red_c1 = cv2.threshold(img_red_c1,red_border,255,cv2.THRESH_BINARY_INV)
        
        if green_flag == True:
            ret,img_green_c1 = cv2.threshold(img_green_c1,green_border,255,cv2.THRESH_BINARY)
        else:
            ret,img_green_c1 = cv2.threshold(img_green_c1,green_border,255,cv2.THRESH_BINARY_INV)
        
        if blue_flag == True:
            ret,img_blue_c1 = cv2.threshold(img_blue_c1,blue_border,255,cv2.THRESH_BINARY)    
        else:
            ret,img_blue_c1 = cv2.threshold(img_blue_c1,blue_border,255,cv2.THRESH_BINARY_INV)

        frame.image = cv2.merge((img_green_c1,img_blue_c1,img_red_c1))

        frame.kido = 1 * np.sum(np.array(gray_image)) / 255
        frame.red = 1 * np.sum(np.array(img_red_c1)) / 255
        frame.blue * np.sum(np.array(img_blue_c1)) / 255
        frame.green = 1 * np.sum(np.array(img_green_c1)) / 255
        
        return frame

    def image_show(self, frame):
        cv2.imshow("", frame.image)
        cv2.waitKey(100) 


    def get_strike_zone (self, frame):
        gray_image = cv2.cvtColor(frame.image, cv2.COLOR_RGB2GRAY)
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame.image)

        img_red_c1[img_green_c1 > 110] = 0
        img_red_c1[img_red_c1 > 100] = 255
        img_red_c1[img_red_c1 <= 100] = 0
        frame.kido = 1 * np.sum(np.array(gray_image)) / 255
        frame.red = 1 * np.sum(np.array(img_red_c1)) / 255
        frame.blue * np.sum(np.array(img_blue_c1)) / 255
        frame.green = 1 * np.sum(np.array(img_green_c1)) / 255        
        
        return frame