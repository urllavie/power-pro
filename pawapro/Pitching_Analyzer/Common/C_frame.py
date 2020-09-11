import cv2
import numpy as np

class smallframe:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.kido = 0
        self.red = 0
        self.blue = 0
        self.green = 0
        self.image = image[self.y:self.y + self.h, self.x :self.x +self.w]
        #cv2.imshow("", self.image)
        #cv2.waitKey(10000)  
        self.zone = 0
        self.analyzeKido(image)


    def analyzeKido(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(image)
        gray_image = gray_image[self.y:self.y + self.h, self.x :self.x +self.w]
        img_red_c1 = img_red_c1[self.y:self.y + self.h, self.x :self.x +self.w]
        img_green_c1 = img_green_c1[self.y:self.y + self.h, self.x :self.x + self.w]
        img_blue_c1 = img_blue_c1[self.y:self.y + self.h, self.x :self.x + self.w]

        self.kido = 1 * np.sum(np.array(gray_image)) / 255
        self.red = 1 * np.sum(np.array(img_red_c1)) / 255
        self.blue * np.sum(np.array(img_blue_c1)) / 255
        self.green = 1 * np.sum(np.array(img_green_c1)) / 255

        img_red_c1[img_green_c1 > 110] = 0
        img_red_c1[img_red_c1 > 100] = 255
        img_red_c1[img_red_c1 <= 100] = 0
        self.zone = 1 * np.sum(np.array(img_red_c1))/255


   
        
        


