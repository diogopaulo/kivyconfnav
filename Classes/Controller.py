class Controller:
	def __init__(self, name):
		self.name = name;
		self.actions = [];

	def AddAction(self, action):
		self.actions.append(action);