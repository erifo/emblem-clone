import sys, pygame


class MenuController():
    def __init__(self):
        pass

    def update(self, model):
       for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_d): #Toggle menu
                    model.active = not model.active
                elif (not model.active):
                    continue
                elif (event.key == pygame.K_UP): #Move selection up
                    model.selectPrevious()
                elif (event.key == pygame.K_DOWN): #Move selection down
                    model.selectNext()
                elif (event.key == pygame.K_c): #Confirm
                    model.generateMenuItems()
                elif (event.key == pygame.K_x): #Cancel
                    pass
            if (event.type == pygame.QUIT):
                sys.exit()