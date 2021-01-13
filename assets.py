import os, pygame
from enum import Enum

class ImageTypes(Enum):
    TILE_GRASS = 0
    TILE_WATER = 1
    TILE_WOOD = 2
    UNIT_HERO = 3
    UNIT_BANDIT = 4


class Assets():
    def __init__(self):
        self.images = {}
        self.audio = {}
        self.loadAllImages()
    
    def loadImagePNG(self, imageType, filename):
        img = pygame.image.load(os.path.join('images', filename)).convert_alpha()
        self.images[imageType] = img
    
    def loadAllImages(self):
        self.loadImagePNG(ImageTypes.TILE_GRASS, "grass.png")
        self.loadImagePNG(ImageTypes.TILE_WATER, "water.png")
        self.loadImagePNG(ImageTypes.TILE_WOOD, "wood.png")
        self.loadImagePNG(ImageTypes.UNIT_HERO, "hero.png")
        self.loadImagePNG(ImageTypes.UNIT_BANDIT, "bandit.png")