# Copyright(C), 2020-2020,  Co.,Ltd.
# FileName : main.py
# Author : lvyandi
# Version : 0.10
# Date : 2020/5/19 15:15
# Description :


import sys

import pygame



size = width, height = 600, 600 # 设置窗口大小
fps = 30  # 刷新频率
black = (0,0,0)  # 背景色
offset = [0, 0]  # x, y 偏移量

mouse_sensitivity = 1



pygame.init()
screencaption=pygame.display.set_caption('~')
screen=pygame.display.set_mode(size)

clock = pygame.time.Clock()



while True:

    clock.tick(fps)
    screen.fill(black)

    pygame.mouse.set_pos = (width / 2, height / 2)
    mouse_move = (0, 0)

    pygame.event.set_grab(True)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_move = event.rel
            if mouse_move != (0, 0):
                print(mouse_move)
                offset[0] -= mouse_move[0]
                offset[1] -= mouse_move[1]
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0:
                        print('left')
                    elif index == 1:
                        print('the mouse wheel pressed')
                    elif index == 2:
                        print('right')


    distance = 2 # 圆直径
    # draw a target
    targetColor = [62,61,50]

    circle_x = int(width/2) + offset[0]
    circle_y = int(height/2) + offset[1]

    pole_x = int(width/2) + offset[0] - 2
    pole_y = int(height/2) + offset[1] + 18

    for x in range(1,11):
        diameter = distance * 2 * x
        pygame.draw.circle(screen, targetColor, [circle_x, circle_y], diameter, 1)

    # draw a pole
    rect_list = [pole_x,pole_y, 4, 200]
    pygame.draw.rect(screen, targetColor, rect_list, 0)


    pygame.display.update()



