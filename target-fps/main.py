# Copyright(C), 2020-2020,  Co.,Ltd.
# FileName : main.py
# Author : lvyandi
# Version : 0.10
# Date : 2020/5/19 15:15
# Description :
import random
import sys

import pygame



size = width, height = 600, 600 # 设置窗口大小
halfsize = int(width/2), int(height/2)

fps = 30  # 刷新频率
black = (0,0,0)  # 背景色
offset = [0, 0]  # x, y 偏移量

mouse_sensitivity = 2  # 灵敏度
aim_point_dia = 20  # 准心外圈直径

frame = 0  # 刷新次数

targetColor = [62, 61, 50]
game_font = pygame.font.SysFont('宋体', 16, True)  # 字体


pygame.init()
screencaption=pygame.display.set_caption('~')
screen=pygame.display.set_mode(size)

clock = pygame.time.Clock()

targets = [
    [(0,0), 100] # 坐标 生命值
]  # 靶子列表

def random_current_coordinates(scope=(600, 600)):  # 随机生成坐标
    return (random.randint(1,scope[0]),random.randint(1,scope[1]))

targets.append([random_current_coordinates(size),100])


while True:

    clock.tick(fps)
    screen.fill(black)

    pygame.mouse.set_pos = halfsize
    pygame.mouse.set_visible(False)  # 鼠标不可见

    mouse_move = (0, 0)

    pygame.event.set_grab(True)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if frame:
                mouse_move = event.rel
                mouse_move = tuple([x*mouse_sensitivity for x in mouse_move])


            if mouse_move != (0, 0):
                offset[0] -= mouse_move[0]
                offset[1] -= mouse_move[1]

        if event.type == pygame.MOUSEBUTTONDOWN:  # 获取点击鼠标事件
            if event.button == 1:  # 点击鼠标左键
                aim_point_dia = int(aim_point_dia/2)





            elif event.button == 2:
                aim_point_dia = 2
            elif event.button == 3:
                aim_point_dia = 2
        if event.type == pygame.MOUSEBUTTONUP:  # 获取松开鼠标事件
            if event.button == 1:  # 松开鼠标左键
                aim_point_dia = 20
            elif event.button == 2:
                aim_point_dia = 20
            elif event.button == 3:
                aim_point_dia = 20

    for target in targets[1:]:
        distance = 2

        target_x, target_y = target[0]
        circle_x = target_x + offset[0]
        circle_y = target_y + offset[1]

        pole_x = target_x + offset[0] - 2
        pole_y = target_y + offset[1] + 18


        # draw a target

        for x in range(1,11,2):
            diameter = distance * 2 * x  # 直径
            pygame.draw.circle(screen, targetColor, [circle_x, circle_y], diameter, 1)
            print('ciryle in ',circle_x, circle_y)
        # draw a pole
        rect_list = [pole_x,pole_y, 4, 200]
        pygame.draw.rect(screen, targetColor, rect_list, 0)
        # draw 血条



    # draw aim point
    circle_xy = [width/2]
    pygame.draw.circle(screen, targetColor, halfsize, 2, 1)
    pygame.draw.circle(screen, targetColor, halfsize, aim_point_dia, 1)

    screen.blit(game_font.render(u'当前已刷新帧数：%d' % frame, True, [255, 0, 0]), [20, 20])
    pygame.display.update()

    frame += 1




