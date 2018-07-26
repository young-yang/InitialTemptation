# -*- coding: UTF-8 -*-
import random
from settings import *
from piece import Piece
from gameWall import GameWall
import pygame

class GameState():
    def __init__(self,screen):
        self.screen = screen 
        self.wall = GameWall(screen)
        self.piece = None
        self.nextPiece = None
        self.timer_interval = TIMER_INTERVAL
        self.game_score = 0
        #游戏是否停止
        self.stopped = True
        #游戏是否暂停
        self.paused = False
        #游戏是否结束
        self.ended = False
        self.session_count = 0
        
    def set_timer(self,time_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, time_interval)
    
    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)  #传入0表示清除定时器    
    
    def add_score(self,score):
        self.game_score += score
    
    def startGame(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES),self.screen,self.wall)
        self.nextPiece = Piece(random.choice(PIECE_TYPES),self.screen,self.wall)
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
    
    def pauseGame(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)   #传入0表示清除定时器
        self.paused = True
        
    def resumeGame(self):
        self.set_timer(self.timer_interval)
        self.paused = False
    
    def touchBottom(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0,c):
                self.stopped = True
                break
            if not self.stopped:
                self.piece = self.nextPiece
                self.nextPiece = Piece(random.choice(PIECE_TYPES),self.screen,self.wall)
                if self.piece.hit_wall():
                    self.stopped = True
            if self.stopped:
                self.stop_timer()