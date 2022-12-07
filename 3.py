from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((300, 300))
display.fill(THECOLORS["white"])

#Фон
rect_ = Rect(0, 0, 250, 250)
draw.rect(display, (200, 0, 5), rect_, 0)

#Желтый треугольник
draw.polygon(display, (255, 255, 0), 
    (
        (40, 60),
        (180, 210),
        (40, 210)
    ), 0)

#Кружок
draw.circle(display, (0, 180, 80), (110, 130), 30)

#Синий треугольник
draw.polygon(display, (0, 145, 255), 
    (
        (40, 60),
        (180, 60),
        (180, 210)
    ),0)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()
