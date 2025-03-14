import pygame
import time

pygame.init()

rect_color = (255,0,0)

# makes a window that is 600x600 pixels
window = pygame.display.set_mode((600,600))
x = 30

exit = False

while not exit:
    if (x != 600):
        x += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    
    time.sleep(.1)
    pygame.draw.rect(window, rect_color,
                     pygame.Rect(x,30,60,60))

    pygame.display.update()
    

