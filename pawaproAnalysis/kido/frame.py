import cv2
import numpy as np

class Frame:

    def __init__(self, image):
        self.kido = 0
        self.red = 0
        self.blue = 0
        self.green = 0
        self.image = image
