import pygame as pg
import sys
from random import randint

sc = pg.display.set_mode((600, 600))

pg.draw.rect(sc, (64, 128, 255),
                 (50, 50, 500, 500), 2)
pg.draw.circle(sc, (250, 128, 255), (300, 300), 250, 2)

pg.display.update()

c = 0
ot = 0

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1)

    x = (randint(51, 549))
    y = (randint(51, 549))
    if ((x - 300) ** 2) + ((y - 300) ** 2) < 246 ** 2:
        c += 1
    else:
        ot += 1

    pg.draw.circle(sc, (255, 255, 255), (x, y), 1, 1)

    pg.display.update()
    print(c / max(1, ot))