# -*- coding: UTF-8 -*-
import sys
import pygame
import time
import random

from piece import Piece
from settings import *
from gameWall import GameWall
from gameState import GameState
from gameDisplay import GameDisplay
from gameResource import GameResource

def main():
    #初始化pygame
    pygame.init()
    #创建屏幕对象
    #设置分辨率
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #设置窗口
    pygame.display.set_caption("俄罗斯方块")
    #让按键看起来更连续一些
    pygame.key.set_repeat(10,100)
    #背景颜色RGB
    bg_color = BACKGROUND_COLOR
    random.seed(int(time.time()))
    game_state = GameState(screen)
    game_resource = GameResource()
    #游戏主循环
    while True:
        #判断方块是否落在最底部
        if game_state.piece and game_state.piece.is_on_bottom:
            game_state.touchBottom()
        check_events(game_state)
        #设置屏幕背景颜色
        screen.fill(bg_color)
        #绘制游戏区域，网格线和墙体
        GameDisplay.draw_game_area(screen, game_state,game_resource)
        if game_state.piece:
            game_state.piece.paint()
        #刷新屏幕
        pygame.display.flip()

def check_events(game_state):
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        #关闭窗口对事件
        if event.type == pygame.QUIT:
            sys.exit()
        #键盘按键事件处理
        elif event.type == pygame.KEYDOWN:
            onKeyDown(event, game_state)
        elif event.type == pygame.USEREVENT:
            if game_state.piece:
                game_state.piece.move_down()
            
def onKeyDown(event,game_state):
    if not game_state.paused and event.key == pygame.K_DOWN:
        if game_state.piece:
            game_state.piece.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        if game_state.piece:
            game_state.piece.turn()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        if game_state.piece:
            game_state.piece.move_left()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        if game_state.piece:
            game_state.piece.move_right()
    elif not game_state.paused and event.key == pygame.K_SPACE:
        if game_state.piece:
            game_state.piece.fall_down()
    #按下S键开始游戏
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.startGame() 
    #按下P键暂停游戏
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resumeGame()
        else :
            game_state.pauseGame()

if __name__ == "__main__":
    main()
    
    