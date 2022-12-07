from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((500, 400))
display.fill(THECOLORS["blue"])

#Голова
pg.draw.ellipse(display, (160, 255, 255), 
    (
        (63, 70),
        (63, 50)
    ),0)

#Треугольник
pg.draw.polygon(display, (0, 180, 80),
    (
        (60, 70),
        (130, 70),
        (95, 15)
    ),0)

#Тело(часть 1)
pg.draw.ellipse(display, (160, 255, 255),
    (
        (45, 105),
        (100, 95)
    ),0)

#Тело(часть 2)
pg.draw.ellipse(display, (160, 255, 255),
    (
        (15, 180),
        (160, 130)
    ),0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()
