class Area:
	def __init__(self, name):
		self.name = name;
		self.controllers = [];

	def AddController(self, controller):
		self.controllers.append(controller);