import pygame
from operator import attrgetter

class MenuView():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def update(self, model):
        if (not model.active):
            return
        self.draw(model)
        
    def draw(self, model):
        #Menu Container & Border
        blue = (50,50,255)
        white = (255,255,255)
        black = (0,0,0)
        longestText = max([item.text for item in model.menuItems], key=self.font.size)
        textSize = self.font.size(longestText) #Width, height
        endX = model.x + (textSize[0]) + 8
        endY = model.y + (textSize[1] * len(model.menuItems)) + 4
        pygame.draw.rect(self.screen, black, (model.x-1, model.y-1, endX+2, endY+2), 3, 5)
        pygame.draw.rect(self.screen, blue, (model.x, model.y, endX, endY), 0, 5)
        pygame.draw.rect(self.screen, white, (model.x, model.y, endX, endY), 4, 5)

        #Menu Items
        for i in range(len(model.menuItems)):
            x = model.x + 8
            y = model.y + (i * textSize[1])
            width = textSize[0]
            height = textSize[1]
            textSurface = None
            if (i == model.selected):
                pygame.draw.rect(self.screen, white, (x-2, y+5, width+2, height-5), 0, 2)
                textSurface = self.font.render(model.menuItems[i].text, False, blue)
            else:
                textSurface = self.font.render(model.menuItems[i].text, False, white)
            self.screen.blit(textSurface, (x, y))
