import pygame

class GameResource():
    def __init__(self):
        self.img_path = '../images/'
        self.newgame_img = None
        self.pausegame_img = None
        self.gameover_img = None
        
    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + "press-s-newgame.png").convert_alpha()
        return self.newgame_img
    
    def load_pausegame_img(self):
        if not self.pausegame_img:
            self.pausegame_img = pygame.image.load(self.img_path + "press-p-pausegame.png").convert_alpha()
        return self.pausegame_img
    
    def load_endgame_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.img_path + "endgame.png").convert_alpha()
        return self.gameover_img