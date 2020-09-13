from canvas import Canvas
from quit_game import Quit_game
from mode.pitching.movie_split.movie_split_manager import Movie_split_manager

class Movie_split_menu:

	def draw(self):
		Canvas.store('left','1:処理開始' + '\n'+\
		 'r:戻る'+ '\n'+\
		 'e:終了')

#NOTE: なるほどぉ。retune　することでどの番号がどこに対応するかは
#わかりやすくなっている。
	def next(self,inp):
		pass
		if   inp=='1':
			movie_split_manager = Movie_split_manager()			
			movie_split_manager.split_main()
			from mode.pitching.pitching_analyzer_menu import Pitching_analyzer_menu
			return Pitching_analyzer_menu()

		elif inp=='r':
			from mode.pitching.pitching_analyzer_menu import Pitching_analyzer_menu
			return Pitching_analyzer_menu()

		elif inp=='e':
			return Quit_game()

		return self