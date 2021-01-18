class Menu():
    def __init__(self, model, view, controller):
        self.model = model
        self.view = view
        self.controller = controller
    
    def update(self):
        self.controller.update(self.model)
        self.view.update(self.model)