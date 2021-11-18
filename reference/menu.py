import pygame


pygame.init()
ck = pygame.display.set_mode((800,600))   #  游戏窗口
pygame.display.set_caption("拳皇双截龙")    #  给窗口取个名 我小时候喜欢双截龙和拳皇
clock = pygame.time.Clock()                         #  游戏刷新速度（我个人这么理解）
start_ck = pygame.Surface(ck.get_size())    #   充当开始界面的画布
start_ck2 = pygame.Surface(ck.get_size())  #  充当第一关的画布界面暂时占位（可以理解为游戏开始了）
start_ck = start_ck.convert()
start_ck2 = start_ck2.convert()
start_ck.fill((255,255,255))  # 白色画布1（开始界面用的）
start_ck2.fill((0,255,0))
# 加载各个素材图片 并且赋予变量名
i1 = pygame.image.load("./images/s1.png")
i1.convert()
i11 = pygame.image.load("./images/s2.png")
i11.convert()

i2 = pygame.image.load("./images/n2.png")
i2.convert()
i21 = pygame.image.load("./images/n1.png")
i21.convert()

i3 = pygame.image.load('./images/m2.png')
i3.convert()
i31 = pygame.image.load('./images/m1.png')
i31.convert()

bg = pygame.image.load('./images/bj.jpg')
bg.convert()







#  以下为选择开始界面鼠标检测结构。
n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 227 and x1 <= 555 and y1 >= 261 and y1 <=327:
        start_ck.blit(i11, (200, 240))
        if buttons[0]:
            n1 = False

    elif x1 >= 227 and x1 <= 555 and y1 >= 381 and y1 <=447:
        start_ck.blit(i21, (200, 360))
        if buttons[0]:
            pygame.quit()
            exit()

    elif x1 >= 227 and x1 <= 555 and y1 >= 501 and y1 <=567:
        start_ck.blit(i31, (200, 480))
    else:
        start_ck.blit(i1, (200, 240))
        start_ck.blit(i2, (200, 360))
        start_ck.blit(i3, (200, 480))


    ck.blit(start_ck,(0,0))
    pygame.display.update()


    # 下面是监听退出动作

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()


ck.blit(start_ck2,(0,0))
pygame.display.update()

#  以下可以写第一关的代码了
n2 = True
while n2:
    clock.tick(30)
    ck.blit(start_ck2, (0, 0))
    start_ck2.blit(bg,(0,0))
    pygame.display.update()
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()



