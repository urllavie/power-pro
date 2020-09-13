from canvas import Canvas
from quit_game import Quit_game
from mode.pitching.movie_split.movie_split_menu import Movie_split_menu

class Pitching_analyzer_menu:

	def draw(self):
		Canvas.store('left','1:動画切り分け処理' + '\n'+\
		 'r:戻る'+ '\n'+\
		 'e:終了')

#NOTE: なるほどぉ。retune　することでどの番号がどこに対応するかは
#わかりやすくなっている。
	def next(self,inp):
		pass
		if   inp=='1':
			return Movie_split_menu()

		elif inp=='r':
			from mode.title import Title
			return Title()

		elif inp=='e':
			return Quit_game()

		return self
