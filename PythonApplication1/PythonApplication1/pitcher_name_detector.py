from ocr import Ocr
import cv2

class PitcherNameDetector:
    THRESHOLD_VALUE = 50
    THRESHOLD_MAX_VALUE = 255
    X = 965
    Y = 435
    WIDTH = 155
    HEIGHT = 40

    def __init__(self):
        self.ocr = Ocr()

    def detect(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, self.THRESHOLD_VALUE, self.THRESHOLD_MAX_VALUE, cv2.THRESH_BINARY_INV)

        pitch_name_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X : self.X + self.WIDTH]
        pitch_name = self.ocr.image_to_string(pitch_name_image)
        frame1 = cv2.rectangle(image,(self.X,self.Y),(self.X+self.WIDTH,self.Y+self.HEIGHT),(0,255,0),1)
        #cv2.imshow("", frame1)
        #cv2.imshow("", pitch_name_image)
        #cv2.waitKey(3000)    

        print(pitch_name)
        return pitch_name, pitch_name_image
