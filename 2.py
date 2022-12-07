from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((300, 350))
display.fill(THECOLORS["white"])

r = Rect( 20, 20, 260, 310 )
draw.rect( display, (60, 0, 255), r, 0 )

draw.rect( display, (0, 0, 0), 
    (
        37, 
        230, 
        20, 
        80
    ), 0 )
draw.ellipse( display, (0, 180, 80), 
    (
        25, 
        210, 
        45, 
        40
    ), 0 )

draw.ellipse( display, (0, 180, 80), 
    (
        110, 
        30, 
        90, 
        80
    ), 0 )
draw.rect( display, (0, 0, 0), 
    (
        140, 
        70, 
        10, 
        190
    ), 0)

draw.rect( display, (0, 0, 0), 
    (
        220, 
        190, 
        22, 
        95
    ), 0 )
draw.ellipse( display, (0, 180, 80), 
    (
        205, 
        170, 
        52, 
        45), 0 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()