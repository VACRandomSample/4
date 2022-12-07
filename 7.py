from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode((250, 200))
display.fill(THECOLORS["white"])

#Крyr
pg.draw.circle( display, (255, 255, 0), 
    (130, 90), 
    70 )

#Глаза
draw.circle( display, (0, 70, 255), (100, 60), 8 )
draw.circle( display, (0, 140, 255), (100, 60), 5 )
draw.circle( display, (0, 70, 255), (160, 60), 8 )
draw.circle( display, (0, 140, 255), (160, 60), 5 )

#Нос
draw.polygon( display, (0, 160, 100), 
    (
        (100, 80),
        (160, 80),
        (130, 105)
    ), 0 )


#Рот
draw.rect( display, (255, 0, 0),
    (80, 110, 85, 10)
, 0 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
