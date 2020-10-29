from typing import Tuple
import pygame
from random import randint
from src.pictures.pictures import DICE1, DICE2, DICE3, DICE4, DICE5, DICE6


class Dice:
    def __init__(self, display, position:Tuple[int]):
        self.display = display
        self.position = position
        self.dice = [
                    pygame.image.load(DICE1),
                    pygame.image.load(DICE2),
                    pygame.image.load(DICE3),
                    pygame.image.load(DICE4),
                    pygame.image.load(DICE5),
                    pygame.image.load(DICE6)
                    ]
        self.width = 100 #pixels
        self.height = 100 #pixels
        self.value = self.dice[randint(1,6)-1]

    def throw_the_dice(self):
        self.value = self.dice[randint(1,6)-1]
    

    def draw(self):
        self.display.blit(self.value, self.position)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.position[0] and pos[0] < self.position[0] + self.width:
            if pos[1] > self.position[1] and pos[1] < self.position[1] + self.height:
                return True
            
        return False