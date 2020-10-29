import pygame, sys
from pygame.locals import *
from src.config.display import BACKGROUND_COLOR, WIDTH, HEIGHT
from src.core.dice import Dice
from src.config.dice import DICE_SIZE, DICE_PADDING, DICE_SPACING, DICE_INITIAL_HEIGHT, DICE_KEEP_ZONE
from src.core.button import Button
from src.config.button import BUTTON_WIDTH, BUTTON_HEIGHT
from src.config.color import GREEN, DARK_GREEN
import time

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    
    keep_zone = []
    all_dices = []
    for position in range(5):
        dice_position = (DICE_SIZE+DICE_SPACING)*position + DICE_PADDING

        all_dices.append(
            Dice(DISPLAY, (dice_position, DICE_INITIAL_HEIGHT)))

    button_roll = Button(GREEN, (WIDTH/2-BUTTON_WIDTH/2,300),
                        (BUTTON_WIDTH, BUTTON_HEIGHT), 'Roll Dices')

    while True:
        DISPLAY.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_roll.isOver(mouse_pos):
                    [dice.throw_the_dice() for dice in all_dices if dice not in keep_zone]

                for dice in all_dices:
                    if dice.isOver(mouse_pos):
                        if dice not in keep_zone:
                            keep_zone.append(dice)
                        else:
                            keep_zone.remove(dice)

            if event.type == pygame.MOUSEMOTION:
                if button_roll.isOver(mouse_pos):
                    button_roll.color = DARK_GREEN
                else:
                    button_roll.color = GREEN

        button_roll.draw(DISPLAY, (0,90,0))
        
        i, j = 0, 0
        for dice in all_dices:
            if dice not in keep_zone:
                dice_position = (DICE_SIZE+DICE_SPACING)*i + DICE_PADDING
                dice.position = (dice_position, DICE_INITIAL_HEIGHT)
                dice.draw()
                i += 1
            if dice in keep_zone:
                dice_position = (DICE_SIZE+DICE_SPACING)*j + DICE_PADDING
                dice.position = (dice_position, DICE_KEEP_ZONE)
                dice.draw()
                j += 1

            
        pygame.display.update()

main()
