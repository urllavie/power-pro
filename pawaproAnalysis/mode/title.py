from canvas import Canvas
from quit_game import Quit_game
from mode.pitching.pitching_analyzer_menu import Pitching_analyzer_menu
from mode.tester.test_menu import Test_menu
#from mode.player_list import Player_list

class Title:

	def draw(self):
		Canvas.store('left','1:投球解析' + '\n'+\
		 '9:テスト'+ '\n'
		 'e:終了'+ '\n')

#NOTE: なるほどぉ。retune　することでどの番号がどこに対応するかは
#わかりやすくなっている。
	def next(self,inp):
		pass
		if   inp=='1':
			return Pitching_analyzer_menu()
		if   inp=='9':
			return Test_menu()
		elif inp=='e':
			return Quit_game()

		return self
