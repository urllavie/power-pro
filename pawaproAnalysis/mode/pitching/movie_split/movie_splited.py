from canvas import Canvas
import os
import cv2

class Movie_splited:

	def __init__(self, dir_splited, movie, v, file_no):
    # 動画ファイル保存用の設定
		self.fps = int(v.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
		self.vw = int(v.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
		self.vh = int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
		self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
		self.file_path = dir_splited + movie.filename_without_extension + '-' + str(file_no).zfill(2) +'.mp4'
		self.video = cv2.VideoWriter(self.file_path, self.fourcc, self.fps, (self.vw, self.vh), True)


	def write_image(self, image):
		self.video.write(image)
