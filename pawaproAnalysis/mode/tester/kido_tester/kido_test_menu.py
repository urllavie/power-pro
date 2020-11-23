from canvas import Canvas
from quit_game import Quit_game

class Kido_test_menu:

	def draw(self):
		Canvas.store('left','1:輝度テスト開始' + '\n'+\
		 'r:戻る'+ '\n'+\
		 'e:終了')

#NOTE: なるほどぉ。retune　することでどの番号がどこに対応するかは
#わかりやすくなっている。
	def next(self,inp):
		pass
		if   inp=='1':

			from mode.tester.test_menu import Test_menu
			return Test_menu()

		elif inp=='r':
			from mode.tester.test_menu import Test_menu
			return Test_menu()

		elif inp=='e':
			return Quit_game()

		return self