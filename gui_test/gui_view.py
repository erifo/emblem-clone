class GUI_View():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def update(self, model):
        pygame.display.flip()
    
    def