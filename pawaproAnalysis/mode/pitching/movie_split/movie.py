from canvas import Canvas
import os
import cv2

class Movie:

	def __init__(self, filepath):
		self.filename = os.path.basename(filepath)
		self.filename_without_extension = os.path.splitext(self.filename)[0]
		self.file_path =filepath

