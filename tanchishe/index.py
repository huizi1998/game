import sys
from tanchishe.Snake import *
from tanchishe.Diamonds import *
from tanchishe.Prop import *
from  tanchishe.jiemian import *
pygame.init()
screen=pygame.display.set_mode((400,600))
#背景图
background=pygame.image.load("picture/index.png").convert()
start= pygame.image.load("picture/开始.gif").convert()
pygame.display.set_caption("贪吃蛇碰方块")
while True:
    screen.blit(background,(0,0))
    screen.blit(start,(68,400))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print("关闭")
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(68,68+265) and event.pos[1] in range(400,400+65):
                jiemian=JieMian()
                jiemian.start()
                print("index关闭")
                pygame.quit()
                sys.exit()
        else:
            pass


    pygame.display.update()