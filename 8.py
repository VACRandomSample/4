from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode( (250, 250) )
display.fill( THECOLORS["white"] )

#Звезда
draw.polygon( display, (220, 30, 30), 
    (
        (80, 180),
        (100, 130),
        (50, 97),
        (110, 95),
        (130, 40),
        (150, 95),
        (210, 97),
        (160, 130), 
        (180, 180), 
        (130, 150)
    ), 0 )

#Кирпич
draw.rect( display, (255, 255, 0),
    (
        50, 180, 170, 40
    ), 0)

#Кружок
draw.circle( display, (0, 200, 120),
    (130, 35), 
    12 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
