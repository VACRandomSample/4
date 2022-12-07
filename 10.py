from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode( (400, 250) )
display.fill( THECOLORS["white"] )

#Элипс
draw.ellipse( display, (255, 255, 0),
    (
        (60, 20),
        (210, 190)
    ), 0 )

#Маленький круг
draw.ellipse( display, (240, 30, 30),
    (
        (110, 60),
        (110, 110)
        ), 0 )

#Квадрат
draw.rect( display, (0, 0, 200),
    (
        (130, 100),
        (70, 30)
    ), 0 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
