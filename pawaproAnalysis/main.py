from game import Game
from mode.title import Title
from quit_game import Quit_game

#NOTE:入力を求めて（テキスト表示して）プレイヤーが入力するという
#ゲームの流れが書いてあるだけ。すげぇ。
def main():
   
    title='pawaproAnalysis '
    version='1.0.0'
    print (title+'Version '+version)

    game=Game()

    while True:
        print(game.show())
        inp=input()
        if isinstance(game.mode,Quit_game):
            break
        game.next(str(inp))
   
main()


