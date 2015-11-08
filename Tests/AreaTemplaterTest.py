from Processes.AreaTemplater import AreaTemplater
from Classes.Area import Area
from Classes.Controller import Controller


class AreaTemplaterTest:
    def __init__(self, test_path):
        self.testPath = test_path

    def test(self):
        area_test = self.mock_area()
        templater = AreaTemplater(self.testPath, area_test)
        templater.process_area()

    def mock_area(self):
        area = Area('Test')
        controller = Controller('Test1Controller')
        controller.add_action('Test1')
        controller.add_action('Test2')
        area.add_controller(controller)
        controller = Controller('Test2Controller')
        controller.add_action('Test')
        return area
