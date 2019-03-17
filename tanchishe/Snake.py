import pygame
from tanchishe.shenti import *
class Snake:
    def __init__(self,screen,diamonds,prop):
        self.x=190
        self.y=380
        self.head = pygame.image.load("picture/tou.gif").convert()
        self.screen = screen
        self.distance=[]
        self.diamonds=diamonds
        self.prop=prop
        # self.shen=[]
        # self.hen=[]
        self.gao=20
        self.leng=[]
        self.shenList=[]
        self.zuoBiao=[]
        self.fenShu=0
    # def display(self,y):
    #     self.screen.blit(self.head,(self.x, self.y))
    #     l=self.y-y
    #     for s in self.shenList:
    #         s[1]-=l
    #         s[0].display()
    #         s[0].genSui(self.x,s[1])
    def display(self):
        self.screen.blit(self.head,(self.x, self.y))
        for i in self.leng:
            s=ShenTi(self.screen,self.x,self.y+i)
            s.display()
    # def display(self):
    #     self.screen.blit(self.head, (self.x, self.y))
    #     # self.xingZou()
    #     for j in self.shenList:
    #         s=ShenTi(self.screen,j[0],j[1])
    #         s.display()
    #         s.genSui(self.x)
    # def xingZou(self):
    #     for i in self.distance:
    #         x=self.x
    #         y=self.y+i
    #         self.zuoBiao.append([x,y])
    def pProp(self):
        for b in self.prop.startList:
            for i in range(0,b[0]):
                ex=int(b[1][i])
                ey=int(b[3])
                if self.x+10 in range(ex,ex+20) and self.y in range(ey,ey+40):
                    print("吃到道具")
                    for a in range(0,b[2][i]):
                        self.addShen()
                    b[0]-=1
                    b[1].pop(i)
                    b[2].pop(i)

                    break
            # ex= int(self.star.x)
            # ey = int(self.star.y)
            # if b.x   in range(ex-40,ex+40)   and   b.y in range(ey,ey+40):
            #     # print("打中了  哈哈")
            #     self.star.hit=False
            #     self.num=self.num+1
            #     # print(self.num)
            #     break
    def pDiamonds(self):
        for b in self.diamonds.squareList:
            for i in range(0,b[0]):
                ex=int((b[1][i]-1)*80)
                ey=int(b[3])
                if self.x+10 in range(ex,ex+80) and self.y in range(ey,ey+80):
                    print("碰到方块")
                    self.jianShen()
                    self.fenShu+=1
                    # for a in range(0,b[2][i]):
                    #     self.addShen()
                    b[0]-=1
                    b[1].pop(i)
                    b[2].pop(i)

                    break

    def left(self):
        self.x-=5
    def right(self):
        self.x+=5
    def up(self):
        self.y-= 5
    def down(self):
        self.y+=5
    def move(self,x,y):
        self.x=x-10
        self.y=y-10
    # def move(self,x,y):
    #     self.x=x-10
    #     self.y=y-10
    #     bool=True
    #     zu=[]
    #     zu1=[]
    #     for i in self.shenList:
    #         if bool:
    #             zu=i
    #             i[0]=x-10
    #             i[1]=y-10
    #             bool=False
    #         else:
    #             zu1=i
    #             i=zu

    # def addShen(self):
    #     shen=[]
    #     shen.append(ShenTi(self.screen, self.x, self.y+self.gen))
    #     shen.append(self.gen)
    #     self.shenList.append(shen)
    #     self.gen+=20
    # def addShen(self):
    #     n=len(self.shenList)
    #     if n==0:
    #         self.shenList.append([self.x,self.y+20])
    #     else:
    #         last=self.shenList[n-1]
    #         self.shenList.append([last[0],last[1]+20])
    def addShen(self):

        self.leng.append(self.gao)
        self.gao+=20
    def jianShen(self):
        try:
            self.leng.pop()
            self.gao-=20
        except IndexError as e:
            print("结束游戏")
            exit()
        else:
            pass