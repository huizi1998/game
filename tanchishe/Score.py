import pygame
class Score:
    def __init__(self,screen,fenShu):
        self.fenShu=fenShu
        self.screen=screen
        self.x=0
        self.y=0
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 128)
        # 通过字体文件获得字体对象（字体，大小）
        fontObj = pygame.font.Font('music/chinese.stsong.ttf', 40)
        # 配置要显示的文字+背景色
        textSurfaceObj = fontObj.render("分数："+str(self.fenShu), True, BLUE)
        # 配置要显示的文字
        # textSurfaceObj = fontObj.render('Pygame', True, GREEN)
        # 获得要显示的对象的rect
        textRectObj = textSurfaceObj.get_rect()
        # 设置显示对象的坐标
        textRectObj.center = (80,20)
        # 绘制字体
        screen.blit(textSurfaceObj,textRectObj)
