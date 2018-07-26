# -*- coding: UTF-8 -*-

from settings import *
import pygame

class GameDisplay():
    @staticmethod
    def draw_cell(screen,row,column,color):
        
        cell_position = (column * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         row * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2,CELL_WIDTH -2)
        cell_rect = pygame.Rect(cell_position,cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)
        
    @staticmethod
    def draw_game_area(screen,game_state,game_resource):
        '''绘制游戏区域'''
        for r in range(21):
            pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP + r*CELL_WIDTH),(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP+r*CELL_WIDTH))
        for c in range(11):
            pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT+c*CELL_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT+c*CELL_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGHT))
        
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)
        GameDisplay.draw_next_piece(screen)
        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_end_prompt(screen,game_resource)
            GameDisplay.draw_start_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen,game_resource)
            
    @staticmethod
    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen,r, c, PIECE_COLORS[game_wall.area[r][c]])
    @staticmethod
    def draw_score(screen,score):
        '''绘制游戏得分'''
        score_label_font = pygame.font.Font('simhei.ttc',24)
        score_label_surface = score_label_font.render(u'得分:',False,SCORE_LABEL_COLOR)
        score_label_position = (NEXT_PIECE_LEFT,NEXT_PIECE_BOTTOM + 40)
        screen.blit(score_label_surface,score_label_position)
        
        score_font = pygame.font.SysFont('arial',36)
        score_surface = score_font.render(str(score),False,SCORE_COLOR)
        
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20,score_label_position[1])
        screen.blit(score_surface,score_position)
    
    @staticmethod
    def draw_next_piece(screen):
        #花提示框
        pygame.draw.line(screen, NEXT_PIECE_EDGE, (NEXT_PIECE_LEFT,NEXT_PIECE_TOP),(NEXT_PIECE_RIGHT,NEXT_PIECE_TOP))
        pygame.draw.line(screen, NEXT_PIECE_EDGE, (NEXT_PIECE_LEFT,NEXT_PIECE_BOTTOM),(NEXT_PIECE_RIGHT,NEXT_PIECE_BOTTOM))
        pygame.draw.line(screen, NEXT_PIECE_EDGE, (NEXT_PIECE_LEFT,NEXT_PIECE_TOP),(NEXT_PIECE_LEFT,NEXT_PIECE_BOTTOM))
        pygame.draw.line(screen, NEXT_PIECE_EDGE, (NEXT_PIECE_RIGHT,GAME_AREA_TOP),(NEXT_PIECE_RIGHT,NEXT_PIECE_BOTTOM))
        
    
    @staticmethod
    def draw_start_prompt(screen, game_resource):
        start_tip_position = (GAME_AREA_LEFT - 0.5 * CELL_WIDTH, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)
    
    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        pause_tip_position = (GAME_AREA_LEFT - 0.5 * CELL_WIDTH, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_pausegame_img(), pause_tip_position)
    
    @staticmethod
    def draw_end_prompt(screen, game_resource):
        end_tip_position = (GAME_AREA_LEFT - 0.5 * CELL_WIDTH, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_endgame_img(), end_tip_position)
    