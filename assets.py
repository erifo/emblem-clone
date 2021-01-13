import os, pygame
from enum import Enum

class ImageTypes(Enum):
    NONE = 0
    TILE_GRASS = 1
    TILE_WATER = 2
    TILE_WOOD = 3
    UNIT_HERO = 4
    UNIT_BANDIT = 5


class Assets():
    def __init__(self):
        self.images = {}
        self.audio = {}
        self.loadAllImages()
    
    def loadImagePNG(self, imageType, filename):
        img = pygame.image.load(os.path.join('images', filename)).convert_alpha()
        self.images[imageType] = img
    
    def loadAllImages(self):
        self.loadImagePNG(ImageTypes.NONE, "none.png")
        self.loadImagePNG(ImageTypes.TILE_GRASS, "grass.png")
        self.loadImagePNG(ImageTypes.TILE_WATER, "water.png")
        self.loadImagePNG(ImageTypes.TILE_WOOD, "wood.png")
        self.loadImagePNG(ImageTypes.UNIT_HERO, "hero.png")
        self.loadImagePNG(ImageTypes.UNIT_BANDIT, "bandit.png")