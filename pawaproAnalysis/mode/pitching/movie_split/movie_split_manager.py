from canvas import Canvas
import glob
import shutil 
import os
from mode.pitching.movie_split.movie_spliter import Movie_spliter
from mode.pitching.movie_split.movie import Movie

class Movie_split_manager:
	def __init__(self):
		self.dir_input = os.getcwd() + '\\mode\\pitching\\DATA_INPUT\\'
		self.dir_output = os.getcwd() + '\\mode\\pitching\\DATA_ROW\\'
		self.dir_splited = os.getcwd() + '\\mode\\pitching\\DATA_SPLITED\\'

	def split_main(self):

		file_path_list = glob.glob(self.dir_input + '*.mp4')
		movies = []

		for file_path in file_path_list:
			movies.append(Movie(file_path))


		movie_spliter = Movie_spliter(self.dir_splited)
		for movie in movies:
			movie_spliter.split(movie)
			shutil.move(movie.file_path, self.dir_output + movie.filename)

