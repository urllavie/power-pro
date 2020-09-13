from canvas import Canvas
from mode.title import Title
#NOTE:このクラスはmenuを把握してinpを渡している。
#そして次のシーンを受け取っているのか、、、
class Game:
    
    def __init__(self):
        self.mode=Title()
        
#self.modeはインスタンスなのか、気付かなかったーー！
    def next(self,inp):
        self.mode=self.mode.next(inp)


    def show (self):
        self.mode.draw()
        return Canvas.show()
        

    
