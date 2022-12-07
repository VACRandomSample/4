from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((250, 300))
display.fill(THECOLORS["white"])

#Крyr
draw.circle(display, (220, 0, 0), 
    (130, 190)
    , 70)

#Многоу-ик(внутри)
draw.polygon(display, (255, 255, 0),
    (
        (90, 190),
        (130, 220),
        (170, 190),
        (130, 160)
    ), 0)

#Многоу-ик(снаружи)
draw.polygon(display, (0, 160, 160), 
    (
        (100, 126),
        (160, 126),
        (170, 80),
        (130, 50),
        (90, 80)
    ), 000)
draw.polygon(display, (0, 0, 255), 
    (
        (100, 126),
        (160, 126),
        (170, 80),
        (130, 50),
        (90, 80)
    ), 5)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
