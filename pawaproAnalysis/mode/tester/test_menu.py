from canvas import Canvas
from quit_game import Quit_game
from mode.tester.kido_tester.kido_test_menu import Kido_test_menu

class Test_menu:

	def draw(self):
		Canvas.store('left','1:輝度テスト' + '\n'+\
		 'r:戻る'+ '\n'+\
		 'e:終了')

#NOTE: なるほどぉ。retune　することでどの番号がどこに対応するかは
#わかりやすくなっている。
	def next(self,inp):
		pass
		if inp=='1':
			return Kido_test_menu()

		elif inp=='r':
			from mode.title import Title
			return Title()

		elif inp=='e':
			return Quit_game()

		return self
