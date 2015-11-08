class Area:
    def __init__(self, name):
        self.name = name
        self.controllers = []

    def add_controller(self, controller):
        self.controllers.append(controller)
