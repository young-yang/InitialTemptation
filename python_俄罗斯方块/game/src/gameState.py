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
        self.timer_interval = TIMER_INTERVAL
        self.game_score = 0
        #游戏是否停止
        self.stopped = True
        #游戏是否暂停
        self.paused = False
        
    def set_timer(self,time_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, time_interval)
    
    def add_score(self,score):
        self.game_score += score
    
    def startGame(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES),self.screen,self.wall)
    
    def pauseGame(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)   #传入0表示清除定时器
        self.paused = True
        
    def resumeGame(self):
        self.set_timer(self.timer_interval)
        self.paused = False
        