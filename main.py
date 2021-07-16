import pygame
import math
import time
import random

pygame.init()

def len_d(x1,x2,y1,y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2)
    return d
FPS = 60
WITH = 1280
HEIGHT = 720

sc = pygame.display.set_mode((WITH,HEIGHT))
pygame.display.set_caption("Scanner")
pygame.display.update()

RED = (255,0,0)
GREEN = (0,255,0)

angle = 0
revers = 0

arr_x = []
arr_y = []

f1 = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    sc.fill((0,0,0))
    # pygame.display.flip()

    pygame.draw.circle(sc, GREEN,
                       (WITH / 2, HEIGHT), WITH * 0.375, 5)

    text = f1.render("200 cm", False, GREEN)
    place = text.get_rect(
        center=(WITH / 2 + 50, HEIGHT - WITH/2- 20))
    sc.blit(text, place)

    pygame.draw.circle(sc,GREEN,
                       (WITH/2,HEIGHT),WITH/2,5)

    text = f1.render("150 cm", False, GREEN)
    place = text.get_rect(
        center=(WITH / 2 + 50, HEIGHT - WITH *0.375 - 20))
    sc.blit(text, place)

    pygame.draw.circle(sc, GREEN,
                       (WITH / 2, HEIGHT), WITH / 4, 5)

    text = f1.render("100 cm", False, GREEN)
    place = text.get_rect(
        center=(WITH / 2 + 50, HEIGHT - WITH / 4 - 20))
    sc.blit(text, place)

    pygame.draw.circle(sc, GREEN,
                       (WITH / 2, HEIGHT), WITH / 8, 5)

    text = f1.render("50 cm", False, GREEN)
    place = text.get_rect(
        center=(WITH / 2+50, HEIGHT - WITH / 8 - 20))
    sc.blit(text, place)

    pygame.draw.line(sc,GREEN,
                     (WITH/2,HEIGHT),
                     (WITH/2,HEIGHT-WITH/2 - 20),5)


    text = f1.render("90º", False, GREEN)
    place = text.get_rect(
        center=(WITH/2, HEIGHT-WITH/2 - 50))
    sc.blit(text, place)

    x = (-WITH / 2-20) * math.cos(math.radians(30)) + WITH/2
    y = (-WITH / 2-20) * math.sin(math.radians(30)) +HEIGHT

    pygame.draw.line(sc, GREEN,
                     (WITH / 2, HEIGHT),
                     (x, y), 5)

    text = f1.render("30º", False, GREEN)
    place = text.get_rect(
        center=(x-30, y - 20))
    sc.blit(text, place)

    x = (-WITH / 2-20) * math.cos(math.radians(60)) + WITH/2
    y = (-WITH / 2-20) * math.sin(math.radians(60)) +HEIGHT

    pygame.draw.line(sc, GREEN,
                     (WITH / 2, HEIGHT),
                     (x, y), 5)

    text = f1.render("60º", False, GREEN)
    place = text.get_rect(
        center=(x - 10, y - 20))
    sc.blit(text, place)

    x = (-WITH / 2-20) * math.cos(math.radians(120)) + WITH / 2
    y = (-WITH / 2-20) * math.sin(math.radians(120)) + HEIGHT

    pygame.draw.line(sc, GREEN,
                     (WITH / 2, HEIGHT),
                     (x, y), 5)

    text = f1.render("120º", False, GREEN)
    place = text.get_rect(
        center=(x + 10, y - 20))
    sc.blit(text, place)

    x = (-WITH / 2 - 20) * math.cos(math.radians(150)) + WITH / 2
    y = (-WITH / 2 - 20) * math.sin(math.radians(150)) + HEIGHT

    pygame.draw.line(sc, GREEN,
                     (WITH / 2, HEIGHT),
                     (x, y), 5)

    text = f1.render("150º", False, GREEN)
    place = text.get_rect(
        center=(x + 30, y - 10))
    sc.blit(text, place)

    x = (-WITH / 2 - 20) * math.cos(math.radians(angle)) + WITH / 2
    y = (-WITH / 2 - 20) * math.sin(math.radians(angle)) + HEIGHT

    pygame.draw.line(sc, GREEN,
                     (WITH / 2, HEIGHT),
                     (x, y), 5)
    rand = random.randint(0,250)
    arr_x.append((-WITH / 2 - 20+rand) * math.cos(math.radians(angle)) + WITH / 2)
    arr_y.append((-WITH / 2 - 20+rand) * math.sin(math.radians(angle)) + HEIGHT)




    for i in range(0,len(arr_x)):
        pygame.draw.circle(sc,RED,
                           (arr_x[i],arr_y[i]),5)
        if len(arr_x) > 1 and i != 0:
            pygame.draw.line(sc,RED,
                            (arr_x[i-1],arr_y[i-1]),
                             (arr_x[i],arr_y[i]),5)
    if revers == 0:
        angle += 1
    else:
        angle -=1

    if angle >179:
        arr_x.clear()
        arr_y.clear()
        revers = 1
    if angle < 1:
        arr_x.clear()
        arr_y.clear()
        revers = 0



    pygame.display.update()
    time.sleep(0.1)