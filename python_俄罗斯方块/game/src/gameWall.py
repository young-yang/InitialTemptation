# -*- coding: UTF-8 -*-

from settings import *
'''游戏区墙体类。记住落到底部的方块组成对墙'''
class GameWall():
    def __init__(self,screen):
        #游戏开始时，游戏区域20*10个格子被‘-’符号填充
        self.screen = screen
        self.area = [ ]
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])
            
    def print(self):
        print(len(self.area),"rows",len(self.area[0]),"columns")
        for line in self.area:
            print(line)
    
    def add_to_wall(self,piece):
        #把piece放入墙中
        shape_turn = PIECES[piece.shape][piece.turn_times]
        #r表示行号，c表示列号
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell(piece.y+r,piece.x+c,piece.shape)
    
    def set_cell(self,row,column,shape_label):
        '''把r行c列的格子上搭上方块记号（如S，L，。。。），因为该格子被此方块占据'''
        self.area[row][column] = shape_label
    
    def is_wall(self, row, column):
        return self.area[row][column] != WALL_BLANK_LABEL
    
    def eliminate_lines(self):
        #消行.如果一行没有空白单元格，就应该取消该行，返回得分。
        '''
        计分规则：
        消掉一行：0分
        消掉两行：100分
        消掉三行：400分
        消掉四行：800分
        '''
        #需要消除哪几行
        lines_eliminated = [ ]
        for r in range(LINE_NUM) :
            if self.is_full(r):
                lines_eliminated.append(r)
            
        for r in lines_eliminated:
            self.copy_down(r)
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL
        eliminated_num = len(lines_eliminated)
        assert(eliminated_num <= 4 and eliminated_num >= 0)
        if eliminated_num < 3:
            score = eliminated_num * 100
        elif eliminated_num == 3:
            score = 400
        else:
            score = 800
        return score
        
    def is_full(self,row):
        '''下标为row的一行满了吗'''
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False
        return True
    
    def copy_down(self,row):
        for r in range(row,0,-1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r-1][c]
                
    def clear(self):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                self.area[r][c] = WALL_BLANK_LABEL