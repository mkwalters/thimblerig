

import pygame

pygame.init()


dimensions = (800,600)

cup_color = (255,253,130)

gameDisplay = pygame.display.set_mode(dimensions)
gameDisplay.fill((27,153,139))

pygame.display.set_caption('thimblerig')

pygame.draw.circle(gameDisplay, cup_color, (dimensions[0] / 4, dimensions[1] / 2), 50)
pygame.draw.circle(gameDisplay, cup_color, ( dimensions[0] / 2, dimensions[1] / 2), 50)
pygame.draw.circle(gameDisplay, cup_color, ( 3 * dimensions[0] / 4, dimensions[1] / 2), 50)

clock = pygame.time.Clock()

still_playing = True


# class Cup
    
#     def __init__(self)

#         self.color = (255,0,0) #red
#         self.position = (dimensions[0] / 3, dimensions[1] / 3)
#         self.radius = 50

#     def draw_self(self)
#         pygame.draw.circle()

while still_playing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_playing = False

        #print(event)



    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()