from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((400, 300))
display.fill(THECOLORS["white"])

#Стенa
rect_ = pg.Rect(110, 110, 160, 160)
draw.rect(display, 
    (
        200,
        200,
        200
    ), rect_, 0)

#Крыша
draw.polygon(display, (0, 0, 210), 
    (
        (110, 110),
        (270, 110),
        (190, 35)
    ), 0)

#Дверь
draw.rect(display, (250, 250, 0), 
    (
        120,
        170,
        45,
        100
    ), 0)

#Окно
draw.rect(display, (0, 180, 80),
    (
        200,
        140,
        50,
        65
    ),0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
