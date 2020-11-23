import cv2 
from kido.kido_analyzer import Kido_analyzer
from kido.frame import Frame
from mode.pitching.movie_split.movie_splited import Movie_splited

class Movie_spliter:

	def __init__(self, dir_splited):
		self.dir_splited = dir_splited
		self.kido_analyzer = Kido_analyzer(580, 450, 125, 130)
		self.kido_border = 500

		

	def split(self, movie):
		n_file = 0

		v = cv2.VideoCapture(movie.file_path)
		write_flag = False
		
		while (v.isOpened()):
			r,image = v.read()
			if  (r == False):
				v.release()
				break

			frame = Frame(image)
			frame = self.kido_analyzer.analyze(frame)
			strike_zone = self.kido_analyzer.get_strike_zone(frame)
			#self.kido_analyzer.image_show(frame)
			#print(strike_zone.red)

			if write_flag == False and frame.red < self.kido_border:
				n_file += 1
				movie_splited = Movie_splited(self.dir_splited, movie, v, n_file)
				print(movie_splited.file_path)
				write_flag = True

			if write_flag == True and frame.red >= self.kido_border:
				write_flag = False

			if write_flag == True:
				movie_splited.write_image(image)











