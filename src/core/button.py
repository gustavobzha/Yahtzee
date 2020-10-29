from typing import Tuple
import pygame

class Button():
    def __init__(self, color, position:Tuple[int], size:Tuple[int], text=''):
        self.color = color
        self.position_x = position[0]
        self.position_y = position[1]
        self.width = size[0]
        self.height = size[1]
        self.text = text

    def draw(self,display,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(display, outline, (self.position_x-2,self.position_y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(display, self.color, (self.position_x,self.position_y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            display.blit(text, (self.position_x + (self.width/2 - text.get_width()/2), self.position_y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.position_x and pos[0] < self.position_x + self.width:
            if pos[1] > self.position_y and pos[1] < self.position_y + self.height:
                return True
            
        return False