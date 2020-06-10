import cv2 
import numpy as np


def analyze(frame1):
    height, width, channels = frame1.shape
    x = 480
    y = 155
    w = 300
    h = 55
    img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame1)
    img_red_c1 = img_red_c1[y:y + h, x :x +w]
    img_green_c1 = img_green_c1[y:y + h, x :x +w]
    img_blue_c1 = img_blue_c1[y:y + h, x :x +w]
    kido = np.sum(np.array(img_red_c1)) + np.sum(np.array(img_green_c1)) - np.sum(np.array(img_blue_c1))
    return kido
