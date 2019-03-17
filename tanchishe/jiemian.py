import pygame
import  time
import sys
from tanchishe.Snake import *
from tanchishe.Diamonds import *
from tanchishe.Prop import *
from tanchishe.Score import *
class JieMian:
    def start(self):

        pygame.init()
        screen=pygame.display.set_mode((400,600))
        #背景图
        background=pygame.image.load("picture/bground.jpg").convert()
        pygame.mixer.music.load('music/bgmusic.mp3')
        # # 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
        pygame.mixer.music.play(-1, 0.0)
        pygame.display.set_caption("贪吃蛇碰方块")
        diamonds=Diamonds(screen)
        prop=Prop(screen)
        snake=Snake(screen,diamonds,prop)
        while True:
            screen.blit(background,(0, 0))
            snake.display()
            diamonds.display()
            prop.display()
            snake.pProp()
            snake.pDiamonds()
            score = Score(screen, snake.fenShu)
            for i in prop.startList:
                # if i[3]>300 and i[3]<301:
                if i[3]==300:
                    bool=True
                    break
                else:
                    bool=False
            if bool:
                prop.creat()
            prop.remove()
            for j in diamonds.squareList:
                # if j[3]>200 and j[3]<201:
                if j[3]==200:
                    bool=True
                    break
                else:
                    bool=False
            if bool:
                diamonds.creat()
            diamonds.move()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print("关闭")
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                        snake.left()
                        print("左")
                    elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                        snake.right()
                        print("右")
                    elif event.key==pygame.K_w or event.key==pygame.K_UP:
                        snake.up()
                        print("上")
                    elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                        snake.down()
                        print("下")
                    elif event.key==pygame.K_SPACE:
                        snake.addShen()
                    else:
                        pass
                elif event.type==pygame.MOUSEMOTION:
                    snake.move(event.pos[0],event.pos[1])
                    y=event.pos[1]

            pygame.display.update()

