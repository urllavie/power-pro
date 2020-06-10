from PIL import Image
import cv2
import pyocr
import pyocr.builders
import os

class Ocr:
    def __init__(self, lang='jpn', type='text'):
        path_tesseract ="C:\\Users\\url_l\\AppData\\Local\\Tesseract-OCR"
        if path_tesseract not in os.environ["PATH"]:
           os.environ["PATH"] += os.pathsep + path_tesseract

        tools = pyocr.get_available_tools()
        self.tool = tools[0]
        self.lang = lang
        if type == 'text':
            self.builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        elif type == 'digit':
            # Tesseractが4になってからdigitBuilderが効かないようになってるらしくてつらい...
            # 本当はここで良い感じに数字のみ認識可能になってほしい
            self.builder = pyocr.builders.DigitBuilder(tesseract_layout=6)


    def image_to_string(self, image):
        return self.tool.image_to_string(self.__cv2pil(image), lang=self.lang, builder=self.builder)

    def image_to_number(self, image):
        return self.tool.image_to_string(self.__cv2pil(image), lang=self.lang, builder=self.numbuilder)

    def __cv2pil(self, image):
        new_image = image.copy()
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
        new_image = Image.fromarray(new_image)
        return new_image
