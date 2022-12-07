from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode( (400, 300) )
display.fill( THECOLORS["white"] )
#Ромб
draw.polygon( display, (0, 180, 90),
    (
        (100, 100),
        (200, 180),
        (300, 100),
        (200, 20)
    ), 0 )

#Стрелка слева
draw.polygon( display, (240, 30, 30),
    (
        (170, 100),
        (90, 50),
        (90, 150)
        ), 0 )
draw.rect( display, (240, 30, 30),
    (
        (10, 75),
        (80, 50)
    ), 0 ) 

#Стрелка справа
draw.polygon( display, (255, 255, 0),
    (
        (250, 50),
        (250, 150),
        (170, 100)
    ), 0 )
draw.rect( display, (255, 255, 0),
    (
        (240, 75),
        (75, 50)
    ), 0 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()