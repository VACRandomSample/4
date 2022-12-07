from pygame import draw, display as dp, Rect
from pygame.color import THECOLORS
import pygame as pg
import sys

pg.init()
display = dp.set_mode(( 300, 500 ))
display.fill( THECOLORS["white"] )

react_ = Rect( 100, 100, 120, 150 )
draw.rect( display, (255, 0, 40), react_, 0 )

draw.polygon( display, (255, 0, 40), (
    (80, 250), 
    (240, 250), 
    (160, 350) 
    ), 0 )
draw.polygon( display, (40, 0, 255), ( 
    (80, 100), 
    (240, 100), 
    (160,60) 
    ), 0 )

draw.circle( display, (0, 180, 80), 
    (160, 300)
    , 50 )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()

        
