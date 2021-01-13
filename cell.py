from element import Element

class Cell(Element):
    def __init__(self, y, x, imageType):
        super().__init__(y, x, imageType)
        self.passable = True