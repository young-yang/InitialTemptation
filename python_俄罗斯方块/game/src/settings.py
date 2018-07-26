# -*- coding: UTF-8 -*-

#窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_WIDTH = 26.7
#游戏区域
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAME_AREA_HEIGHT = CELL_WIDTH * 20
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_TOP = (SCREEN_HEIGHT - GAME_AREA_HEIGHT) //2
COLUMN_NUM = 10
LINE_NUM = 20
WALL_BLANK_LABEL = '-'
#提示框区域
NEXT_PIECE_LEFT = GAME_AREA_LEFT+ COLUMN_NUM * CELL_WIDTH + 80
NEXT_PIECE_RIGHT = GAME_AREA_LEFT+ COLUMN_NUM * CELL_WIDTH + 80 + CELL_WIDTH * 4
NEXT_PIECE_TOP = GAME_AREA_TOP
NEXT_PIECE_BOTTOM =  GAME_AREA_TOP + CELL_WIDTH * 4

#定时器
TIMER_INTERVAL = 1000
#颜色定义
EDGE_COLOR = (0,0,0)
CELL_COLOR = (230,230,230)
BACKGROUND_COLOR = (230,230,230)
NEXT_PIECE_EDGE = (100,100,100)
PIECE_COLORS = {
    'S' : (0,255,128),
    'Z' : (255,128,255),
    'J' : (128,0,255),
    'L' : (0,0,255),
    'I' : (255,255,0),
    'O' : (255,0,0),
    'T' : (255,128,0)
}
SCORE_LABEL_COLOR = (120,120,120)
SCORE_COLOR = (120,120,120)
#方块形状定义
PIECE_TYPES = ['S','Z','T','L','J','O','I']
S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.',
                     '....']]

J_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     'OO..',
                     '....'],
                    ['O...',
                     'OOO.',
                     '....',
                     '....'],
                    ['.OO.',
                     '.O..',
                     '.O..',
                     '....'],
                    ['....',
                     'OOO.',
                     '..O.',
                     '....']]
L_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.OO.',
                     '....'],
                    ['....',
                     'OOO.',
                     'O...',
                     '....'],
                    ['OO..',
                     '.O..',
                     '.O..',
                     '....'],
                    ['..O.',
                     'OOO.',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['.OO.',
                     '.OO.',
                     '....',
                     '....']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..',
                     '....']]

T_SHAPE_TEMPLATE = [['.O..',
                     'OOO.',
                     '....',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '.O..',
                     '....'],
                    ['....',
                     'OOO.',
                     '.O..',
                     '....'],
                    ['.O..',
                     'OO..',
                     '.O..',
                     '....']]

I_SHAPE_TEMPLATE = [['....',
                     'OOOO',
                     '....',
                     '....'],
                    ['.O..',
                     '.O..',
                     '.O..',
                     '.O..']]

PIECES = {'S' : S_SHAPE_TEMPLATE,
          'J' : J_SHAPE_TEMPLATE,
          'L' : L_SHAPE_TEMPLATE,
          'O' : O_SHAPE_TEMPLATE,
          'Z' : Z_SHAPE_TEMPLATE,
          'T' : T_SHAPE_TEMPLATE,
          'I' : I_SHAPE_TEMPLATE}
